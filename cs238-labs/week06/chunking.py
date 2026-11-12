"""Week 6 · Part 3.1: fixed-size versus semantic chunking.

Run from this folder:  uv run chunking.py
"""
import re
from genai import chunk, similarity
from genai.rag import LONG_DOC

# 1. Fixed-size chunks: cut every 20 words, wherever that lands
print("1. FIXED-SIZE CHUNKS: the text cut every 20 words, no matter where")
print("   sentences end. The start of each chunk:\n")
for i, piece in enumerate(chunk(LONG_DOC, size=20, overlap=0), start=1):
    print(f"   Chunk {i}: {piece[:60]}...")

# 2. Semantic chunking: split where the topic shifts
sentences = [s.strip() for s in re.split(r"(?<=[.?]) ", LONG_DOC) if s.strip()]
scores = [similarity(sentences[i], sentences[i + 1])
          for i in range(len(sentences) - 1)]
weakest = scores.index(min(scores))
print("\n2. SPLITTING WHERE THE TOPIC SHIFTS: how similar each sentence is to")
print("   the next one (closer to 1 = same topic). The lowest score is the")
print("   best place to split.\n")
for i, score in enumerate(scores):
    mark = "   ◀ SPLIT HERE (lowest)" if i == weakest else ""
    print(f"   {score:.3f}  after: {sentences[i][:45]}...{mark}")
