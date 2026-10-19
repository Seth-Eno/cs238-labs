"""Week 3 · Part 1.3: numbers come in chunks.

Run from this folder:  uv run my_number_chunks.py
"""
import re
from genai import ask, tokenize

# The model to test. For Part B, change it to "qwen3.5:0.8b" or "llama3.2:latest".
MODEL = "qwen3.5:0.8b"                                   # ← change for Part B

# Numbers chunk three digits from the left, not by place value
print("How GPT-4's tokenizer splits numbers into tokens (separated by | ):\n")
for n in ["42", "1234", "1234567", "8675309"]:
    print(f"   {n:9} →  {' | '.join(tokenize(n))}")

a, b = 3947, 6281
prompt = f"What is {a} * {b}? Reply with only the number."
print(f"\nAsking {MODEL}: {prompt}")
reply = ask(prompt, model=MODEL, max_tokens=40).strip()
numbers = re.findall(r"-?\d[\d,]*", reply)   # the last number in the reply
right = bool(numbers) and numbers[-1].replace(",", "") == str(a * b)
print(f"   The model says:   {reply}")
print(f"   The real answer:  {a * b:,}  (the model is {'right' if right else 'wrong'})")
