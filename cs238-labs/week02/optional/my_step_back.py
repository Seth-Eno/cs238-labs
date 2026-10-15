"""Week 2 · Optional: your own step-back question (the chapter's Exercise 2).

Find a question where your own first instinct tends to be wrong.
Run from the week02 folder:  uv run optional/my_step_back.py
"""
from genai import ask
from genai.prompting import step_back

question = ("If it takes 5 machines 5 minutes to make 5 widgets, how many "   # ← yours
            "minutes would it take 100 machines to make 100 widgets?")

print(f"Your question: {question}\n")
print("── The model's answer when asked directly:")
print(ask(question, max_tokens=100).strip())

principle, answer = step_back(question)
print("\n── Step-back, part 1: the model first names the general principle:")
print(principle.strip())
print("\n── Step-back, part 2: then it answers using that principle:")
print(answer.strip())
