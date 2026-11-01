# Part 1: LLM Fundamentals

This part is optional. It gives the background needed to understand how language models work. Readers with a strong math and programming background can skip ahead to [Part 2](02-scientist.md).

## Mathematics for machine learning

Models are built from vectors, matrices, and probability. The most useful ideas are:

- **Linear algebra:** vectors and matrix multiplication. Every layer of a neural network is a matrix operation.
- **Calculus:** derivatives and the chain rule. They explain how a model learns from its errors.
- **Probability and statistics:** distributions, expectation, and maximum likelihood. Language models predict the next token as a probability distribution.

## Python for machine learning

Most LLM tools are written in Python. Focus on:

- Working with NumPy arrays and tensor shapes.
- Using PyTorch to define models and run training loops.
- Reading and writing code clearly, with functions, classes, and tests.

## Neural networks

A neural network is a stack of simple functions with learnable weights. The key concepts are:

- **Forward pass:** input flows through layers to produce a prediction.
- **Loss function:** a number that measures how wrong the prediction is.
- **Backpropagation and gradient descent:** the method that adjusts weights to reduce the loss.
- **Overfitting and regularization:** why a model can memorize training data and how to prevent it.

## Natural language processing

NLP is the field that turns text into numbers and back. Important steps include:

- **Tokenization:** splitting text into units the model can process.
- **Embeddings:** representing each token as a vector that captures meaning.
- **Sequence models:** earlier approaches such as recurrent networks, which helped set the stage for transformers.

## Why it matters

Without these foundations, the rest of the course looks like a list of tricks. With them, each technique in Parts 2 and 3 becomes a logical step.

## Suggested exercise

Train a small neural network on a text classification task, such as sentiment analysis. Measure the loss over time, then try a different tokenizer and compare the results.

## Resources

See the [Fundamentals section of the course](../README.md#-llm-fundamentals) for the full list of links.
