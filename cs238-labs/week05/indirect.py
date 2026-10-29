"""Week 5 · Part 2: attacks that ride in on documents.

Indirect injection hides the instruction in a document the system trusts.
The hardened assistant refuses to hand over the code when asked directly,
yet obeys the same request planted in a note. Run from this folder:
    uv run indirect.py
"""
from genai.security import ask_about_note, ask_hardened, CLEAN_NOTE, POISONED_NOTE, DIRECT_ASK

print("How to read this: USER is the request, DOCUMENT is the clinical note the")
print("assistant was handed, and GEMMA4:E2B is its reply.\n")

print("═══ 1. The everyday job: summarize a clean note.\n")
ask_about_note(CLEAN_NOTE)                     # the everyday job

print("\n═══ 2. The same job, but someone planted one extra sentence in the note.\n")
ask_about_note(POISONED_NOTE)                  # one planted sentence

print("\n═══ 3. The poisoned note again, with the security policy turned on.\n")
ask_about_note(POISONED_NOTE, hardened=True)   # the policy doesn't help

print("\n═══ 4. For comparison: asking the same hardened assistant for the code")
print("directly.\n")
ask_hardened(DIRECT_ASK)                       # the policy works here
