"""Week 7 · Part 4: who knows what they don't know?

Self-refine (draft, critique, rewrite), then self-rated confidence on an
answerable and an impossible question. Run from this folder:
    uv run self_check.py
"""
import re
from genai import ask
from genai.agent import show_self_refine, show_turn

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

print("═══ 1. SELF-REFINE: Sophia writes a draft, critiques it herself, then")
print("rewrites it. The lines are labeled: USER (the question), SOPHIA draft,")
print("CRITIC (her own critique), and SOPHIA final.\n")
show_self_refine("Does retrieval-augmented generation "
                 "eliminate hallucinations?")

print("\n═══ 2. CONFIDENCE: Sophia answers, then rates how sure she is from")
print("1 to 5, shown as (score/5) next to her name. A score of 2 or lower adds")
print("an ESCALATE line: the answer gets held for a human to check.\n")
show_confidence("What is the capital of France?")
print()
show_confidence("What is the first name of the reader "
                "holding this book right now?")
