"""Week 2 · Optional: your own misguided-attention trap (the chapter's Exercise 1).

Write a problem that looks like a famous puzzle but has a trivial answer.
Run from the week02 folder:  uv run optional/my_puzzle.py
"""
from genai import ask

puzzle = ("Three people check into a hotel room that costs $30. "   # ← your puzzle
          "Nobody pays anything extra or gets any refund. "
          "How much did the room cost?")

print(f"Your puzzle: {puzzle}\n")
print("── llama3.2's answer when asked plainly:")
print(ask(puzzle, model="llama3.2:latest", max_tokens=200).strip())
print("\n── llama3.2's answer with \"Let's think step by step\" added:")
print(ask(puzzle + " Let us think step by step.",
          model="llama3.2:latest", max_tokens=300).strip())
