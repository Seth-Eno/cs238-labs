---
title: Glossary
---

This glossary collects the recurring vocabulary of the book in one place. Each entry is a short working definition, not a full treatment; the chapter where a term first appears develops it properly. Terms set in italics inside a definition have their own entries.

agent
: A language model placed in a loop where it can plan, take actions with *tool use*, observe the results, and decide what to do next, rather than producing a single reply and stopping.

alignment
: The effort to make a model's goals and behavior match what its developers and users intend, including being truthful and refusing harmful requests.

attention
: The mechanism inside a *transformer* that lets the model weigh how relevant every other token in the input is when processing each token.

autoregressive generation
: Producing text one token at a time, where the model predicts each new token from all the tokens generated so far.

bag of words
: A text representation that records which words occur and how often, while discarding word order.

batching
: Processing several requests through a model together so that shared computation is performed once.

benchmark
: A fixed, shared set of test problems used to measure and compare model performance.

byte pair encoding (BPE)
: The algorithm most models use to build their *vocabulary*: starting from single characters, it repeatedly merges the most frequent adjacent pair of symbols found in training text.

chain-of-thought prompting
: Asking a model to write out intermediate reasoning steps before giving its final answer, which improves accuracy on multi-step problems.

chain-of-verification (CoVe)
: A self-checking recipe where the model drafts an answer, writes verification questions about its own claims, answers those questions independently, and then revises the draft.

chunking
: Splitting long documents into smaller passages so that each piece can be embedded and retrieved on its own.

clustering
: Grouping items by similarity, usually measured between their *embeddings*, without any predefined categories.

code generation
: Using a language model to write source code from a natural language description or from surrounding code.

computer use
: An agent capability where the model operates a real user interface by viewing the screen and issuing clicks and keystrokes.

content moderation
: Screening model inputs and outputs for harmful, unsafe, or policy-violating content.

context engineering
: Deciding what information goes into the model's *context window*, in what form and order, and what gets left out.

context window
: The maximum amount of text, measured in *tokens*, that a model can consider at one time. Everything the model knows about your request must fit inside it.

corrective RAG (CRAG)
: A retrieval pipeline that grades its own retrieved documents and falls back to another source, such as web search, when retrieval quality looks poor.

cosine similarity
: A number between -1 and 1 that measures how similar two *embeddings* are by the angle between them. Higher means more similar.

determinism
: The property that the same input always produces the same output. Setting *temperature* to zero makes generation close to deterministic.

differential privacy
: A mathematical privacy guarantee achieved by adding carefully calibrated noise, so that results reveal patterns in the data without exposing any individual record.

diffusion model
: An image generation model trained to remove noise step by step, so that starting from pure noise it can produce a coherent image matching a text prompt.

distributional hypothesis
: The observation that words appearing in similar contexts tend to have similar meanings. It's the foundation of *embeddings*.

document ingestion
: The pipeline that takes raw source files and turns them into clean, chunked, embedded text ready for *retrieval*.

embedding
: A list of numbers representing the meaning of a piece of text, code, or an image, computed so that similar meanings end up near each other.

emergent abilities
: Capabilities that appear in larger models even though they weren't present in smaller models trained the same way.

evaluation
: Measuring a system's quality with defined criteria and consistent test cases, rather than judging by impression.

fairness
: The goal that a model's behavior and errors don't systematically disadvantage particular groups of people.

federated learning
: Training a shared model across many devices or organizations without collecting their raw data in one central place.

few-shot prompting
: Including a handful of worked examples in the prompt so the model infers the pattern it should follow.

fine-tuning
: Continuing a pretrained model's training on a smaller, task-specific dataset to specialize its behavior.

frontier model
: One of the largest and most capable models available at a given time.

function calling
: See *tool use*.

generative AI
: Software that produces new content, such as text, images, code, or audio, from patterns learned during training.

governance
: The policies, processes, and accountability structures an organization uses to manage how AI systems are built and deployed.

greedy decoding
: Always choosing the single most probable next token, instead of *sampling* among candidates.

grounding
: Tying a model's output to specific source material, so that its claims can be traced back to evidence and checked.

guardrails
: Checks placed around a model that block, filter, or rewrite unsafe inputs and outputs.

