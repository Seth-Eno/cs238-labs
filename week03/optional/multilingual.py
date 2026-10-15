"""Week 3 · Optional: a newer tokenizer for more languages.

GPT-4o's tokenizer was built with far more non-English text than GPT-4's.
Run from the week03 folder:  uv run optional/multilingual.py
"""
from genai import count_tokens

samples = {                                                                    # ← add your own
    "English":  "Tokenization is the bridge between human text and model numbers.",
    "Spanish":  "La tokenización es el puente entre el texto humano y los números del modelo.",
    "Hindi":    "टोकनाइज़ेशन मानव पाठ और मॉडल संख्याओं के बीच का पुल है।",
    "Japanese": "トークン化は、人間のテキストとモデルの数値をつなぐ橋です。",
}

print("The same sentence through two tokenizers: GPT-4's, and GPT-4o's newer")
print("one, which learned from much more non-English text. (The first run")
print("downloads GPT-4o's vocabulary, a few megabytes.)\n")
for label, text in samples.items():
    old, new = count_tokens(text), count_tokens(text, "multilingual")
    print(f"   {label:9} GPT-4: {old:3} tokens    GPT-4o: {new:3} tokens")
