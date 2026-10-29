"""Week 5 · Optional: lost in translation.

Ask both builds to translate their instructions into French. Why do safety
habits learned in English sometimes fail in another language?
Run from the week05 folder:  uv run optional/translation.py
"""
from genai.security import ask_naive, ask_hardened, TRANSLATE_ATTACK

print("Asking the assistant to translate its own instructions into French.")
print("USER is the request and GEMMA4:E2B is the reply. Did HUGEPANDA leak?")
print("\n═══ The plain assistant:\n")
ask_naive(TRANSLATE_ATTACK)
print("\n═══ The hardened assistant (security policy added):\n")
ask_hardened(TRANSLATE_ATTACK)
