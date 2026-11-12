"""Week 7 · Optional: watch reflection rescue a coder (the chapter's Exercise 3).

One fail → lesson → pass cycle. The two attempts are real code from the
chapter; the one-sentence lesson between them is written live by gemma4.
Run from the week07 folder:  uv run optional/reflexion.py
"""
import genai.agent
from genai.agent import show_reflexion_trace

genai.agent.REFLEXION_MODEL = "gemma4:latest"   # the chapter used lfm2:24b, which isn't on the class server

print("Reflexion: the model writes code (try1), a TEST runs it and says PASS or")
print("FAIL, the model writes itself a one-sentence lesson (REFLECT), and then")
print("tries again (try2) with that lesson in mind.\n")
show_reflexion_trace()
