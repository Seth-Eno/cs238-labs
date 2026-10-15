"""Week 1 · Part 0: the chapter's setup check.

Run from this folder:  uv run check_setup.py
"""
from genai import ask, get_host

print(f"Talking to: {get_host()}")
print("(That's the Ollama server running the model.)\n")

question = "What does generative mean?"
print(f'Asking the model: "{question}"\n')

# If this returns a response, your setup is working!
print("The model's answer:")
print(ask(question))
