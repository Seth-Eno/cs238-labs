"""Week 2 · Part 1.3: count the answers.

Ask for an animal six times at each temperature and count what comes back.
Run from this folder:  uv run count_animals.py
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

prompt = "Name one animal. Reply with one word."
print(f'Asking "{prompt}" {TRIES} times at each setting.\n')
for temp in [0.0, 1.0, 2.0]:
    report(f"Temperature {temp}", tally(prompt, temp))
report("Temperature 2.0 with top_k=1", tally(prompt, 2.0, top_k=1))
