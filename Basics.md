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

### Where LLM Runs ?

LLMs run on remote servers provided by companies like Google, OpenAI, or Groq.

We access them using APIs.

Key Point:
- The model is not running locally
- API acts as a communication bridge

## Invocation

Invocation means sending input to the LLM and receiving a response.

In LangChain:
.invoke() is used to call the model.

Analogy:
Like asking a question to a person and getting an answer.

Key Point:
- It connects our code to the LLM
- It triggers the model to generate output

## Why Not Use LLM Directly ?

Using LLM directly via API can lead to:
- No structure
- Repetitive code
- Difficult to manage workflows

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