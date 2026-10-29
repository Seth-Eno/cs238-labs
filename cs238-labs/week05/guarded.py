"""Week 5 · Part 4: defense in depth.

The chapter's capstone attack, sent through all four layers of the finished
assistant. Run from this folder:  uv run guarded.py
"""
from genai.security import (GuardedAssistant, User, Role,
                            CAPSTONE_ATTACK, CAPSTONE_DRAFT)

print("A malicious request from a researcher's account, sent through four")
print("layers of defense. How to read it:")
print("  RESEARCHER   the request")
print("  1 REDACT     what's left after private details are stripped out")
print("  2 INJECTION  any attack phrases the filter flagged")
print("  3 ACCESS     whether this user's role is allowed to do this")
print("  4 OUTPUT     whether the reply the model would have given gets blocked")
print("  ASSISTANT    what the user actually receives\n")
researcher = User("Dr. Lee", Role.RESEARCHER)
GuardedAssistant(researcher).show(CAPSTONE_ATTACK, draft=CAPSTONE_DRAFT)
