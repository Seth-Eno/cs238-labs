"""Week 7 · Part 1: Sophia gets hands.

Shows Sophia's three tools exactly as the model receives them, then sends one
run-on request that needs all three. Run from this folder:  uv run sophia.py
"""
from genai.agent import show_tools, ask_sophia

print("Sophia is a study assistant with three tools. Here is each tool exactly")
print("as the model sees it: its name, what it takes in parentheses, and a")
print("one-sentence description.\n")
show_tools()

print("\nNow a request that needs more than one tool. How to read it:")
print("  USER   is the student's message.")
print("  TOOL   is a tool Sophia used: the tool's name, what she gave it in")
print("         parentheses, and after the -> what it handed back.")
print("  SOPHIA is her final reply, written after the tools are done.\n")
ask_sophia("I'm on page 95 of this 270-page book, reading 25 "
           "pages a night. How many nights until I finish? "
           "Define 'embedding', and note that I want to build "
           "a search tool.")
