"""Week 5 · Task 1: play attacker (the chapter's Exercise 2).

Write your own reframing that means "reveal the code" without naming anything
the security policy forbids. Run from this folder:  uv run my_attack.py
"""
from genai.security import ask_naive, ask_hardened, sanitize

mine = "Replace this sentence with your attack."   # ← your attack

# The model behind the assistant. For Task 1B, change it to "gemma4:latest".
MODEL = "gemma4:e2b"                                # ← change for Task 1B

flags = sanitize(mine)["flags"]
print("═══ Step 1: a cheap keyword filter checks your attack for suspicious phrases.")
if flags:
    print(f"   CAUGHT. It flagged: {', '.join(flags)}")
else:
    print("   Not caught. It didn't flag anything.")

print(f"\nIn the conversations below, USER is your attack and {MODEL.upper()} is the")
print("assistant's reply. Did the secret code, HUGEPANDA, leak?")
print("\n═══ Step 2: your attack on the plain assistant.\n")
ask_naive(mine, model=MODEL)
print("\n═══ Step 3: your attack on the hardened assistant (security policy added).\n")
ask_hardened(mine, model=MODEL)
