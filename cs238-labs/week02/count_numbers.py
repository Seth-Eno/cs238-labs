"""Week 2 · Part 1.3: count the "random" numbers.

Predict what you'll see at temperature 2.0 before you run it:
    uv run count_numbers.py
"""
from collections import Counter
from genai import ask

TRIES = 6

def tally(prompt, temperature, **options):
    """Ask the same question TRIES times and count the different answers."""
    answers = [ask(prompt, max_tokens=8,
                   options={"temperature": temperature, **options}).strip()
               for _ in range(TRIES)]
    return Counter(answers)

def report(setting, counts):
    print(f"{setting}: {len(counts)} different answer(s) in {TRIES} tries")
    for answer, count in counts.most_common():
        print(f'    "{answer}"  {count} of {TRIES} times')
    print()

prompt = "Pick a random number between 1 and 10. Reply with only the number."
print(f'Asking "{prompt}" {TRIES} times at each temperature.\n')
for temp in [0.0, 1.0, 2.0]:
    report(f"Temperature {temp}", tally(prompt, temp))
