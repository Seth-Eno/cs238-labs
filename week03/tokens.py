"""Week 3 · Part 1.1: what's a token?

A token is a chunk, not a word. Watch where the splits fall.
Run from this folder:  uv run tokens.py
"""
from genai import count_tokens, tokenize

def pieces(text):
    """The tokens, separated by | , with · marking each space."""
    return " | ".join(t.replace(" ", "·") for t in tokenize(text))

print("How GPT-4's tokenizer splits each word into tokens.")
print("Tokens are separated by | . A � is a piece of a character that")
print("takes more than one token to spell.\n")
for s in ["cat", "tokenization", "antidisestablishmentarianism",
          "🍓", "café"]:
    n = count_tokens(s)
    print(f"{s:30} {n} token{'' if n == 1 else 's'}:  {pieces(s)}")
