"""Week 5 · Task 4: what has the model memorized?

Write the start of a few lines you think the model has seen many times (a
famous speech, a poem, a saying) and one line you made up yourself. For each,
the model finishes the line, and we read how sure it was of the next word.
Run from this folder:  uv run my_recitation.py
"""
import math
import requests
from genai import get_host

MODEL = "llama3.2:latest"

lines = [
    ("famous",  "Four score and seven years"),                    # ← yours
    ("famous",  "Ask not what your country can do for"),          # ← yours
    ("made up", "The purple calculator whispered to the"),        # ← one you made up
]

def recite(start):
    """Write `start` into the model's own reply and let it continue. Returns the
    continuation and the probability it gave the very next word, from one call."""
    reply = requests.post(f"{get_host()}/api/chat", json={
        "model": MODEL, "stream": False,
        "messages": [{"role": "user", "content": "Finish this line."},
                     {"role": "assistant", "content": start}],   # the model continues this
        "options": {"temperature": 0, "num_predict": 12},
        "logprobs": True, "top_logprobs": 1,
    }).json()
    tokens = reply["logprobs"]
    first = next((t for t in tokens if t["token"].strip()), tokens[0])   # skip a bare space
    return reply["message"]["content"].strip(), first["token"].strip(), math.exp(first["logprob"])

print(f"{MODEL} finishes the start of each line. We write the start into the")
print("model's own reply (the Week 1 trick), so it has to continue it. 'How sure'")
print("is the probability it gave the next word, from 0% to 100%. A memorized")
print("line comes back nearly certain; a line it has never seen forces a guess.\n")
for kind, start in lines:
    finish, word, p = recite(start)
    print(f"── ({kind}) {start} ...")
    print(f"   The model continues:  {finish.replace(chr(10), ' ')}")
    print(f"   How sure it was of the next word, '{word}':  {p:.0%}\n")
