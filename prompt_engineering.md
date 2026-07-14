# Prompt Engineering

## What is Prompt Engineering?

Prompt Engineering is the process of designing prompts clearly and effectively so that the AI model generates accurate, useful, and consistent responses.

---

## Why is Prompt Engineering Important?

The quality of the AI's response depends heavily on how the prompt is written.

A clear prompt usually produces a better response than a vague prompt.

---

## Real-world Analogy

Imagine giving instructions to a new employee.

Instead of saying:

"Do something with the data."

You say:

"Analyze this CSV file and summarize the top 3 sales trends."

The second instruction is much clearer, so the employee can do the task correctly.

The same idea applies to AI models.

---

# Prompt Template

## What is a Prompt Template?

A Prompt Template is a reusable prompt structure that contains placeholders.

Example:

Explain {topic} in simple words.

Here, `{topic}` is a placeholder.

---

## input_variables

`input_variables` tells LangChain which placeholders are expected inside the template.

Example:

input_variables = ["topic"]

---

## format()

`.format()` replaces the placeholders with actual values.

Example:

Before:

Explain {topic}

After:

Explain Artificial Intelligence

---

## Benefits

- Reduces repetitive work
- Makes prompts reusable
- Keeps prompts consistent
- Easier to maintain