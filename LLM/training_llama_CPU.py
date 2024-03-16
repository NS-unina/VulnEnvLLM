#!/usr/bin/env python
# coding: utf-8

# - The %%capture magic command is used to suppress the output of the cell in Jupyter notebook.
# - The %pip magic command is used to install Python packages within a Jupyter notebook: accelerate, peft, bitsandbytes, transformers, and trl are the names of the Python packages being installed.
# - These packages are installed in the current Python environment running the Jupyter notebook.

# In[1]:

import pdb
#get_ipython().run_cell_magic('capture', '', "# Uncomment if you haven't these packages\n# %conda install accelerate peft bitsandbytes transformers trl huggingface_hub tensorboard\n# %pip install trl # not available in conda channels\n")


# In[2]:


import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:64" 
os.environ['XLA_USE_BF16'] = "1"
os.environ['XLA_TENSOR_ALLOCATOR_MAXSIZE'] = '100000000'


# In[3]:


from huggingface_hub import login
#login()


# In[4]:


# pip install datasets transformers torch peft trl
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig
from trl import SFTTrainer


# In[5]:


# Model from Hugging Face hub
base_model = "meta-llama/Llama-2-7b-hf"
# Fine-tuned model
new_model = "llama-2-7b-dockerfile-generation"
# Load the model
dataset = load_dataset("mlabonne/guanaco-llama2-1k", split="train")


# In[6]:


model = AutoModelForCausalLM.from_pretrained(
    base_model,
    device_map="cpu"
)
model.config.use_cache = False
model.config.pretraining_tp = 1


# In[7]:


# Load the tokenizer from Hugginface and set padding_side to “right” to fix the issue with fp16
tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"


# List of hyperparameters that can be used to optimize the training process:
# 
# - **output_dir**: The output directory is where the model predictions and checkpoints will be stored.
# - **num_train_epochs**: One training epoch.
# - **fp16/bf16**: Disable fp16/bf16 training.
# - **per_device_train_batch_size**: Batch size per GPU for training.
# - **per_device_eval_batch_size**: Batch size per GPU for evaluation.
# - **gradient_accumulation_steps**: This refers to the number of steps required to accumulate the gradients during the update process.
# - **gradient_checkpointing**: Enabling gradient checkpointing.
# - **max_grad_norm**: Gradient clipping.
# - **learning_rate**: Initial learning rate.
# - **weight_decay**: Weight decay is applied to all layers except bias/LayerNorm weights.
# - **Optim**: Model optimizer (AdamW optimizer).
# - **lr_scheduler_type**: Learning rate schedule.
# - **max_steps**: Number of training steps.
# - **warmup_ratio**: Ratio of steps for a linear warmup.
# - **group_by_length**: This can significantly improve performance and accelerate the training process.
# - **save_steps**: Save checkpoint every 25 update steps.
# - **logging_steps**: Log every 25 update steps.

# In[8]:


peft_params = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,
    bias="none",
    task_type="CAUSAL_LM",
)

training_params = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    optim="paged_adamw_8bit",
    save_steps=25,
    logging_steps=25,
    learning_rate=2e-4,
    weight_decay=0.001,
    fp16=False,
    bf16=False,
    max_grad_norm=0.3,
    max_steps=-1,
    warmup_ratio=0.03,
    group_by_length=True,
    lr_scheduler_type="constant",
    report_to="tensorboard",
    use_cpu=True
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_params,
    dataset_text_field="text",
    max_seq_length=1024,
    tokenizer=tokenizer,
    args=training_params,
    packing=False
)


# In[ ]:


# Train the model
pdb.run("trainer.train()")


# In[ ]:


# Save the model
trainer.model.save_pretrained(new_model)
trainer.tokenizer.save_pretrained(new_model)


# In[ ]:


# pip install tensorboard
from tensorboard import notebook
log_dir = "resultpips/runs"
notebook.start("--logdir {} --port 4000".format(log_dir))
# Test the model
logging.set_verbosity(logging.CRITICAL)
prompt = "Generate a Dockerfile of Python 2.7"
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])


# In[ ]:





# In[ ]:




