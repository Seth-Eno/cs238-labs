"""Week 7 · Task 2: build your own tool.

Replace count_letter with a tool of your own (something a language model is bad
at on its own), describe it with tool_spec, and write three requests: one that
needs your tool, one that needs both tools, and one that needs neither.
Run from this folder:  uv run my_tool.py
"""
from datetime import date
from genai.agent import tool_spec, ask_sophia
import random

def days_until(target: str = "", **_):
    try:
        return {"days": (date.fromisoformat(target) - date.today()).days}
    except ValueError:
        return {"error": "use the format YYYY-MM-DD"}

def roll_dice(sides: int = 0, times: int = 0, **_):          # ← your function
    sum = 0
    for i in range(times):
        sum += random.randint(1, sides)
    return {"roll": sum}

tools = [
    tool_spec("days_until",
              "Count the days from today until a date given as YYYY-MM-DD.",
              target="string"),
    tool_spec("roll_dice",                                    # ← your tool's name
              "Roll a dice of any number of sides any number of times.",  # ← its description
              sides="sides", times="times"),                   # ← its parameters
]
handlers = {"days_until": days_until,
            "roll_dice": roll_dice}                        # ← name → function

requests = [                                                     # ← your three requests
    "Roll 10, 20 sided dice and give me the total",
    "How many days until 2026-12-25, and roll 2, 6 sided dice for me.",
    "What's your favorite crater on the moon?",
]

print("How to read each conversation:")
print("  USER   is the request.")
print("  TOOL   is a tool Sophia used: its name, what she gave it in parentheses,")
print("         and after the -> what it handed back. No TOOL line means she")
print("         answered without any tool.")
print("  SOPHIA is her final reply.")
for number, request in enumerate(requests, start=1):
    print(f"\n── Request {number}\n")
    ask_sophia(request, tools=tools, handlers=handlers)
