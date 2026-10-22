"""Week 4 · Part 2.1: word arithmetic, and where it breaks (the chapter's Exercise 2).

Run from this folder:  uv run analogies.py
"""
from genai import similarity, word_analogy

def check(a, b, c, candidates, hoping_for):
    got, score = word_analogy(a, b, c, candidates)
    verdict = "works" if got == hoping_for else "BREAKS"
    print(f"{a} − {b} + {c} = ?   (we're hoping for '{hoping_for}')")
    print(f"   The choices:         {', '.join(candidates)}")
    print(f"   The closest choice:  {got}  (similarity {score:.2f}), so it {verdict}\n")

print("Word arithmetic with embeddings: start at one word, subtract another,")
print("add a third, and see which choice lands closest.\n")
check("king", "man", "woman", ["queen", "prince", "princess", "duke"], "queen")
check("better", "good", "bad", ["worse", "worst", "terrible"], "worse")
check("bigger", "big", "small", ["smaller", "smallest", "tiny"], "smaller")
check("happy", "sad", "rich", ["poor", "wealthy", "money", "broke"], "poor")

print("Are opposites far apart? Cosine similarity can run from -1 (pointing")
print("opposite ways) to 1 (identical). Here's where opposites actually land:\n")
for a, b in [("happy", "sad"), ("rich", "poor"), ("hot", "cold"),
             ("good", "bad"), ("true", "false")]:
    print(f"   {a + ' / ' + b:18} {similarity(a, b):+.2f}")
print("\nAnd some pairs for comparison:\n")
for a, b in [("happy", "economics"), ("happy", "stapler"),
             ("cat", "car"), ("happy", "happy")]:
    print(f"   {a + ' / ' + b:18} {similarity(a, b):+.2f}")
