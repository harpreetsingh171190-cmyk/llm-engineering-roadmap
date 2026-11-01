# Part 3: The LLM Engineer

This part is about using language models in real products. The focus is on running models efficiently, connecting them to data, and deploying them safely.

## Running LLMs

Before building anything, learn to run a model and send it prompts. Important choices include the model size, the prompt format, and the sampling settings such as temperature.

## Building a vector store

Many applications need the model to use information it was not trained on. A **vector store** holds text as embeddings, so the application can find passages similar in meaning to a question.

## Retrieval-augmented generation (RAG)

RAG combines search with generation. The steps are:

1. Split documents into chunks.
2. Store the chunk embeddings in a vector store.
3. For each question, retrieve the most relevant chunks.
4. Give those chunks to the model as context for its answer.

RAG reduces made-up answers and lets the system use up-to-date information.

## Advanced RAG

Basic RAG can fail when the question is vague or the answer spans many documents. Improvements include better chunking, reranking retrieved results, and rewriting the user's question before searching.

## Agents

An agent is a model that can call tools, such as a search function or a calculator, and decide what to do next. Agents need clear tool descriptions, limits on how many steps they can take, and checks on their actions.

## Inference optimization

Serving a model to many users is expensive. Common techniques include batching requests, caching repeated work, using quantized weights, and choosing the right hardware.

## Deploying LLMs

Deployment means exposing the model through an API that is reliable and measurable. Good practice includes:

- Packaging the service in a container.
- Logging requests and latency.
- Setting timeouts and rate limits.
- Monitoring quality over time.

## Securing LLMs

LLM applications have their own risks. The main ones are prompt injection, where untrusted text tries to override instructions, and data leakage. Defenses include validating inputs and outputs, limiting what tools an agent can use, and never trusting model output as code without review.

## Suggested project

Build a small question-answering app over your own documents. Use RAG, add a simple evaluation set with ten questions and expected answers, and deploy it behind a basic API with logging.

## Resources

See the [Engineer section of the course](../README.md#-the-llm-engineer) for the full list of links.
