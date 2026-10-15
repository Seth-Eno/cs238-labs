# Week 1 Lab: The Prediction Machine

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 1 (Introduction) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Run a language model from Python with the book's `genai` library
- Tell a *discriminative* task (pick from existing options) from a *generative* one (make something new)
- Look inside the prediction machine: read a model's probabilities for the next token, and tell a *peaked* forecast from a *spread* one

---

## Before You Start

- No prior coding or GenAI experience is required.
- Read Chapter 1. This lab reruns its experiments, so you'll recognize every one.
- Follow **Getting Started** in the [course labs README](../README.md) to set up your `cs238` folder, download these labs, and point `genai` at the class server. If you can, do it before class.

Then go into this week's folder. From your `cs238` folder:

```bash
cd cs238-labs/week01
```

Run every script below from inside this folder with `uv run`. When a script draws a chart, it opens in its own window and is also saved as a `.png` here. **Close the chart window to let the script continue.**

**Working locally?** (see *Working Off Campus* in the [labs README](../README.md)) This lab uses `gemma4` and `llama3.2`.

---

## Part 0: Setup Check (6 minutes)

`check_setup.py` is the chapter's own setup check. It prints which server you're using, then asks the model what "generative" means.

```bash
uv run check_setup.py
```

**Checkpoint:** You should see `Talking to: http://ollama2.cs.wallawalla.edu:11434` and a short definition. If you get a connection error, check that you're on the campus network (or VPN) and that you finished step 5 of Getting Started. Working locally? Make sure the Ollama app is running.

**Task 0 (the chapter's Warm-Up):** Run it two more times. The wording drifts a little on each run. Chapter 2 explains exactly why; for now, just notice it.

---

## Part 1: The Jigsaw and the LEGO (7 minutes)

The chapter's picture: *discriminative* AI solves a jigsaw puzzle, placing a piece where it belongs among options that already exist, while *generative* AI plays with LEGO bricks and builds something new. A modern LLM can do both.

`jigsaw_and_lego.py` classifies the chapter's movie review as POSITIVE, NEGATIVE, or MIXED (discriminative), then writes a brand-new review (generative):

```bash
uv run jigsaw_and_lego.py
```

**Task 1:** Open `my_review.py` and replace the review on the marked line with one you write yourself that should be hard to label, like a sarcastic one. Run it:

```bash
uv run my_review.py
```

Does the model get it right? Keep your review and its label for the lab questions.

---

## Part 2: Inside the Prediction Machine (14 minutes)

Before it writes each token, a language model scores every token it knows and turns those scores into probabilities. `next_token_distribution` asks Ollama for the top few, and `plot_next_token` draws them as the chapter's bar charts.

### 2.1 One Obvious Answer, One Long Shot

`predict.py` does three things with "The capital of the USA is":
1. charts the model's forecast for the first word of its answer;
2. writes "New" into the start of the model's *own* answer and charts what it predicts next;
3. sends "The capital of the USA is New" as a message of our own instead, and prints the reply.

```bash
uv run predict.py
```

Compare with the chapter. The first chart should be steeply *peaked* on "Washington." Once "New" is in the model's own reply, it rushes on to "York." But send the same words as a *message* and it corrects you instead.

### 2.2 A Door That Opens Onto Anything

`door.py` predicts the chapter's open-ended story prompt, "She opened the door and saw a", two words in a row: first the forecast for the next word, then, with the favorite locked in, the forecast for the word after it.

```bash
uv run door.py
```

The first step should be *spread* across many reasonable words, and the second should snap shut once the first word is locked in.

### 2.3 Your Turn: Predict, Then Peek

This is the chapter's Exercise 1. Think of two unfinished sentences of your own:
- one where you expect the model to be **very sure** of the next word, and
- one where you expect **almost anything** could come next.

**Before running anything**, write down which one you expect to be peaked and what you think its top candidates will be. Then open `my_prompts.py`, put your sentences on the two marked lines, and run it:

```bash
uv run my_prompts.py
```

It saves one chart per sentence, `sure.png` and `anything.png`.

A chart may show the first *piece* of a word rather than the whole word. For "The capital of Argentina is", the top candidate is just `B`, the start of "Buenos Aires", because the model writes uncommon words in chunks. Chapter 3 (Tokens) explains why.

**Task 2:** Were your predictions right? Keep your two prompts, your predictions, and the actual top candidates for the lab questions.

---

## Part 3: Lab Questions (5 minutes)

Open `lab1_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **Warm-up (Task 0) and your review (Task 1):** How did the answer to "What does generative mean?" change across your three runs? What was your hard-to-label review, and did the model label it correctly?
2. **Peaked vs. spread (Task 2):** What were your two prompts? What did you predict, what were the actual top candidates, and were you right?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload (or copy-paste) `lab1_results.txt` to the **Week 1 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

Congrats, you're done with the first lab! Yippee! 🎉

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week01` folder.

- **Bigger isn't always better (the chapter's Warm-Up 2).** `optional/smaller_model.py` asks `gemma4` and the much smaller `llama3.2:1b` the setup question. What do you gain and lose as the model shrinks?
  ```bash
  uv run optional/smaller_model.py
  ```
- **Find your own long shot.** In `optional/my_long_shot.py`, put one of your Task 2 prompts on the marked line and run it to see the candidates. Then set `long_shot` to a word the model gave less than 1% and run it again. Like "New" leading to "York", does the model build confidently on a word it barely believed in?
  ```bash
  uv run optional/my_long_shot.py
  ```
- **Paying attention (the chapter's Exercise 2).** To predict the next word, a model first has to decide which earlier words matter most. That's *attention*, and the chapter watches it by reading the attention heads of BERT, a small language model. First download BERT (about 420 MB, one time only):
  ```bash
  uv run optional/download_bert.py
  ```
  Then run the chapter's demo, where changing one word ("tired" to "warm") flips which noun "it" points back to:
  ```bash
  uv run optional/attention.py
  ```
  Finally, in `optional/my_attention.py`, write two sentences of your own that differ by one word, where that word changes which noun a pronoun points back to ("The trophy didn't fit in the suitcase because it was too *big*" versus "…too *small*"). Predict the answer first, then run it. Does the single head lean where you expected, and does the 144-head vote agree?
  ```bash
  uv run optional/my_attention.py
  ```
