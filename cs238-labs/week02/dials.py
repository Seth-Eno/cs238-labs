"""Week 2 · Part 1.2: seeing the dials.

Temperature reshapes the odds; top-k and top-p trim which words are allowed.
Run from this folder:  uv run dials.py
"""
from pathlib import Path
from genai import ask, next_token_distribution
from genai.viz import plot_sampling_controls

HERE = Path(__file__).parent

dist = next_token_distribution("She opened the door and saw a",
                               model="llama3.2:latest", top_k=10)
print('A chart is opening (also saved as sampling_controls.png). It uses the')
print('model\'s real guesses for the word after "She opened the door and saw a".')
print("  Left side:  temperature reshapes the odds. Low temperature makes the")
print("              favorite even more likely; high temperature evens things out.")
print("  Right side: top-k and top-p decide which words are allowed at all.")
print("Close the chart window to continue.\n")
plot_sampling_controls(dist, k=3, p=0.9, n=5,
                       save_path=HERE / "sampling_controls.png")

# Temperature is the accelerator; top-k and top-p are the brakes
prompt = "Describe a walk on the beach in one sentence."
print(f'Now the same prompt under three settings: "{prompt}"\n')
settings = [
    ("Safe: temperature 0.7, brakes on (top_k=40, top_p=0.9)",
     {"temperature": 0.7, "top_k": 40, "top_p": 0.9}),
    ("Hot only: temperature 2.0, brakes still on (top_k=40, top_p=0.9)",
     {"temperature": 2.0, "top_k": 40, "top_p": 0.9}),
    ("Brakes off: temperature 2.0, no top-k or top-p limit",
     {"temperature": 2.0, "top_k": 0, "top_p": 1.0}),
]
for label, options in settings:
    print(f"── {label}")
    print(ask(prompt, options=options, max_tokens=40).strip())
    print()
