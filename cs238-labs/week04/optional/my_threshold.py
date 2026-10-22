"""Week 4 · Optional: testing AI with AI (the chapter's Exercise 7).

There's no single right wording for a model's answer, so an automated test
can't just check `answer == expected`. Instead, compare meanings. Put two
questions on the marked lines and pick a threshold, then run from the week04
folder:
    uv run optional/my_threshold.py
"""
from genai import ask, similarity

question = "Why is the sky blue? Answer in two sentences."          # ← yours
other_question = "How do bees make honey? Answer in two sentences."  # ← a different one
THRESHOLD = 0.8                                                      # ← your threshold

first = ask(question, options={"temperature": 0.8})
second = ask(question, options={"temperature": 0.8})
different = ask(other_question, options={"temperature": 0.8})

print(f"Asking the same question twice: {question}\n")
print(f"   Answer 1: {first.strip()}\n")
print(f"   Answer 2: {second.strip()}\n")
print(f"And a different question: {other_question}\n")
print(f"   Answer 3: {different.strip()}\n")

print(f"Do the answers agree? Our test says yes when similarity is at least {THRESHOLD}.\n")
for label, a, b in [("Answer 1 vs Answer 2 (same question)", first, second),
                    ("Answer 1 vs Answer 3 (different question)", first, different)]:
    score = similarity(a, b)
    verdict = "AGREE" if score >= THRESHOLD else "DIFFERENT"
    print(f"   {label}: {score:.3f}  →  {verdict}")
