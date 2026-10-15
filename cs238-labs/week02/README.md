# Week 2 Lab: Prompting

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 2 (Prompting) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Explain what temperature, top-k, and top-p each do to the model's next-token forecast
- Use few-shot examples, and tell when they're worth the tokens
- Spot the "pink elephant" problem with negative instructions, and rewrite a ban as a positive
- Try chain-of-thought and step-back prompting, and notice when they rescue an answer and when they don't

---

## Before You Start

- Completed the Week 1 lab (your `cs238` folder set up and pointed at the class server)
- Read Chapter 2

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week02
```

Run every script below from inside this folder with `uv run`. Close chart windows to let a script continue.

**Working locally?** This lab uses `gemma4` and `llama3.2`.

---

## Part 1: The Control Panel (15 minutes)

### 1.1 Temperature

`temperature.py` is the chapter's temperature sweep: one story prompt at temperatures `0.0`, `0.7`, and `1.5`. Run it twice:

```bash
uv run temperature.py
```

The `0.0` opening should come back word for word; the `1.5` one should wander.

### 1.2 Seeing the Dials

Temperature *reshapes* the odds; top-k and top-p *trim* which words are allowed at all. `dials.py` first draws the chapter's picture of both on a real forecast ("She opened the door and saw a"), then pushes the dials to their limits on one beach sentence: safe settings, high temperature with the top-k/top-p "brakes" on, and high temperature with the brakes off.

```bash
uv run dials.py
```

"Hot only" should still hold together; "brakes off" should fall apart.

### 1.3 Your Turn: Count the Answers

One sample tells you very little, so these two scripts ask the same question six times at each temperature and count the answers.

`count_animals.py` asks for an animal at temperatures `0.0`, `1.0`, and `2.0`, then once more at `2.0` with `top_k=1`:

```bash
uv run count_animals.py
```

`count_numbers.py` asks for "a random number between 1 and 10" the same way. **Before running it**, predict what you'll see at temperature 2.0.

```bash
uv run count_numbers.py
```

**Task 1:** How many different answers did each prompt give at each temperature? Why does `top_k=1` give the same animal every time, even at the highest temperature? And why do you think the "random" number barely moves? (Think back to *peaked* versus *spread* forecasts from Week 1.)

---

## Part 2: When Do Examples Earn Their Tokens? (8 minutes)

*Few-shot* prompting puts a handful of labeled examples in the prompt so the model can copy the pattern. The chapter's classifier sorts student emails into LOGISTICS, CONCEPTUAL, or DEBUGGING, and found that `gemma4` needs *zero* examples when the label names explain themselves, but falls apart when the labels are meaningless codes. `few_shot_codes.py` tests the second half of that: five student questions labeled Q1 (logistics), Q2 (conceptual), and Q3 (debugging), first with no examples and then with three.

```bash
uv run few_shot_codes.py
```

**Task 2:** How many of the five did each version get right? Why would names like LOGISTICS need no examples at all, while the codes need them?

---

## Part 3: The Pink Elephant (10 minutes)

A ban has to name the thing it forbids, and naming it makes the model *more* likely to say it. `pink_elephant.py` asks two models for the largest land animal without saying "elephant", then asks `gemma4` to describe the ocean without saying "water".

```bash
uv run pink_elephant.py
```

**Task 3 (the chapter's Exercise 4):** Open `my_bans.py`. Replace the two example traps with your own, each forbidding a word strongly tied to its topic, and put that word on the line after each prompt so the script can check for it. Then replace the third entry with a *positive* rewrite of one of them that gives the model somewhere to go (the chapter's example: *"call it the gentle giant"* instead of *"do not say elephant"*).

```bash
uv run my_bans.py
```

The script marks each reply LEAKED or Held. Did the positive version do better?

---

## Part 4: The Reasoning Ladder (10 minutes)

`reasoning.py` runs three of the chapter's demos:
1. **Misguided attention:** the wolf-goat-cabbage puzzle, except only the goat needs to cross.
2. **Chain of thought:** an age puzzle (the answer is 67), asked cold and then with "Let's think step by step", to two models.
3. **Step-back:** a half-life question, asked cold and then after naming the principle first.

```bash
uv run reasoning.py
```

**Task 4:** Did the farmer's answer notice that *only the goat* needs to cross? For the age puzzle, did "step by step" rescue either model, or just help it reach a different wrong answer? Did naming the principle fix the half-life question?

---

## Part 5: Lab Questions (7 minutes)

Open `lab2_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **The control panel (Task 1):** What did your tallies look like at each temperature, for both prompts? In your own words, how is what temperature does different from what top-k and top-p do?
2. **Examples (Task 2):** How did the coded labels do with zero examples versus three? When are few-shot examples worth adding to a prompt, and when are they just wasted tokens?
3. **Pink elephants (Task 3):** What were your two traps, did they leak, and did the positive rewrite work better?
4. **Reasoning (Task 4):** Pick one of the three reasoning demos and describe what happened. When would you reach for chain-of-thought or step-back, and when wouldn't you bother?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab2_results.txt` to the **Week 2 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

Great, you're done with the second lab!

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week02` folder.

- **Rewrite a real prompt (the chapter's Exercise 3).** In `optional/my_prompt_rewrite.py`, paste a prompt you recently gave a chatbot into `original`, and write a version with all four parts of a prompt's anatomy (instruction, context, examples, output format) into `rewritten`. Which parts were missing from your original?
  ```bash
  uv run optional/my_prompt_rewrite.py
  ```
- **Set your own misguided-attention trap (Exercise 1).** In `optional/my_puzzle.py`, write a problem that looks like a famous puzzle but has a trivial answer. Does the model overcomplicate it? Does "Let's think step by step" rescue it, or help it spiral?
  ```bash
  uv run optional/my_puzzle.py
  ```
- **Find your own step-back question (Exercise 2).** In `optional/my_step_back.py`, put a question where your own first instinct tends to be wrong. Does naming the principle first change the answer?
  ```bash
  uv run optional/my_step_back.py
  ```
