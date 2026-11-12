"""Week 7 · Part 2: a date tool.

Models can't know today's date or count days reliably, so we give it a tool.
Run from this folder:  uv run date_tool.py
"""
from datetime import date
from genai.agent import tool_spec, ask_sophia

def days_until(target: str = "", **_):
    """Our Python function: the model never runs this, we do."""
    try:
        return {"days": (date.fromisoformat(target) - date.today()).days}
    except ValueError:
        return {"error": "use the format YYYY-MM-DD"}

tools = [tool_spec("days_until",
                   "Count the days from today until a date given as YYYY-MM-DD.",
                   target="string")]
handlers = {"days_until": days_until}

print("Sophia gets one new tool, days_until. How to read the conversation:")
print("  USER   is the student's message.")
print("  TOOL   is the tool she used, the date she gave it, and after the ->")
print("         the number of days our Python code worked out.")
print("  SOPHIA is her final reply.\n")
ask_sophia("How many days are left until December 25, 2026?",
           tools=tools, handlers=handlers)
