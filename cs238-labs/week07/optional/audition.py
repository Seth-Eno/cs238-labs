"""Week 7 · Optional: hold your own audition (the chapter's Exercise 1).

Put a different tool-capable model in MODEL and compare it with gemma4.
Run from the week07 folder:  uv run optional/audition.py
"""
from genai.agent import ask_sophia

MODEL = "llama3.2:latest"                                # ← the model to audition

print(f"Auditioning {MODEL} as Sophia. The first request needs the calculator")
print("tool; the second needs no tool at all. A TOOL line shows a tool she used,")
print("what she gave it, and after the -> what it returned.")
for request in [
    "I'm on page 95 of this 270-page book, reading 25 pages a night. "
    "How many nights until I finish?",
    "Thanks, you've been a huge help today!",            # should call nothing
]:
    print()
    ask_sophia(request, model=MODEL)
