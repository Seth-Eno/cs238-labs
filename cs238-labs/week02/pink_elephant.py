"""Week 2 · Part 3: the pink elephant.

A ban has to name the thing it forbids, and naming it makes the model more
likely to say it. Run from this folder:  uv run pink_elephant.py
"""
import re
from genai import ask

def check(reply, banned):
    """Did the reply use the banned word anyway?"""
    if re.search(rf"\b{re.escape(banned)}", reply, re.IGNORECASE):
        return f"LEAKED: it said '{banned}'"
    return f"Held: no '{banned}'"

question = ("What is the largest land animal on Earth? "
            "Answer in one short sentence, "
            "but do not use the word 'elephant'.")
print(f'Asking two models: "{question}"\n')
for model in ["gemma4:latest", "llama3.2:latest"]:
    reply = ask(question, model=model, system=None, options={"temperature": 0},
                max_tokens=40).strip()
    print(f"── {model}")
    print(f"   {reply}")
    print(f"   {check(reply, 'elephant')}\n")

prompt = "Describe the ocean in one sentence. Do not use the word 'water'."
reply = ask(prompt, options={"temperature": 0}, max_tokens=40).strip()
print(f'Asking gemma4: "{prompt}"')
print(f"   {reply}")
print(f"   {check(reply, 'water')}")
