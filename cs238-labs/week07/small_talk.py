"""Week 7 · Task 1: deliberate or eager?

The same three tools, but a message that needs none of them.
Run from this folder:  uv run small_talk.py
"""
from genai.agent import ask_sophia

print("A message that needs no tools. If Sophia used one, a TOOL line would")
print("appear between USER (the student) and SOPHIA (her reply).\n")
ask_sophia("Thanks, you've been a huge help today!")
