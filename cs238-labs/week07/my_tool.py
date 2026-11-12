"""Week 7 · Task 2: build your own tool.

Replace count_letter with a tool of your own (something a language model is bad
at on its own), describe it with tool_spec, and write three requests: one that
needs your tool, one that needs both tools, and one that needs neither.
Run from this folder:  uv run my_tool.py
"""
from datetime import date
from genai.agent import tool_spec, ask_sophia

def days_until(target: str = "", **_):
    try:
        return {"days": (date.fromisoformat(target) - date.today()).days}
    except ValueError:
        return {"error": "use the format YYYY-MM-DD"}

def count_letter(word: str = "", letter: str = "", **_):          # ← your function
    return {"count": word.lower().count(letter.lower())}

tools = [
    tool_spec("days_until",
              "Count the days from today until a date given as YYYY-MM-DD.",
              target="string"),
    tool_spec("count_letter",                                    # ← your tool's name
              "Count how many times a letter appears in a word.",  # ← its description
              word="string", letter="string"),                   # ← its parameters
]
handlers = {"days_until": days_until,
            "count_letter": count_letter}                        # ← name → function

requests = [                                                     # ← your three requests
    "How many r's are in strawberry?",
    "How many days until 2026-12-25, and how many s's are in Mississippi?",
    "What's a good name for a goldfish?",
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
