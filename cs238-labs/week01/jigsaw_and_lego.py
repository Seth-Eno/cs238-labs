"""Week 1 · Part 1: the jigsaw and the LEGO.

Discriminative AI places a piece among options that already exist; generative
AI builds something new. A modern LLM can do both.

Run from this folder:  uv run jigsaw_and_lego.py
"""
from genai import ask

review = ("I felt like part one was more fast-paced and exciting, "
          "but the soundtrack in part two was more emotionally "
          "satisfying.")

print("The review:")
print(f"  {review}\n")

# Discriminative: choose one of three labels that already exist
label = ask("Classify as POSITIVE, NEGATIVE, or MIXED. "
            f"One word.\n{review}")
print("1. DISCRIMINATIVE (the jigsaw): pick one of the labels POSITIVE,")
print("   NEGATIVE, or MIXED for the review above.")
print(f"   The model's label: {label.strip()}\n")

# Generative: make something that didn't exist before
new_review = ask("Write a one-sentence MIXED review of a movie sequel.")
print("2. GENERATIVE (the LEGO): write a brand-new one-sentence MIXED review")
print("   of a movie sequel.")
print(f"   The model wrote: {new_review.strip()}")
