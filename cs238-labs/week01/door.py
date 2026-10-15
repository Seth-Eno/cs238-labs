"""Week 1 · Part 2.2: a door that opens onto anything.

Run from this folder:  uv run door.py
"""
from pathlib import Path
from genai import next_token_distribution
from genai.viz import plot_two_step

HERE = Path(__file__).parent
MODEL = "llama3.2:latest"
door = "She opened the door and saw a"

# 1. The forecast for the first word: many reasonable options
step1 = next_token_distribution(door, model=MODEL, top_k=6)
print(f'Step 1: the model\'s top guesses for the word after "{door}"')
print("(how likely the model thinks each one is to come next):")
for token, p in step1:
    print(f'  "{token.strip()}"  {p:.1%}')

# 2. Lock in the favorite and forecast the word after it
top_word = step1[0][0]
step2 = next_token_distribution(door, model=MODEL, top_k=6,
                                reply_start=top_word)
print(f'\nStep 2: we lock in the favorite, "{top_word.strip()}". The model\'s')
print("top guesses for the word after that:")
for token, p in step2:
    print(f'  "{token.strip()}"  {p:.1%}')

print("\nA chart of both steps is opening (also saved as door.png).")
print("Close the chart window to finish.")
plot_two_step(door, top_word, step1, step2, HERE / "door.png")
