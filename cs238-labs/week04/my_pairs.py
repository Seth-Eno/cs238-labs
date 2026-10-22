"""Week 4 · Task 1: meaning versus word overlap, your pairs (the chapter's Exercise 1).

Write one pair of sentences that share almost no words but mean the same
thing, and one pair that shares nearly every word but means something
different. Predict both scores, then run:
    uv run my_pairs.py
"""
import re
from genai import similarity

def word_overlap(a, b):
    """The old way: the share of distinct words the two sentences have in common."""
    words_a = set(re.findall(r"[a-z']+", a.lower()))
    words_b = set(re.findall(r"[a-z']+", b.lower()))
    return len(words_a & words_b) / len(words_a | words_b)

same_meaning = ("The meeting got pushed to next week",              # ← yours
                "We postponed our appointment by seven days")       # ← yours
same_words = ("The dog chased the mail carrier",                    # ← yours
              "The mail carrier chased the dog")                    # ← yours

print("Two ways to score how alike two sentences are, both from 0 to 1:")
print("  Word overlap:  the share of words they have in common.")
print("  Embedding:     cosine similarity of their meanings.\n")
for label, (a, b) in [("Same meaning, different words", same_meaning),
                      ("Same words, different meaning", same_words)]:
    print(f"── {label}")
    print(f'   "{a}"')
    print(f'   "{b}"')
    print(f"   word overlap: {word_overlap(a, b):.2f}    embedding: {similarity(a, b):.3f}\n")
