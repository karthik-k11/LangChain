# Basics

## LLM

A Large Language Model (LLM) is a system trained on a huge amount of text data that generates responses by predicting the next sequence of words based on the given input.

It can perform tasks such as:
- Answering questions
- Summarizing text
- Explaining concepts
- Generating content

---

## LangChain

LangChain is a framework used to build applications with Large Language Models (LLMs). It provides a structured way to interact with LLMs by offering components such as prompts, chains, memory, tools, and agents.

Instead of making raw API calls everywhere in the application, LangChain helps organize the workflow into reusable and maintainable components.

---

## How LLM Works

An LLM generates text by predicting the next sequence of words based on the given input.

### Flow

Input

↓

Model processes the input

↓

Generated Output

### Key Points

- An LLM does not "know" facts like a database.
- It generates responses by predicting patterns learned during training.
- The quality of the output depends on the input provided.

---

## Where LLM Runs

LLMs run on remote servers provided by companies such as Google, OpenAI, or Groq.

Our application communicates with those models through APIs.

### Key Points

- The model does not run on our local computer.
- APIs act as the communication bridge between our application and the LLM.

---

## Invocation

Invocation means sending an input to the LLM and receiving a generated response.

In LangChain, `.invoke()` is commonly used to communicate with the model.

### Real-world Analogy

Imagine asking a question to a teacher.

You ask the question.

↓

The teacher thinks.

↓

The teacher gives the answer.

Similarly, `.invoke()` sends the prompt to the model and returns the response.

### Key Points

- `.invoke()` sends our input to the model.
- The model processes the request.
- LangChain returns a response object.

---

## Response Object

LangChain does not return only plain text.

Instead, it returns a response object that contains additional information such as:

- Generated content
- Metadata
- Model information
- Token usage
- Response ID

This information is useful for debugging, monitoring, logging, and tracking API usage.

---

## Why do we use `.content`?

The response returned by LangChain is an object.

To display only the generated answer, we use:

```python
response.content
```

Without `.content`, the entire response object is printed, including metadata and other information.

---

## Why Not Use LLM Directly?

Using an LLM directly through API calls can lead to:

- Repetitive code
- Poor structure
- Difficult maintenance
- Less reusable workflows

<<<<<<< HEAD
LangChain solves these problems by providing reusable components such as prompts, chains, memory, tools, and agents.
=======
LangChain solves this by:
- Providing structure
- Managing prompts
- Supporting chains and memory

## Prompt Template

Prompt Template is a reusable prompt structure containing placeholders.

Example:
"Explain {topic} in simple words"

Here:
{topic} is a placeholder.

Benefits:
- reusable
- reduces repetition
- easier maintenance
- consistency

## input_variables

input_variables tells LangChain which placeholders are expected inside the template.

Example:
template="Explain {topic}"

input_variables=["topic"]

This helps LangChain validate and organize prompt inputs properly.

## format()

.format() replaces placeholders dynamically with actual values.

Example:

Before formatting:
"Explain {topic}"

After formatting:
"Explain AI"

# Langchain Definition: 

LangChain helps organize and structure interactions with LLMs instead of making raw API calls directly.

It provides reusable workflows using prompts, templates, chains, memory, and agents.

Langchain acts as the bridge between the LLM and outside sources (like pdf, general interne, etc..)
>>>>>>> f92036c43e48283e55cfe23192128b5c3b74f502
