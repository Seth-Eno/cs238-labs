"""Week 3 · Task 2: spell your own word backward (the chapter's Exercise 1).

Put a word of your own on the marked line (a long one is more interesting),
predict whether the model can spell it backward, then run:
    uv run my_backward.py
"""
from genai import ask, tokenize

word = "stochastic"                                       # ← your word

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

answer = word[::-1]
reply = ask(f"Spell the word '{word}' backward. Reply with only the "
            "backward spelling.", model=MODEL, max_tokens=40).strip()

print(f"Asking {MODEL} to spell your word, '{word}', backward.")
print(f"(Capital letters don't matter: '{answer.upper()}' would count the same as '{answer}'.)\n")
print(f"   Your word as tokens:   {pieces(word)}")
print(f"   The model says:        {reply}")
print(f"   The real answer:       {answer}")
print(f"   The model is {'RIGHT' if spelled_right(reply, answer) else 'WRONG'}.\n")
print("The backward spelling is a string the tokenizer has rarely seen, so it")
print(f"breaks into different pieces:  {pieces(answer)}")
