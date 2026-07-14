# Chains

## What is a Chain?

A Chain is a workflow that connects multiple LangChain components together.

The output of one component automatically becomes the input of the next component.

---

## Why do we need Chains?

Without Chains, we manually connect every step.

For example:

Prompt Template

↓

Format Prompt

↓

LLM

↓

Response

↓

Extract Content

This becomes repetitive as applications grow.

Chains automate this workflow.

---

## Real-world Analogy

Think of ordering food at a restaurant.

You place the order once.

The cashier sends it to the kitchen, the chef prepares it, and the waiter brings it to your table.

You don't have to coordinate every person yourself.

A Chain works the same way.

---

## Benefits

- Reduces repetitive code
- Automates workflows
- Easier to maintain
- Easy to extend
- Cleaner code

---

## Why is it called LangChain?

The framework is called LangChain because it connects different language-processing components into a workflow.

## Building vs Executing a Chain

Creating a chain does not execute it.

Example:

chain = prompt | llm

This only creates the workflow by connecting the Prompt Template and the LLM.

The workflow runs only when:

response = chain.invoke({"topic": "Artificial Intelligence"})

Key Points:
- `|` builds the workflow.
- `.invoke()` executes the workflow.