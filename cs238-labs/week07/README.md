# Week 7 Lab: Giving the Model Hands

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 7 (Agentic) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Describe a tool to a model (its name, description, and parameters) and let the model decide when to call it
- Build a tool of your own and watch an agent loop call it, read the result, and answer
- Show that a tool's *name* and *description* decide whether the model ever reaches for it
- Use self-critique and self-rated confidence to catch a thin or shaky answer before a user sees it

---

## Before You Start

- Completed the earlier labs
- Read Chapter 7

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week07
```

Run every script below from inside this folder with `uv run`.

**Working locally?** This lab uses `gemma4`.

---

## Part 1: Sophia Gets Hands (10 minutes)

A tool reaches the model as a function name, a one-sentence description, and a list of parameters. The model never runs anything itself: it *asks* for a call, our program runs it and hands back the result, and the model decides what to do next. That loop is the agent.

`sophia.py` shows the three tools from the chapter (a calculator, a glossary lookup, and a note-keeper) exactly as the model receives them. Then it sends one run-on request that needs all three. The glossary lookup reads `glossary.md` in this folder, the glossary from the back of the book.

```bash
uv run sophia.py
```

Each `TOOL` line is one call `gemma4` chose to make (with its arguments and what came back), and the `SOPHIA` line is the answer it wrote once the tools were done. Nothing in the code told it which tool to use for which part.

`small_talk.py` gives Sophia the same three tools but a message that needs none of them: "Thanks, you've been a huge help today!"

```bash
uv run small_talk.py
```

**Task 1:** In `sophia.py`, which tools did it call, with what arguments? Did it do the arithmetic itself or hand it to the calculator? In `small_talk.py`, did it call any tools? A *deliberate* caller calls none; an *eager* one reaches for something anyway.

---

## Part 2: Build Your Own Tool (13 minutes)

Models can't know today's date or count days reliably, which makes a date tool a good first build. `date_tool.py` defines a Python function, `days_until`, describes it to the model with `tool_spec`, and asks how many days are left until December 25, 2026.

```bash
uv run date_tool.py
```

Look at `days_until` in the file. When the model passes a bad argument, it returns a polite, readable error instead of crashing, so the model can try again.

**Task 2:** Open `my_tool.py`. It already has the date tool plus an example second tool, `count_letter` (remember the strawberry problem from Week 3?). Replace `count_letter` with a tool of your own: something a language model is bad at on its own. Change the four marked spots: the Python function, its `tool_spec` (name, description, and parameters), and its entry in `handlers`. Some ideas:
- `word_count(text)`: count the words in a passage
- `convert_units(value, from_unit, to_unit)`: a handful of conversions you choose
- `roll_dice(sides, count)`: something a model can't do fairly on its own

Then write three requests on the marked lines: one that should use your tool, one that should use *both* tools, and one that should use *neither*.

```bash
uv run my_tool.py
```

Did the model make the right call each time?

---

## Part 3: Labels Decide Everything (10 minutes)

A tool reaches the model as two labels, its *name* and its *description*. `labels.py` asks the date question with the same date tool labeled four ways: both labels clear, a vague name (`fn`), a vague description ("Returns a number for the given input."), and both vague. For each one, it shows every call the model made, with what it passed in and what came back.

```bash
uv run labels.py
```

**Task 3:** Did the model call the tool in every version? Look at what it passed in. Which versions got the date format right on the first try, and which had to read the tool's error message and try again? Only one of the two labels says what format the tool expects: which one? The chapter found that some models ignore a tool entirely when both labels are vague. Why is a tool whose description doesn't explain its inputs a problem even when the model does call it?

---

## Part 4: Who Knows What They Don't Know? (10 minutes)

Two cheap safety nets from the chapter. *Self-refine*: the model drafts an answer, critiques its own draft in one sentence, then rewrites it. *Self-rated confidence*: the model rates how sure it is from 1 to 5, and a low score holds the answer back for a human. `self_check.py` runs self-refine on a question about RAG, then rates its confidence on an answerable question and an impossible one.

```bash
uv run self_check.py
```

**Task 4:** Did the critique make the final answer better, or just longer? How did the confidence scores compare between the answerable and the impossible question? Then open `my_confidence.py` and write three questions of your own on the marked lines: two impossible ones (about the future, about you, about something private) and one tricky question it *might* know.

```bash
uv run my_confidence.py
```

Does the score track how answerable each one really is?

---

## Part 5: Lab Questions (5 minutes)

Open `lab7_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **The loop (Tasks 1 and 2):** In your own words, who actually runs a tool: the model or your program? What tool did you build, and did the model use it correctly on all three of your requests?
2. **Labels (Task 3):** In which versions did the model pass the right date format on the first try, and in which did it need the error message to recover? If you were writing tools for a real assistant, what would you make sure every description and every error message says?
3. **Self-checks (Task 4):** What confidence scores did your impossible questions get? Would you trust this model's confidence score enough to automatically hide answers it rates 1 or 2? Why or why not?
4. **Reflection:** The chapter's recurring lesson is that "there's no best model, only best-at-something models." What's one thing you'd want to test before letting a model take real actions (sending email, spending money) on your behalf?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab7_results.txt` to the **Week 7 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week07` folder.

- **Hold your own audition (the chapter's Exercise 1).** `optional/audition.py` sends a request that needs the calculator and one that needs no tool at all to another tool-capable model (`llama3.2` by default; change `MODEL` to try others). Run it a few times. Does it write the arithmetic correctly every time, and how does it handle the thank-you? Is it more deliberate or more eager than `gemma4`?
  ```bash
  uv run optional/audition.py
  ```
- **Watch reflection rescue a coder (Exercise 3).** `optional/reflexion.py` shows one fail → lesson → pass cycle: the code fails a test, `gemma4` writes itself a one-sentence lesson, and the second try passes. Why does one written lesson beat simply retrying?
  ```bash
  uv run optional/reflexion.py
  ```
- **Route by difficulty.** Read the chapter's *Economics* section, then run `optional/routing.py`. It sends an easy, a medium, and a hard task (answers: 3000, 0.05, and 4) to `gemma4` and to the smaller `llama3.2`. Which tasks could you safely route to the cheaper model?
  ```bash
  uv run optional/routing.py
  ```