hallucination
: Output that's fluent and confident but factually wrong or entirely invented.

human-in-the-loop
: A workflow where a person reviews, approves, or corrects model output at defined points, instead of letting the system act fully autonomously.

hybrid retrieval
: Combining keyword search and embedding-based search so that each covers the other's blind spots.

hypothetical document embeddings (HyDE)
: A retrieval technique where the model first writes an imagined answer to the query, and the search uses the embedding of that imagined answer, since it usually lands closer to real answers than the bare question does.

in-context learning
: A model's ability to pick up a task from instructions and examples in the prompt alone, with no change to its weights.

inference
: Running a trained model to produce output, as opposed to training it.

inference-time scaling
: Improving answer quality by spending more computation when the model runs, for example through longer reasoning or multiple candidate answers, rather than by training a bigger model.

jailbreaking
: Crafting prompts designed to make a model ignore its safety rules.

knowledge cutoff
: The date after which events are absent from a model's training data, and therefore absent from its knowledge.

KV cache
: The store of key and value vectors a model keeps for every *token* it has processed, letting it extend a prompt or conversation by reading only the new tokens instead of re-reading everything from scratch.

large language model (LLM)
: A neural network with billions of *parameters*, trained on very large amounts of text to predict the next *token*. That single skill turns out to be enough to draft, summarize, translate, answer questions, and write code.

latency
: How long a request takes from sending it to receiving the response.

least privilege
: The security principle that a system should have only the minimum access it needs. Applied to agents, it means limiting which tools and data they can touch.

LLM-as-judge
: Using a capable model to grade or compare the outputs of another model.

membership inference
: An attack that tries to determine whether a specific record was part of a model's training data.

memorization
: A model reproducing specific content from its training data rather than generalizing from it.

memory stream
: An agent memory design that stores every observation with a timestamp and an importance score, and retrieves memories by combining recency, importance, and relevance.

model routing
: Sending each request to the cheapest model that can handle it, and reserving large models for the hard cases.

multimodal model
: A model that works with more than one kind of data, such as text together with images or audio.

neural network
: A function built from many simple connected units whose connection strengths are adjusted during training. It's the structure underlying modern AI models.

next-token prediction
: The training objective of language models: given the text so far, predict which *token* comes next.

observability
: Being able to see what an AI system did and why, through logs, traces, and metrics.

Ollama
: The free tool this book uses to download and run *open weights* models on your own computer.

one-shot prompting
: Prompting with exactly one worked example.

open weights
: A model whose trained *parameters* are published, so that anyone can download and run it locally.

optical character recognition (OCR)
: Extracting machine-readable text from images.

pairwise judging
: Evaluating by showing a judge two candidate answers and asking which one is better, which is more reliable than scoring answers in isolation.

parameters
: The numbers inside a *neural network* that training adjusts. Model sizes are quoted by parameter count.

personalization
: Adapting a system's behavior to an individual user's history, preferences, and skill level.

personally identifiable information (PII)
: Data that identifies a specific person, such as names, addresses, or account numbers.

pink elephant problem
: The difficulty models have with negative instructions: naming the forbidden thing in the prompt makes the model more likely to produce it.

planner-executor pattern
: An agent design where a strong model writes the plan and a cheaper model carries out the steps.

position bias
: A judge model's preference for an answer based on where it appears in the prompt, typically favoring whichever answer it reads first.

precision and recall
: Two measures of *retrieval* quality. Precision asks how much of what you retrieved was relevant; recall asks how much of what was relevant you retrieved.

pretraining
: The initial, large-scale training of a model on broad data, before any specialization.

probability distribution
: The model's ranked list of every possible next *token*, with the likelihood it assigns to each. *Sampling* picks from this list.

program-aided language models (PAL)
: Having the model write a short program that computes the answer, instead of doing the arithmetic in prose.

prompt
: Everything you send to the model: the instructions, the question, and any context or examples.

prompt compression
: Shortening what goes into the *context window* while keeping its meaning, to save time and memory.

prompt injection
: An attack where instructions hidden inside data the model processes, such as a web page or a document, hijack the model's behavior.

