"""Week 4 · Part 1.1: words as locations.

Run from this folder:  uv run semantics.py
"""
from genai import embed, similarity

v = embed("cat")
print(f"The embedding of 'cat' is a list of {len(v)} numbers. The first three:")
print(f"   {v[0]:+.2f}, {v[1]:+.2f}, {v[2]:+.2f}, ...\n")

print("How similar 'cat' is to other words. The score is cosine similarity:")
print("closer to 1 means closer in meaning.\n")
for word in ["kitten", "dog", "car"]:
    print(f"   cat and {word:7} {similarity('cat', word):.3f}")
