"""Week 3 · Task 3: your own arithmetic problems.

Keep the four starter problems below and replace the last three with your
own: some you expect the model to get right, and some you expect it to miss.
Each one is (number, operation, number), where the operation is "+", "-",
"*", or "/". Predict, then run:
    uv run my_arithmetic.py
"""
import re
from genai import ask, tokenize

problems = [
    (47, "+", 38),                 # the four starter problems
    (3947, "*", 6281),
    (123456789, "+", 987654321),
    (98765, "/", 43),
    (99, "*", 99),                                        # ← your problems
    (1243, "-", 1),                                       # ← your problems
    (250, "/", 1234),                                        # ← your problems
]

# The model to test. For Part B, change it to "qwen3.5:0.8b" or "llama3.2:latest".
MODEL = "llama3.2:latest"                                   # ← change for Part B

def solve(a, op, b):
    """Python does the arithmetic exactly, digit by digit."""
    return {"+": a + b, "-": a - b, "*": a * b, "/": a / b}[op]

def last_number(reply):
    """The last number in the model's reply, with commas removed."""
    numbers = re.findall(r"-?\d[\d,]*(?:\.\d+)?", reply)
    return float(numbers[-1].replace(",", "")) if numbers else None

def chunks(n):
    """How the tokenizer splits a number, separated by | ."""
    return " | ".join(tokenize(str(n)))

print(f"Asking {MODEL} your arithmetic problems. Each number is also shown")
print("split into tokens (separated by | ), the way the model reads it.")
right_count = 0
for a, op, b in problems:
    answer = solve(a, op, b)
    prompt = f"What is {a} {op} {b}? Reply with only the number."
    reply = ask(prompt, model=MODEL, max_tokens=40).strip()
    got = last_number(reply)
    right = got is not None and abs(got - answer) < 0.01
    right_count += right
    shown = f"{answer:,.2f}" if op == "/" else f"{answer:,}"
    print(f"\n── {a:,} {op} {b:,}")
    print(f"   As tokens:        {chunks(a)}   {op}   {chunks(b)}")
    print(f"   The model says:   {reply}")
    print(f"   The real answer:  {shown}  (the model is {'right' if right else 'WRONG'})")
    if got is not None and not right:
        same_size = len(str(int(abs(got)))) == len(str(int(abs(answer))))
        off = f"{abs(got - answer):,.2f}" if op == "/" else f"{abs(got - answer):,.0f}"
        print(f"   It's off by {off}, and "
              f"{'has the right number of digits' if same_size else 'has the wrong number of digits'}.")
print(f"\nThe model got {right_count} of {len(problems)} right.")
