## LLM

A Large Language Model is a system trained on huge text data that generates responses by predicting the next sequence of words based on input. It can perform tasks like answering questions, summarizing, and explaining concepts.

---

## LangChain

LangChain is a framework used to build applications with LLMs by organizing workflows such as prompt management, chaining multiple steps, maintaining memory, and enabling tool usage.

It provides structure like prompts, chains, memory, etc.

### How LLM Works ?

An LLM generates text by predicting the next sequence of words based on the given input.

Flow:
Input → Model processes → Output

Key Point:
- It does not "know" facts like a database
- It predicts based on patterns learned during training

## Invocation

Invocation means sending input to the LLM and receiving a response.

In LangChain:
.invoke() is used to call the model.

Analogy:
Like asking a question to a person and getting an answer.

Key Point:
- It connects our code to the LLM
- It triggers the model to generate output