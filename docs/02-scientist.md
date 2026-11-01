# Part 2: The LLM Scientist

This part is about building the best possible language models. It covers the design choices, training methods, and evaluation techniques used by model developers.

## The LLM architecture

Most modern language models use the **transformer**. Its core idea is **attention**, which lets each token look at other tokens in the sequence and decide which ones matter. Key parts include:

- Multi-head self-attention.
- Positional encodings, which tell the model the order of tokens.
- Feed-forward layers and normalization, which keep training stable.

## Pre-training models

Pre-training teaches a model general language skills by predicting the next token on very large amounts of text. The main questions are how much data to use, how big the model should be, and how to clean the data.

## Post-training datasets

A pre-trained model is not yet useful as an assistant. Post-training uses curated examples of instructions and good answers. Dataset quality usually matters more than dataset size.

## Supervised fine-tuning

Supervised fine-tuning (SFT) trains the model on instruction and answer pairs. Methods such as LoRA update only a small set of extra weights, which makes fine-tuning much cheaper.

## Preference alignment

Alignment teaches the model which answers people prefer. Common approaches include reinforcement learning from human feedback (RLHF) and simpler methods such as Direct Preference Optimization (DPO), which learn directly from pairs of preferred and rejected answers.

## Evaluation

Measuring model quality is difficult. Good evaluation combines:

- Automatic benchmarks on fixed tasks.
- Human review of real examples.
- Checks for errors, bias, and unsafe output.

Always test on data the model has not seen during training.

## Quantization

Quantization stores weights with fewer bits, such as 8-bit or 4-bit, so a model uses less memory and runs faster. There is a trade-off: smaller formats can lose some accuracy, so the result should be measured.

## New trends

The field changes quickly. Recent directions include mixture-of-experts models, longer context windows, and reasoning-focused training. Follow research papers and model release notes to keep up.

## Suggested exercise

Fine-tune a small open model on a narrow task, evaluate it before and after training, and write a short report on what changed.

## Resources

See the [Scientist section of the course](../README.md#-the-llm-scientist) for the full list of links.
