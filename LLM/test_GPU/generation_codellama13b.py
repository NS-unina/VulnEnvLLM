import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from scripts.improve_result import improve_result, generate_constraints
from huggingface_hub import login
from os import path, chdir
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing_extensions import Annotated
import typer


def return_forced_words_ids(prompt: str, tokenizer) -> list:
    """
    Returns a list of forced word IDs based on the given prompt and tokenizer.

    Args:
        prompt (str): The prompt string.
        tokenizer: The tokenizer object.

    Returns:
        list: A list of forced word IDs.
    """
    image_name = generate_constraints(prompt)
    forced_words_ids = []

    if image_name != "":
        forced_words_ids.append(tokenizer(f"FROM {image_name}\n", add_special_tokens=True).input_ids)
    else:
        forced_words_ids.append(tokenizer("FROM", add_special_tokens=True).input_ids)
    forced_words_ids.append(tokenizer(["```dockerfile\n", "```Dockerfile\n"], add_special_tokens=True).input_ids)
    forced_words_ids.append(tokenizer(["ARG DEBIAN_FRONTEND noninteractive\n", "ARG debian_frontend noninteractive\n"], add_special_tokens=True).input_ids)

    return forced_words_ids


def generate_text(tokenizer, model, prompt: str) -> str:
    """
    Generate text based on a given prompt using a tokenizer and a model.

    Args:
        tokenizer (Tokenizer): The tokenizer used to tokenize the input text.
        model (Model): The model used for text generation.
        prompt (str): The prompt to generate text from.

    Returns:
        str: The generated text.

    """
    bad_words = ["apk", "\begin(code)", "\\end(code)", "EOF", "exit", "ONBUILD", "alpine", "# FROM", "#FROM"]
    bad_words_ids = tokenizer(bad_words, add_special_tokens=False).input_ids
    prompt = "<s>[INST] Generate a dockerfile of " + prompt + " [/INST]"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")  # Added last part to avoid crash to KeyError: 'shape'
    # beam-search multinomial sampling if num_beams>1 and do_sample=True
    gen_tokens = model.generate(input_ids, bad_words_ids=bad_words_ids, force_words_ids=return_forced_words_ids(prompt, tokenizer), max_new_tokens=512, no_repeat_ngram_size=7, num_beams=5, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    result = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0]  # One element list, just the response
    return improve_result(prompt, result)


def main(prompt: Annotated[str, typer.Argument(help="The prompt to generate the Dockerfile")], save_dir:Annotated[str, typer.Argument(help="File name to save the dockerfile")]="generated.Dockerfile"):
    '''
    Ex: "python3 generate_dockerfile.py 'Wordpress 5.7'"
    '''
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"),transient=True,) as progress:
        chdir(path.dirname(path.abspath(__file__)))  # change working directory to script location
        # Hugging-face login
        progress.console.print("\n[green]Copy and paste HuggingFace Token here and press enter, ignore this if you've already logged in.")
        login(new_session=False, add_to_git_credential=False)

        p = progress.add_task(description="Loading Model..", total=None)

        compute_dtype = getattr(torch, "float16")
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
            attn_implementation="flash_attention_2",
        )
        model_name = "Tony177/codellama-13b-dockerfile-generation"
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=quant_config,
            device_map="auto",
        )
        model.config.use_cache = True
        model.config.pretraining_tp = 1 # Setting config.pretraining_tp to a value different than 1 will activate the more accurate but slower computation of the linear layers, which should better match the original logits.
        model.enable_input_require_grads() # Warning about gradients during generation

        progress.remove_task(p)
        p = progress.add_task(description="Loading Tokenizer..", total=None)

        # Load the tokenizer from Hugginface and set padding_side to “right” to fix the issue with fp16
        tokenizer = AutoTokenizer.from_pretrained(model_name, device_map="auto")
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "left"
        progress.remove_task(p)
        p = progress.add_task(description="Generating Dockerfile..", total=None)
        result = generate_text(tokenizer, model, prompt)
        with open(save_dir,'w') as f:
            f.write(result)
        progress.remove_task(p)
        progress.console.print(f"\n[green]File saved in {save_dir}")



if __name__ == "__main__":
    typer.run(main)