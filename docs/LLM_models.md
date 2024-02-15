# Fine Tuning
### Pros of Fine Tuning of LLM Models:

- Adaptability to specific tasks: Fine-tuning allows an LLM model to be adapted to a particular task, making it highly specialized for that application. This makes it very flexible and suitable for a wide range of natural language processing tasks.
- Performance improvement: Basic LLM models, such as GPT-3 or BERT, have a general understanding of language, but may not be optimal for specific tasks. Fine-tuning can greatly improve performance on those tasks, often outperforming other specialized models.
- Time and resource savings: Training an LLM model from scratch requires enormous resources in terms of time and computing power. Fine-tuning is usually faster and more efficient because it is based on a pre-trained base model.
- Need for less labeled data: While training from scratch requires large amounts of labeled data, fine-tuning can be accomplished with smaller datasets, which is useful when labeled data is limited.

### Cons of Fine Tuning of LLM Models:

- Dependence on fine-tuning data: The quality of the fine-tuned model depends on the quality of the labeled data used in the fine-tuning process. If the labeled data are not representative or contain bias, the model inherits these issues.
- Overfitting: Excessive fine-tuning on a specific dataset can lead to the phenomenon of overfitting, in which the model overfits the training data and does not generalize well to new data.
- Computational resources: Although fine-tuning is more efficient than training from scratch, it still requires significant computational resources to perform the process, particularly for large LLM models.
- Maintenance and upgrades: Fine-tuned models may require ongoing maintenance to remain aligned with the evolving needs of the task. Upgrades require restarting the fine-tuning process.
- Complexity in base model selection: Choosing which base model to use as a starting point for fine-tuning can be a critical decision and requires a good understanding of the specific needs of the task.

# Prompt Engineering
### Pros of Prompt Engineering with LLM Models:

- Flexibility: Prompt engineering offers a high degree of flexibility in adapting an LLM template to a wide range of tasks. Specific prompts can be defined for the desired task, allowing precise control over text generation.
- Speed of implementation: Implementation of prompt engineering is often faster than fine-tuning an LLM model. There is no need to train the model from scratch or collect large amounts of labeled data.
- Increased performance: A well-designed prompt can improve the performance of the LLM model on specific tasks. This can translate into increased accuracy and consistency in text generation.
- Reduced resources: Compared with fine-tuning, prompt engineering requires fewer computational resources and is lighter in terms of memory and computing power.

### Cons of Prompt Engineering with LLM Models:

- Complexity in prompt design: Creating effective prompts requires careful analysis of the specific task and requirements. An inappropriate prompt can lead to unsatisfactory results.
- Semantic limitations: LLM models with prompt engineering can be limited by the semantic capacity of the prompts themselves. If a task requires understanding beyond the syntax of the prompt, the model may fail.
- Sensitivity to changes in input data: Models with prompt engineering may be sensitive to small changes in input data.
- Complexity in optimization: Prompt tuning can be an iterative process, and finding the optimal prompt can take considerable time and effort.
- Possibility of inconsistent generation: In some cases, models with prompt engineering may generate inconsistent or irrelevant output if prompts are worded ambiguously or non-specifically.

# Generative Models
### Pros of Generative LLM Models:

- Creative Text Generation: These models excel at generating creative text, including writings, poetry, fiction, and more. They are often used in applications that require the creation of original content.
- Automatic Phrase Completion: They can be used to complete sentences or text in a consistent manner. This feature is useful in applications such as autocorrect, text prediction and assisted writing.
- Dialogue Applications: Generative models are often employed in chatbots and dialogue systems, as they can generate responses to user input in a natural and consistent manner.
- Scalability: Generative models can be scaled to fit a wide range of tasks and data. They are capable of dealing with tasks of varying sizes.

### Cons of Generative LLM Models:

- Risk of Generating Inappropriate Content or Bias: Generative models can generate content that is inappropriate or contains bias. This is an ethical concern and requires moderation and control measures.
- Lack of Control: In some cases, these models may generate inconsistent or irrelevant text, and there is not always precise control over generation.
- Overfitting: Generative models may suffer from overfitting, particularly if they are trained on data of limited size or if the training process is not properly adjusted.
- Demand for Computational Resources: High-quality generative models require considerable computational resources for training and inference. They may not be practical on devices with limited resources.
- Variability in Quality of Generated Text: The quality of generated text can vary widely depending on the conditions and mode of generation, and may require significant optimization to achieve desired results.

# Differences between approaches
The main differences between these approaches concern the main goal and method of driving the model:
-  Generative **approaches** are designed to generate text independently, without the need for specific instructions. These models create text based on training data and knowledge learned during pre-training.
- In **prompt engineering**, specific instructions or prompts are used to guide the model in generating text. These prompts provide a structure or context for the task to be performed. The goal is to obtain consistent and specific responses.
- In contrast, **fine-tuning** involves fitting a pre-trained model to specific tasks using labeled data. This process improves the performance of the model on a specific task, making it more accurate.

  
# Large Language Model

- Llama (Non-commercial/research license)
- Llama 2 ([Llama2 License ](https://ai.meta.com/llama/license/) not open-source)
- Falcon ([Apache 2.0](https://www.linux.it/opensource/licenze/licenses/apache-2.0/))
- GPT-3 (Obtainable only via interface)
- GPT-Neo ([MIT License](https://www.linux.it/opensource/licenze/licenses/mit/), slightly lower performance GPT-3)
- GPT-J ([Apache 2.0](https://www.linux.it/opensource/licenze/licenses/apache-2.0/), similar style GPT-3)
- GTP-4 (Payment Plus 20€/mo)
