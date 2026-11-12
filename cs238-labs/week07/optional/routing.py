"""Week 7 · Optional: route by difficulty (the chapter's Economics section).

Three tasks from easy to hard, each sent to the big and the small model.
Which could you safely route to the cheaper one?
Run from the week07 folder:  uv run optional/routing.py
"""
from genai import ask

tasks = [
    ("Easy",   "How many metres are in 3 kilometres? Reply with only the number.",
     "3000"),
    ("Medium", "A bat and a ball cost 1.10 dollars in total. The bat costs "
               "1 dollar more than the ball. How much is the ball? "
               "Reply with only the number.",
     "0.05"),
    ("Hard",   "A snail at the bottom of a 7 m well climbs 4 m each day and "
               "slides back 3 m each night. How many days to reach the top? "
               "Reply with only the number.",
     "4"),
]

print("Three tasks of rising difficulty, each sent to a big and a small model.")
for level, task, correct in tasks:
    print(f"\n── {level}: {task}")
    print(f"   (The correct answer is {correct}.)")
    for model in ["gemma4:latest", "llama3.2:latest"]:
        print(f"   {model} says: {' '.join(ask(task, model=model, max_tokens=60).split())}")