quantization
: Storing a model's *parameters* at lower numeric precision so the model uses less memory and runs faster, at a small cost in quality.

query rewriting and expansion
: Reformulating a search query, or generating several variants of it, to improve *retrieval*.

ReAct
: An agent loop format where the model alternates between writing a reasoning step and taking an action with a tool.

red teaming
: Deliberately attacking your own system to find its failures before real adversaries do.

reinforcement learning from human feedback (RLHF)
: A training stage where human preferences between candidate outputs teach the model which kinds of responses people favor.

Reflexion
: An agent technique where the model writes a short reflection on why an attempt failed and carries that reflection into its next attempt.

reranking
: A second, more careful scoring pass over retrieved candidates to put the best ones first.

retrieval
: Finding the most relevant stored passages for a query, usually by *embedding* similarity.

retrieval-augmented generation (RAG)
: Looking up relevant documents first and including them in the prompt, so the model answers from evidence instead of from memory alone.

sampling
: Choosing the next *token* according to the model's probabilities rather than always taking the single most likely one. Sampling is why output varies between runs.

sandboxing
: Running untrusted code or actions in an isolated environment where they can't cause harm.

scaling laws
: The empirical finding that model performance improves in a predictable way as model size, data, and computation grow.

self-consistency
: Sampling several independent answers to the same question and taking a majority vote.

Self-Refine
: Asking the model to critique its own draft and then revise the draft using that critique.

semantic search
: Search by meaning rather than by keywords, using *embeddings*, so that results can match a query they share no words with.

skill library
: An agent memory of verified, reusable code, so that a problem solved once stays solved.

special tokens
: Reserved *tokens* that carry structural meaning, such as marking where a message begins and ends, rather than ordinary text.

speech recognition
: Converting spoken audio into written text.

step-back prompting
: Asking the model to first state the general principle behind a question, and then answer using that principle.

structured output
: Constraining a model to reply in a machine-readable format such as JSON.

subword
: A *token* that's a fragment of a word. Rare words are spelled out of several subwords.

sycophancy
: A model's tendency to agree with the asker's stated beliefs and tell them what they want to hear, even when it knows better.

system prompt
: Standing instructions, set by the developer and usually invisible to the end user, that frame every reply the model gives.

temperature
: The *sampling* setting that controls how adventurous generation is. Low values stick to the most likely tokens; higher values take more risks.

thinking budget
: A reserved token allowance for a *thinking model*'s internal reasoning, separate from the tokens of its visible answer.

thinking model
: A model trained to generate internal reasoning before producing its visible answer.

throughput
: How much output a system produces per unit of time, often quoted in *tokens* per second.

token
: The unit a model reads and writes: a word, a piece of a word, a punctuation mark, or a chunk of code.

tokenization
: Converting text into *tokens* before the model sees it, and converting generated tokens back into text afterward.

tool use
: Letting a model call functions a developer defines, such as a calculator or a search engine, so it can act and fetch facts instead of only generating text.

top-k sampling
: Restricting *sampling* to the k most probable next tokens.

top-p sampling
: Restricting *sampling* to the smallest set of most probable next tokens whose probabilities add up to p.

training data
: The text and other media a model learned from.

transformer
: The *neural network* architecture behind modern language models, built around *attention*.

universal jailbreak
: A single *jailbreaking* prompt that works across many different requests and often transfers to models it was never tuned against, as opposed to one hand-crafted for a single target.

vector arithmetic
: Adding and subtracting *embeddings* to move through meaning, as in the classic example where king minus man plus woman lands near queen.

vector database
: A storage system specialized for holding *embeddings* and finding the nearest ones to a query quickly.

verbosity bias
: A judge model's soft preference for the longer answer, even when the extra words add nothing.

vision-language model
: A model that accepts images alongside text and can describe, read, and reason about them.

vocabulary
: The fixed set of *tokens* a model knows. Every input must be expressed using these and nothing else.

watermarking
: Embedding a hidden statistical signature in generated content so that it can later be identified as machine-made.

Word2Vec
: The 2013 method that first made word *embeddings* widely practical, by training small networks to predict words from their neighbors.

zero-shot prompting
: Asking the model to perform a task from instructions alone, with no examples.
