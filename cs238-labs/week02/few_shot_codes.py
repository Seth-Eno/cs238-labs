"""Week 2 · Part 2: when do examples earn their tokens?

Five student questions, but the labels are meaningless codes: Q1 is
logistics, Q2 conceptual, Q3 debugging. First with no examples, then with
three. Run from this folder:  uv run few_shot_codes.py
"""
from genai import ask

ZERO = """Classify each student question as Q1, Q2, or Q3.

Reply with exactly one label. Classify this question:
Question: {body}"""

THREE = """Classify each student question as Q1, Q2, or Q3.

Question: "When is the project due?" → Q1
Question: "Why does gradient descent need a learning rate?" → Q2
Question: "My loop prints nothing, what is wrong?" → Q3

Reply with exactly one label. Classify this question:
Question: {body}"""

# Each question with its correct code
questions = [
    ("What time are office hours on Friday?",             "Q1"),
    ("How is attention different from convolution?",      "Q2"),
    ("My function returns None instead of a list, why?",  "Q3"),
    ("Is the midterm cumulative?",                        "Q1"),
    ("What does raising the temperature actually do?",    "Q2"),
]

def classify_all(template):
    right = 0
    for question, correct in questions:
        reply = ask(template.format(body=question), options={"temperature": 0.1})
        label = (reply.split() or ["(none)"])[0].strip('.,:"*')
        if label == correct:
            right += 1
            mark = "right"
        else:
            mark = "WRONG"
        print(f"  {question}")
        print(f"      model said {label}, correct is {correct}: {mark}")
    print(f"  Score: {right} of {len(questions)} right\n")

print("The codes mean: Q1 = logistics, Q2 = conceptual, Q3 = debugging.")
print("The model is never told that; it can only learn it from examples.\n")
print("── Version 1: no examples in the prompt")
classify_all(ZERO)
print("── Version 2: three labeled examples in the prompt")
classify_all(THREE)
