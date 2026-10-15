"""Week 3 · Task 1: your own strings (the chapter's Exercise 1).

Put your own name, a long technical term from your major, a common English
word, and an emoji on the marked lines. Guess first, then run:
    uv run my_tokens.py
"""
from genai import count_tokens, tokenize

def pieces(text):
    """The tokens, separated by | , with · marking each space."""
    return " | ".join(t.replace(" ", "·") for t in tokenize(text))

mine = [
    "Chiké",                       # ← your name
    "photosynthesis",              # ← a long term from your major
    "house",                       # ← a common English word
    "🎸",                          # ← an emoji
]

print("How GPT-4's tokenizer splits your words into tokens.")
print("Tokens are separated by | . A � is a piece of a character that")
print("takes more than one token to spell.\n")
for s in mine:
    n = count_tokens(s)
    print(f"{s:30} {n} token{'' if n == 1 else 's'}:  {pieces(s)}")
