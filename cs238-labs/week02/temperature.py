"""Week 2 · Part 1.1: temperature, the chapter's sweep.

Run it twice:  uv run temperature.py
"""
from genai import ask

prompt = ("Write a creative opening for a story that starts "
          "like: 'If I could start over, who would I be?'")

print("Asking for the same story opening at three temperatures.")
print("Low temperature = safe and predictable; high = more random.\n")
for temp in [0.0, 0.7, 1.5]:
    print(f"── Temperature {temp}:")
    print(ask(prompt, options={"temperature": temp}).strip())
    print()
