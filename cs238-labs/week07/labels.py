"""Week 7 · Part 3: labels decide everything.

The same date tool four ways: clear or vague name, clear or vague description.
Does the model still reach for it? Run from this folder:  uv run labels.py
"""
from datetime import date
from genai.agent import tool_spec, run_with_trace

def days_until(**args):
    target = next(iter(args.values()), "")   # whatever the argument is called
    try:
        return {"days": (date.fromisoformat(target) - date.today()).days}
    except ValueError:
        return {"error": "use the format YYYY-MM-DD"}

CLEAR_DESC = "Count the days from today until a date given as YYYY-MM-DD."
VAGUE_DESC = "Returns a number for the given input."
versions = {
    "Clear name and clear description": ("days_until", CLEAR_DESC, "target"),
    "Vague name ('fn')":                ("fn",         CLEAR_DESC, "x"),
    "Vague description":                ("days_until", VAGUE_DESC, "target"),
    "Both vague":                       ("fn",         VAGUE_DESC, "x"),
}
question = "How many days are left until December 25, 2026?"

print(f"The same question, '{question}',")
print("with the same tool labeled four ways. Did the model use the tool?")
print(f"  The clear description: \"{CLEAR_DESC}\"")
print(f"  The vague description: \"{VAGUE_DESC}\"")
for label, (name, desc, param) in versions.items():
    tools = [tool_spec(name, desc, **{param: "string"})]
    reply, calls = run_with_trace(question, tools, {name: days_until})
    print(f"\n── {label}")
    print(f"   Used the tool? {'yes' if calls else 'NO'}")
    for tool_name, args, result in calls:
        shown = ", ".join(f"{k}={v!r}" for k, v in args.items())
        print(f"   It called {tool_name}({shown}) and got back {result}")
    print(f"   Reply: {reply[:100]}")
