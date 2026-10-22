"""Week 3 · Part 2.2: meaning versus word overlap (the chapter's Exercise 1).

Predict each score before you run it:  uv run meaning_vs_words.py
"""
import re
from genai import similarity

def word_overlap(a, b):
    """The old way: the share of distinct words the two sentences have in common."""
    words_a = set(re.findall(r"[a-z']+", a.lower()))
    words_b = set(re.findall(r"[a-z']+", b.lower()))
    return len(words_a & words_b) / len(words_a | words_b)

pairs = [
    ("The cat sat on the mat", "A feline rested on the rug"),
    ("She aced the exam", "He passed the test with flying colors"),
    ("I love this movie", "I don't love this movie"),
]

print("Two ways to score how alike two sentences are, both from 0 to 1:")
print("  Word overlap:  the share of words they have in common.")
print("  Embedding:     cosine similarity of their meanings (closer to 1 =")
print("                 closer in meaning).\n")
for a, b in pairs:
    print(f'   "{a}"')
    print(f'   "{b}"')
    print(f"   word overlap: {word_overlap(a, b):.2f}    embedding: {similarity(a, b):.3f}\n")
