"""Week 5 · Part 3: leaks nobody typed.

Memorization, an embedding that gives away its secret, and poisoned examples.
Run from this folder:  uv run leaks.py
"""
import math
import requests
from genai import get_host
from genai.security import MEMORIZATION_PREFIXES, show_embedding_attack, show_poisoning

RECITE_MODEL = "llama3.2:latest"

def recite(start):
    """Write `start` into the model's own reply and let it continue. Returns the
    continuation and the probability it gave the very next word."""
    reply = requests.post(f"{get_host()}/api/chat", json={
        "model": RECITE_MODEL, "stream": False,
        "messages": [{"role": "user", "content": "Finish this line."},
                     {"role": "assistant", "content": start}],
        "options": {"temperature": 0, "num_predict": 12},
        "logprobs": True, "top_logprobs": 1,
    }).json()
    tokens = reply["logprobs"]
    first = next((t for t in tokens if t["token"].strip()), tokens[0])   # skip a bare space
    return reply["message"]["content"].strip(), first["token"].strip(), math.exp(first["logprob"])

# 1. Memorization: famous lines come back word for word, with high confidence
print("═══ 1. MEMORIZATION. We give the model the start of two famous lines,")
print("and one made-up line it can't have seen, and it finishes each one.")
print("'How sure' is the probability it gave the next word: 100% means certain.\n")
for kind, start, _ in MEMORIZATION_PREFIXES:
    label = "famous" if kind == "memorized" else "made up"
    finish, word, p = recite(start)
    print(f"── ({label}) {start} ...")
    print(f"   The model continues:  {finish.replace(chr(10), ' ')}")
    print(f"   How sure it was of the next word, '{word}':  {p:.0%}\n")

# 2. An embedding is not a disguise: guess the diagnosis from the vector alone
print("═══ 2. EMBEDDING LEAK. The attacker has only the stored embeddings of")
print("patient records, not the text. They embed a few guesses and keep the")
print("closest (cosine near 1 = very close). Then we reveal the real record.\n")
show_embedding_attack()

# 3. Poisoned examples: swap the labels and the judgment flips
print("\n═══ 3. POISONING. The model sorts emails using labeled examples.")
print("CLEAN is its answer with honest examples; POISON is its answer after")
print("the example labels were swapped.\n")
show_poisoning()
