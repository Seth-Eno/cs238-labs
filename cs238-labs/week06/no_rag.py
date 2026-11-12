"""Week 6 · Part 1: the knowledge problem.

The book you're reading isn't in any model's training data.
Run from this folder:  uv run no_rag.py
"""
from genai import ask

question = ("What is covered in the chapter on Augmentation in the "
            "book 'Illustrating Generative AI' by Chiké Abuah?")
print(f"Asking the model, with no documents to look at:\n   {question}\n")
print("The model's answer:")
print(ask(question, max_tokens=80).strip())
