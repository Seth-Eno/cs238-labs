"""Week 2 · Task 3: set your own pink-elephant traps (the chapter's Exercise 4).

Write two negative instructions of your own on the marked lines, each forbidding
a word strongly tied to its topic, and put that word after each prompt. Then
rewrite one as a positive instruction that gives the model somewhere to go.
Run from this folder:
    uv run my_bans.py
"""
import re
from genai import ask

# (name, prompt, the word to watch for)
traps = [
    ("Trap 1",                                                  # ← your trap
     "Describe a birthday party in one sentence. "
     "Do not use the word 'cake'.",
     "cake"),
    ("Trap 2",                                                  # ← your trap
     "Describe a library in one sentence. "
     "Do not use the word 'books'.",
     "books"),
    ("Positive rewrite",                                        # ← your rewrite
     "Describe a birthday party in one sentence, and call the "
     "dessert 'the sweet centerpiece'.",
     "cake"),
]

leaks = 0
for name, prompt, banned in traps:
    reply = ask(prompt, options={"temperature": 0}, max_tokens=40).strip()
    leaked = re.search(rf"\b{re.escape(banned)}", reply, re.IGNORECASE)
    print(f"── {name}")
    print(f"   Prompt: {prompt}")
    print(f"   Reply:  {reply}")
    if leaked:
        leaks += 1
        print(f"   LEAKED: the reply used '{banned}'\n")
    else:
        print(f"   Held: the reply avoided '{banned}'\n")
print(f"{leaks} of {len(traps)} replies used the word they were supposed to avoid.")
