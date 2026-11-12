# Week 6 Lab: Retrieval-Augmented Generation

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 6 (Augmentation) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Explain the knowledge problem: why a model can't know about documents it was never trained on
- Build a small retrieval-augmented generation (RAG) system that answers from your documents and cites them
- Explain how chunk size changes what gets retrieved
- Tell when meaning-based (dense) retrieval wins and when plain keyword matching wins
- Test a grounded system on a question whose answer isn't in its documents

---

## Before You Start

- Completed the Week 4 lab (embeddings and cosine similarity)
- Read Chapter 6

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week06
```

Run every script below from inside this folder with `uv run`.

**Working locally?** This lab uses `gemma4` and `nomic-embed-text`.

---

## Part 1: The Knowledge Problem (5 minutes)

The book you're reading isn't in any model's training data. `no_rag.py` asks the model what the book's Augmentation chapter covers.

```bash
uv run no_rag.py
```

**Task 1:** Does the model admit it doesn't know, or does it guess? If it guesses, what did it think "augmentation" meant?

---

## Part 2: Your First RAG System (10 minutes)

Let's give the model the reading it missed. `my_prompting_sections.txt` in this folder already holds the text of two sections of Chapter 2 (Prompting): **The Control Panel: Model Parameters** and **Zero-Shot and Few-Shot Prompting**. Open it and skim it so you know what the system will be searching.

`book_rag.py` splits that text into chunks of about 80 words, loads them into a `DocumentStore` (which embeds each one), and answers "What does temperature do to the model's output?" from whatever it retrieves:

```bash
uv run book_rag.py
```

The answer should cite numbered sources `[1]`, `[2]`… and print the chunks they point to.

**Task 2:** Open `my_book_questions.py` and put three questions on the marked lines: two that your two sections answer, and one about something they never cover (the example is "What is a vector database?").

```bash
uv run my_book_questions.py
```

Does the system cite the right chunks? What does it do on the question it can't answer? Look at the three sources it retrieved for that one: are they about vector databases at all?

---

## Part 3: Chunking (8 minutes)

Real documents are too long to embed whole, so we slice them into *chunks*. Too small and a chunk loses its context; too large and its embedding gets diluted.

`chunking.py` chunks one short stitched-together document two ways: fixed-size chunks every 20 words, and a semantic chunker that splits where neighboring sentences stop resembling each other.

```bash
uv run chunking.py
```

The fixed-size chunks slice straight through sentences; the semantic chunker finds the seam where the document changes topic.

`chunk_sizes.py` is the chapter's Exercise 1: it chunks the same document at 10 words and at 80 words, and prints the best-matching chunk at each size for "How does a vision model turn an image into tokens?"

```bash
uv run chunk_sizes.py
```

**Task 3:** Which chunk size gave a more useful best match for the question? What went wrong at the other size?

---

## Part 4: Dense Versus Keyword Retrieval (10 minutes)

*Dense* retrieval compares meaning with embeddings. *Sparse* retrieval, like BM25, compares exact words. `dense_vs_sparse.py` searches six help-desk notes both ways, using a tiny keyword scorer from the chapter, with four kinds of query:
1. a paraphrase that shares one misleading word with the wrong note ("why is my laptop so noisy"),
2. a paraphrase that shares no words with any note ("websites show old versions"),
3. something none of the notes cover ("my printer is jammed"), and
4. an exact error code ("E1045").

```bash
uv run dense_vs_sparse.py
```

**Task 4 (the chapter's Exercise 2):** Which method found the right note for each paraphrase? What did each method do on the printer question, which no note answers? Keyword search *fails loudly*: when nothing matches, it says so. Dense search *fails silently*: it always returns its closest guess, even when that guess is wrong. On a set this small, both find the exact error code. The chapter shows keyword search pulling ahead on exact terms in a large collection, where many passages are on similar topics.

Then open `my_dense_vs_sparse.py` and write two queries of your own on the marked lines: one that should favor dense search, and one about something none of the six notes cover.

```bash
uv run my_dense_vs_sparse.py
```

Did each method behave the way you expected?

---

## Part 5: Grounded Answers, and Knowing When to Say "I Don't Know" (10 minutes)

This is the chapter's Exercise 5, "ask my syllabus." `my_syllabus.txt` in this folder already holds the text of the course website. If you'd rather ask about a document you live by (a lab manual, a rulebook, a job posting), paste its text into `my_syllabus.txt` in place of the website.

`my_syllabus.py` chunks your document and answers each question using *only* the passages it retrieves, with citations, and says it doesn't know when the answer isn't there.

**Task 5:** Replace the questions in `my_syllabus.py` with five you actually care about, including one whose answer you *know* isn't in the document. Then run it:

```bash
uv run my_syllabus.py
```

Count the hits and misses. For each answer, look at the source it cites: does that passage really say what the answer claims? What did the system do on the unanswerable one?

---

## Part 6: Lab Questions (5 minutes)

Open `lab6_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **The knowledge problem (Tasks 1 and 2):** What did the model say about the book without retrieval, and how did the answers change once it could retrieve? What did it do on the question your two sections don't cover?
2. **Chunking (Task 3):** Which chunk size worked better for the question, and what went wrong with the other?
3. **Dense versus keyword (Task 4):** Give one query where dense search found the right note and keyword search didn't. What did each method do on a question no note answers, and which way of failing would you rather have in a real system? Why does a real system want both (hybrid search)?
4. **Grounding (Task 5):** How many of your five syllabus questions did it get right? Did any answer cite a source that didn't actually support it? Grounding *reduces* hallucination; based on what you saw, why doesn't it eliminate it?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab6_results.txt` to the **Week 6 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week06` folder.

- **Chain-of-verification.** `optional/cove.py` runs the chapter's two demos. On Portugal, checking each claim on its own fixes the draft on runs where the draft slips in a wrong country (run it a few times; some drafts are already right). On Brazil, it throws away correct answers. Why is a self-check only as good as the checker?
  ```bash
  uv run optional/cove.py
  ```
- **Precision and recall by hand (Exercise 4).** In `optional/my_precision_recall.py`, write six short documents, mark which ones are relevant to your query, and compare retrieving the top 3 with the top 5. Watch one number rise while the other falls.
  ```bash
  uv run optional/my_precision_recall.py
  ```
- **Search a whole chapter.** `optional/my_chapter.txt` holds the whole Augmentation chapter. Put your questions in `optional/my_chapter_search.py` and run it (or paste in a different chapter you've read). How does retrieval hold up as the store grows?
  ```bash
  uv run optional/my_chapter_search.py
  ```
