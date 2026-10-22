# Week 4 Lab: Semantics

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 4 (Semantics) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Turn text into an embedding and measure how close two meanings are with cosine similarity
- Explain why counting shared words misses meaning, and what the *distributional hypothesis* gets right
- Show where word arithmetic works, where it breaks, and why opposites sit close together
- Explain why reading a whole sentence at once beats averaging its words
- Build a small semantic search, then find a query that fools it

---

## Before You Start

- Completed the Week 3 lab
- Read Chapter 4

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week04
```

Run every script below from inside this folder with `uv run`. Close chart windows to let a script continue.

**Working locally?** This lab uses `nomic-embed-text`, a small model (0.3 GB) that turns text into embeddings. The optional "testing AI with AI" exercise also uses `gemma4`.

---

# Part 1: Words as Locations (14 minutes)

An *embedding* turns text into a long list of numbers, a point in space, so that things with similar meanings land near each other. *Cosine similarity* measures how closely two of those points line up: `1` for the same direction, `0` for nothing in common, and `-1` for opposite directions.

## 1.1 Words as Locations (4 minutes)

`semantics.py` prints the start of the embedding for "cat" and how long it is, then compares "cat" with "kitten", "dog", and "car".

```bash
uv run semantics.py
```

The ranking should match common sense: kitten closest, car furthest. A score like `0.56` for "car" doesn't mean cat and car are half alike; it just means car is the least catlike of the three.

## 1.2 Why Word-Counting Fails (6 minutes)

The old way to compare sentences is to count the words they share. `meaning_vs_words.py` scores three pairs both ways: by word overlap and by embedding. The first two pairs share almost no words but mean the same thing; the third shares nearly every word but flips the meaning ("I love this movie" / "I don't love this movie").

```bash
uv run meaning_vs_words.py
```

**Task 1 (the chapter's Exercise 1):** Open `my_pairs.py` and write two pairs of your own on the marked lines: one that shares almost no words but means the same thing, and one that shares nearly every word but means something different. **Before running it**, predict both scores for each pair.

```bash
uv run my_pairs.py
```

Does the embedding rate meaning over surface wording? Where did your "same words, different meaning" pair land?

## 1.3 A Map of Meaning (4 minutes)

Each embedding is 768 numbers long, so we can't plot it directly. `meaning_map.py` squashes 24 words from four groups (animals, vehicles, fruits, and code) down to two dimensions with a technique called t-SNE, which keeps close words close. The exact positions mean nothing, but the clusters do.

```bash
uv run meaning_map.py
```

Find "java" on the map. It's a programming language, but it's also slang for coffee and the name of an island. Which group does it sit nearest, and does it stray?

---

# Part 2: Word Arithmetic, and Where It Breaks (12 minutes)

## 2.1 Word Arithmetic (6 minutes)

The famous trick: take "king", subtract "man", add "woman", and you land near "queen". `analogies.py` tries it, plus two grammar versions (good → better, big → bigger), and then asks for an opposite: happy − sad + rich, hoping for "poor". Then it lists where real opposites sit on the cosine scale.

```bash
uv run analogies.py
```

**Task 2 (the chapter's Exercise 2):** Which analogies worked, and which broke? What did the opposite of "rich" come back as? Look at the list of opposites: where do pairs like "rich / poor" land on the scale from `-1` to `1`? Why would words that mean opposite things sit so close together? (Hint: "I felt so *happy* after the call" / "I felt so *sad* after the call." You can know a word by the company it keeps.)

## 2.2 The Borrowed Arrow (6 minutes)

An analogy works by borrowing an *arrow*: the step from "man" to "woman" has to point the same way as the step from "king" to "queen". `borrowed_arrow.py` measures those steps for gender, for comparisons (big → bigger), and for opposites, then draws them.

```bash
uv run borrowed_arrow.py
```

**Task 3 (the chapter's Exercise 3):** Which relationships share an arrow, and which don't? Why can "gender" be one direction in the space when "opposite" can't? (Think about what the opposite of "happy" changes, compared with the opposite of "rich".)

---

# Part 3: From Words to Sentences (8 minutes)

We usually need to compare whole sentences, not single words. The simple way is to embed each word and average them. The modern way is a *transformer* that reads the whole sentence at once, letting every word shape every other word's meaning. That's how `nomic-embed-text` works. `sentences.py` compares the two on word order ("The dog bit the cat" / "The cat bit the dog"), then on how clearly each one separates a paraphrase from an off-topic sentence.

```bash
uv run sentences.py
```

**Task 4 (the chapter's Exercise 4):** Did either method tell "the dog bit the cat" from "the cat bit the dog"? Which method had the bigger *spread* between the related and unrelated sentence? What can the whole-sentence model use that the average throws away?

---

# Part 4: A Semantic Search You Can Fool (10 minutes)

Keyword search matches exact words. *Semantic search* matches meaning: it embeds your query and every document, then returns the documents whose embeddings sit closest. `search.py` searches six sentences for "artificial intelligence" and "dinner".

```bash
uv run search.py
```

None of the AI sentences contains the words "artificial" or "intelligence", and the search finds them anyway.

**Task 5 (the chapter's Exercise 5):** Open `my_search.py`. Replace the corpus with six to eight sentences of your own on two or three topics. Set `finds_it` to a query that shares no words with the sentence you want, and `fools_it` to a query designed to *mislead* the search (searching for one car brand might surface a rival, for example).

```bash
uv run my_search.py
```

Did the first query still find your sentence? What did the second one return? Does the search ever warn you that it missed?

---

## Part 5: Lab Questions (6 minutes)

Open `lab4_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **Meaning versus words (Task 1):** What were your two pairs, and how did the word-overlap and embedding scores compare? Which of your predictions was furthest off?
2. **Opposites (Tasks 2 and 3):** In a sentence or two, explain why "rich" and "poor" sit close together in embedding space, and why "opposite" isn't a single direction the way "gender" is.
3. **Sentences (Task 4):** What does reading a whole sentence at once give an embedding that averaging its words doesn't? Did it fully solve word order?
4. **Search (Task 5):** What query fooled your search, and what did it return? Where would you add a plain keyword check to catch what the embeddings blur together?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Copy/paste `lab4_results.txt` to the **Week 4 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week04` folder.

- **Cluster a corpus (the chapter's Exercise 6).** In `optional/my_clusters.py`, put nine or ten sentences from three topics you know well, plus one sentence that straddles two of them (a recipe written like a chemistry procedure, say). The k-means algorithm sorts them into three groups by meaning alone. Do the groups match your topics, and which group claims the straddler?
  ```bash
  uv run optional/my_clusters.py
  ```
- **Testing AI with AI (the chapter's Exercise 7).** A model never words an answer the same way twice, so an automated test can't check for an exact match. `optional/my_threshold.py` asks `gemma4` one question twice and a different question once, then compares the answers by meaning against a `THRESHOLD` you choose. What threshold separates "same answer" from "different answer"? What breaks if you set it too low, or too high?
  ```bash
  uv run optional/my_threshold.py
  ```
