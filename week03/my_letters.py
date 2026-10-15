"""Week 3 · Part 1.2: letters the model can't see.

Run from this folder:  uv run my_letters.py
"""
import re
from genai import ask, tokenize

# The model to test. For Part B, change it to "qwen3.5:0.8b" or "llama3.2:latest".
MODEL = "gemma4:latest"                                   # ← change for Part B

def pieces(text):
    """The tokens, separated by | ."""
    return " | ".join(tokenize(text))

def letters_only(text):
    """Lowercase, with everything but letters removed."""
    return "".join(ch for ch in text.lower() if ch.isalpha())

def spelled_right(reply, target):
    """Did the reply contain the target spelling? Capital letters don't count
    against it, and neither do spaces or dashes between the letters."""
    target = letters_only(target)
    words = [letters_only(w) for w in reply.split()]
    return target in words or letters_only(reply) == target

print(f"Asking {MODEL} to count letters. It reads tokens, not letters,")
print("so each word is also shown split into tokens (separated by | ).\n")
for word, letter in [("strawberry", "r"), ("mississippi", "s"),
                     ("parallel", "l")]:
    reply = ask(f"How many times does the letter '{letter}' appear in "
                f"'{word}'? Reply with only the number.", model=MODEL,
                max_tokens=10).strip()
    correct = word.lower().count(letter.lower())
    numbers = re.findall(r"\d+", reply)
    verdict = "right" if numbers and numbers[0] == str(correct) else "wrong"
    print(f"How many '{letter}'s are in '{word}'?")
    print(f"   As tokens:        {pieces(word)}")
    print(f"   The model says:   {reply}")
    print(f"   The real answer:  {correct}  (the model is {verdict})\n")

word = "tokenization"
backward = ask(f"Spell the word '{word}' backward. Reply with only the "
               "backward spelling.", model=MODEL, max_tokens=30).strip()
answer = word[::-1]
print(f"Asking {MODEL} to spell '{word}' backward.")
print(f"   The model says:   {backward}")
print(f"   The real answer:  {answer}  "
      f"(the model is {'right' if spelled_right(backward, answer) else 'wrong'})")
