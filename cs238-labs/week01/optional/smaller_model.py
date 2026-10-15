"""Week 1 · Optional: bigger isn't always better (the chapter's Warm-Up 2).

Run from the week01 folder:  uv run optional/smaller_model.py
"""
from genai import ask

question = "What does generative mean?"
print(f'Asking two models the same question: "{question}"\n')
for model, size in [("gemma4:latest", "the larger model"),
                    ("llama3.2:1b", "a much smaller model")]:
    print(f"── Answer from {model} ({size}):")
    print(ask(question, model=model))
    print()
