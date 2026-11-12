"""Week 6 · Part 3.2: too small or too large? (the chapter's Exercise 1)

Chunk the same document at two sizes and find the best match for one question.
Run from this folder:  uv run chunk_sizes.py
"""
from genai import chunk, similarity
from genai.rag import LONG_DOC

question = "How does a vision model turn an image into tokens?"
print(f"Question: {question}")
print("Cutting the same text into small chunks, then big ones, and finding")
print("the chunk closest in meaning to the question.")
for size in [10, 80]:
    chunks = chunk(LONG_DOC, size=size, overlap=0)
    best = max(chunks, key=lambda c: similarity(question, c))
    print(f"\n── Chunks of {size} words ({len(chunks)} chunks). The best match:")
    print(f"   {best}")
