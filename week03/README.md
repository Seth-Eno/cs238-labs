# Week 3 Lab: Tokens

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~40 minutes
**Reading:** Chapter 3 (Tokens) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Predict how a tokenizer will chop up words, emoji, and numbers, and explain why that matters
- Explain why models struggle to count letters and multiply long numbers

---

## Before You Start

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week03
```

Run every script below from inside this folder with `uv run`.

**Working locally?** This lab uses `gemma4`, and the Part B tasks also try `qwen3.5:0.8b` and `llama3.2`.

---

# Part 1: Tokens (30 minutes)

A language model never sees your words. It sees *tokens*, chunks of text that are each swapped for an integer ID. `count_tokens` and `tokenize` show you the chunks, using the tokenizer behind GPT-4 unless you name another.

## 1.1 What's a Token? (7 minutes)

`tokens.py` splits five strings into tokens: a short word, a longer word, a very long word, an emoji, and an accented word.

```bash
uv run tokens.py
```

**Task 1 (the chapter's Exercise 1):** Open `my_tokens.py` and put your own strings on the four marked lines: your name, a long technical term from your major, a common English word, and an emoji. **Before running it**, guess whether each will be one clean token or shatter into pieces.

```bash
uv run my_tokens.py
```

How often was your guess right?

## 1.2 Letters the Model Can't See (10 minutes)

If a model only sees chunks, then counting the letters inside a word asks it to read something it can't see. `my_letters.py` asks the model to count letters in three words (showing each word's tokens beside the answer), then to spell "tokenization" backward, and checks each answer.

```bash
uv run my_letters.py
```

**Task 2:** Count the letters yourself. Which counts did the model get right? Did it spell "tokenization" backward correctly? Now try a word of your own: open `my_backward.py`, put your word on the marked line, and **before running it**, predict whether the model will get it right. Capital letters don't matter, so an answer that's right except for case still counts.

```bash
uv run my_backward.py
```

Look at the token pieces of your word and of its backward spelling: why is this task hard for a model and easy for you?

**Task 2B: try other models.** Every script so far has used `gemma4`. At the top of `my_letters.py` and `my_backward.py` is a line `MODEL = "gemma4:latest"`, marked `# ← change for Part B`. Change it to `"qwen3.5:0.8b"`, a model about a seventh of `gemma4`'s size, and run both scripts again. Then change it to `"llama3.2:latest"` and run them once more. Some things to watch for:
- Run `qwen3.5:0.8b` two or three times. Does it give the same letter count twice in a row? Can it reverse even a short word like "cat"?
- Does `llama3.2` do better on short words or long ones? It sometimes capitalizes its answer, which is why the checker ignores case.

## 1.3 Numbers Come in Chunks (13 minutes)

`my_number_chunks.py` shows how four numbers split into tokens, then asks `gemma4` to multiply 3947 × 6281. The true product is **24,791,107**.

```bash
uv run my_number_chunks.py
```

**Task 3:** Did the model get it right? If not, was its answer at least the right *size*? Now try your own: open `my_arithmetic.py`, keep the four starter problems, and replace the three example problems below them with your own. Each one is a number, an operation (`+`, `-`, `*`, or `/`), and another number. Include some you expect the model to get right and some you expect it to miss, and **before running it**, predict which is which.

```bash
uv run my_arithmetic.py
```

Python works out each true answer exactly, and the script marks the model right or wrong and shows how each number splits into tokens. Which problems did the model miss? Do short numbers and long numbers, or addition and multiplication, behave differently?

**Task 3B: try other models.** Change the `MODEL` line at the top of `my_number_chunks.py` and `my_arithmetic.py` to `"qwen3.5:0.8b"` and run both, then to `"llama3.2:latest"` and run them again. Some things to watch for:
- Run `qwen3.5:0.8b` more than once. Does it get even 47 + 38 right every time?
- `llama3.2` often lands *close* on the long problems. Check every digit of its answer to 123,456,789 + 987,654,321, and see how near its division gets. Close isn't correct.
- Look back at `gemma4`'s answer to 98,765 ÷ 43. Where did the decimal point go?

---

## Part 2: Lab Questions (10 minutes)

Open `lab3_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **Tokens (Tasks 1 and 2):** Which of your strings split the way you guessed, and which surprised you? Could `gemma4` spell your word backward? Why can't a model reliably count the letters in "strawberry"?
2. **Other models on letters (Task 2B):** Did `qwen3.5:0.8b` give the same letter count twice in a row? Could it reverse a short word like "cat"? Did `llama3.2` do better on short words or long ones? Which of the three models was best at letters?
3. **Numbers (Task 3):** What did `gemma4` answer for 3947 × 6281, and how do the three-digit chunks explain the mistake? Which of your own problems did it get right, and which did it miss? Where did the decimal point go in its answer to 98,765 ÷ 43?
4. **Other models on numbers (Task 3B):** Did `qwen3.5:0.8b` get 47 + 38 right every time you ran it? How close did `llama3.2` get on 123,456,789 + 987,654,321 and on the division, and was it ever exactly right? Which model did best on your own problems? Why might a model land *close* to the right answer without getting it exactly?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab3_results.txt` to the **Week 3 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week03` folder.

- **Prose versus code (Tokens Exercise 3).** In `optional/my_prose_vs_code.py`, put a paragraph of English and a Python snippet of about the same length on screen. Predict which costs more tokens, then run it. It also tries the snippet with tabs instead of spaces.
  ```bash
  uv run optional/my_prose_vs_code.py
  ```
- **A newer tokenizer.** `optional/multilingual.py` runs one sentence in English, Spanish, Hindi, and Japanese through GPT-4's tokenizer and GPT-4o's newer one, which learned from much more non-English text. Which language gets the biggest discount? Add a sentence in a language you know.
  ```bash
  uv run optional/multilingual.py
  ```
