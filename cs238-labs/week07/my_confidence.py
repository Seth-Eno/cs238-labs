"""Week 7 · Task 4: does the confidence score track reality?

Write two impossible questions (about the future, about you, about something
private) and one tricky question the model might know. Run from this folder:
    uv run my_confidence.py
"""
import re
from genai import ask
from genai.agent import show_turn

def show_confidence(question):
    """Sophia answers, then rates how sure she is from 1 to 5. A score of 2 or
    lower holds the answer back for a human to check."""
    answer = ask(question, max_tokens=80).strip()
    reply = ask("Rate your confidence 1 (guessing) to 5 (certain).\n"
                f"Q: {question}\nA: {answer}\nSingle digit only.", max_tokens=3)
    number = re.search(r"\d+", reply)    # the first number; the model may bold it or keep going
    score = min(max(int(number.group()), 1), 5) if number else None
    show_turn("USER", question)
    label = f"SOPHIA ({score}/5)" if score else "SOPHIA (no score)"
    show_turn(label, answer if len(answer) <= 140 else answer[:140] + "...")
    if score is not None and score <= 2:
        show_turn("ESCALATE", "low confidence: hold the answer and flag it for a "
                              "human and a source check before the reader sees it")

questions = [
    "What will I eat for dinner next Tuesday?",          # ← impossible
    "What is my best friend's middle name?",              # ← impossible
    "In what year did the Battle of Hastings happen?",    # ← tricky but knowable
]

print("Sophia answers each question, then rates how sure she is from 1 to 5,")
print("shown as (score/5) next to her name. A score of 2 or lower adds an")
print("ESCALATE line: the answer gets held for a human to check.")
for q in questions:
    print()
    show_confidence(q)
