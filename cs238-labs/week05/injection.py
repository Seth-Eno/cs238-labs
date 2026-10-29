"""Week 5 · Part 1: prompt injection.

The assistant's hidden system prompt holds an override code it must never
reveal. Run from this folder:  uv run injection.py
"""
from genai.security import (show_system_prompt, ask_naive, ask_hardened,
                            REPEAT_ATTACK, THIRD_PERSON_ATTACK)

print("How to read this: USER is the attacker's message, and GEMMA4:E2B is the")
print("assistant's reply. Watch for the secret code, HUGEPANDA.\n")

print("═══ The assistant's hidden instructions (its SYSTEM prompt). Real users")
print("never see this, and it contains the secret.\n")
show_system_prompt()                 # what the model is guarding

print("\n═══ Attack 1, on the plain assistant: an innocent-sounding request to")
print("repeat the words above.\n")
ask_naive(REPEAT_ATTACK)             # plain assistant, innocent-sounding ask

print("\n═══ The same attack, on the hardened assistant (a security policy has")
print("been added to its instructions).\n")
ask_hardened(REPEAT_ATTACK)          # same ask, security policy added

print("\n═══ Attack 2, on the hardened assistant: the same request reworded in")
print("the third person.\n")
ask_hardened(THIRD_PERSON_ATTACK)    # reworded, still hardened
