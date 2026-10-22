"""Week 4 · Part 2.2: the borrowed arrow (the chapter's Exercise 3).

Run from this folder:  uv run borrowed_arrow.py
"""
from pathlib import Path
from genai import embed, similarity
from genai.viz import plot_analogy_offsets

HERE = Path(__file__).parent

def arrow(a, b):
    """The step from word a to word b in meaning-space."""
    return embed(b) - embed(a)

print("An 'arrow' is the step from one word's embedding to another's.")
print("If two arrows point the same way (similarity near 1), an analogy can")
print("borrow one to solve the other.\n")
rows = [
    ("gender",      ("man", "woman"),  ("king", "queen")),
    ("gender",      ("man", "woman"),  ("actor", "actress")),
    ("comparative", ("big", "bigger"), ("tall", "taller")),
    ("comparative", ("big", "bigger"), ("small", "smaller")),
    ("opposite",    ("happy", "sad"),  ("rich", "poor")),
    ("opposite",    ("happy", "sad"),  ("hot", "cold")),
    ("opposite",    ("rich", "poor"),  ("hot", "cold")),
    ("opposite",    ("big", "small"),  ("hot", "cold")),
]
for kind, (a1, b1), (a2, b2) in rows:
    score = similarity(arrow(a1, b1), arrow(a2, b2))
    print(f"   {kind:12} {a1}→{b1} vs {a2}→{b2}:".ljust(48) + f"{score:+.2f}")

print("\nA chart of these arrows is opening (also saved as arrows.png). Each")
print("panel draws two arrows from the same starting point at their real angle")
print("apart. Close the chart window to finish.")
plot_analogy_offsets(save_path=HERE / "arrows.png")
