"""Week 2 · Part 4: the reasoning ladder.

Misguided attention, chain of thought, and step-back prompting.
Run from this folder:  uv run reasoning.py
"""
import re
from genai import ask
from genai.prompting import show_step_back

# 1. Misguided attention: a famous puzzle with a trivial twist
puzzle = ("A farmer has a wolf, goat, and cabbage. "
          "He can carry one at a time.\n"
          "How does he get just the goat safely across? "
          "He doesn't need anything else.")
print("═══ 1. MISGUIDED ATTENTION")
print("A famous puzzle with a twist: only the goat needs to cross.")
print(f"The puzzle: {puzzle}\n")
print("llama3.2's answer:")
print(ask(puzzle, model="llama3.2:latest", options={"num_predict": 200}).strip())

# 2. Chain of thought: asked directly vs. "Let's think step by step."
problem = "When I was 6 my sister was half my age. Now I am 70. How old is my sister?"
correct = "67"
print("\n═══ 2. CHAIN OF THOUGHT")
print(f"The problem: {problem}  (The correct answer is {correct}.)")
print("Each model answers twice: directly, and with \"Let's think step by step.\"")
print("We show the final number in each answer.\n")

def final_number(text):
    numbers = re.findall(r"-?\d+", text)
    return numbers[-1] if numbers else "no number"

for model in ["gemma4:latest", "llama3.2:latest"]:
    direct = final_number(ask(problem, model=model, max_tokens=80))
    stepwise = final_number(ask(problem + "\nLet's think step by step.",
                                model=model, max_tokens=160))
    print(f"── {model}")
    print(f"   asked directly:   {direct}"
          f"  ({'right' if direct == correct else 'wrong'})")
    print(f"   step by step:     {stepwise}"
          f"  ({'right' if stepwise == correct else 'wrong'})")

# 3. Step-back: name the principle first, then answer
print("\n═══ 3. STEP-BACK")
print("A half-life question, asked two ways: directly (\"cold\"), then after the")
print("model first names the general principle that applies. Each answer is")
print("marked correct or wrong.\n")
show_step_back("Half")
