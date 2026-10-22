"""Week 4 · Part 3: from words to sentences (the chapter's Exercise 4).

Run from this folder:  uv run sentences.py
"""
from genai import similarity
from genai.embed import averaged_similarity

print("Two ways to embed a whole sentence:")
print("  Averaged words:  embed each word on its own, then average them.")
print("  Whole sentence:  a transformer reads the entire sentence at once.\n")

# 1. Word order: same words, very different events
a, b = "The dog bit the cat", "The cat bit the dog"
print("═══ 1. Same words, different order")
print(f'   "{a}"  vs  "{b}"')
print(f"   Averaged words: {averaged_similarity(a, b):.3f}")
print(f"   Whole sentence: {similarity(a, b):.3f}\n")

# 2. The spread: how far apart related and unrelated sentences land
anchor = "The cat sat on the mat"
related = "A feline rested on the rug"
unrelated = "Python is a programming language"
print("═══ 2. Telling related from unrelated")
print(f'   Anchor:     "{anchor}"')
print(f'   Related:    "{related}"')
print(f'   Unrelated:  "{unrelated}"')
print("   The 'spread' is the related score minus the unrelated score. A bigger")
print("   spread means the method tells them apart more clearly.\n")
for name, score in [("Averaged words", averaged_similarity),
                    ("Whole sentence", similarity)]:
    r, u = score(anchor, related), score(anchor, unrelated)
    print(f"   {name}:  related {r:.3f}, unrelated {u:.3f}, spread {r - u:.3f}")
