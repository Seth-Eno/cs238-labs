"""Week 1 · Optional: your own pronoun test (the chapter's Exercise 2).

Write two sentences that differ by one word, where that word changes which
noun the pronoun points back to. Predict the answer, then run:
    uv run optional/my_attention.py
"""
from pathlib import Path
from genai.viz import plot_attention, plot_attention_votes

HERE = Path(__file__).parent

sentences = [
    "The trophy didn't fit in the suitcase because it was too big.",    # ← yours
    "The trophy didn't fit in the suitcase because it was too small.",  # ← yours
]
pronoun = "it"                                                          # ← yours

print(f'Chart 1 (my_attention.png): how much "{pronoun}" looks back at each')
print("earlier word, using one attention head. The longest (green) bar is the")
print(f'word BERT ties "{pronoun}" to.')
print("Close the chart window to continue.\n")
plot_attention(sentences, pronoun=pronoun, path=HERE / "my_attention.png")
for i, sentence in enumerate(sentences, start=1):
    print(f'Chart {i + 1} (my_attention_votes_{i}.png): all 144 of BERT\'s heads vote')
    print(f'on which word "{pronoun}" pays the most attention to, in:')
    print(f'  "{sentence}"')
    print("The green bar got the most votes. Close the chart window to continue.\n")
    plot_attention_votes(sentence, word=pronoun,
                         path=HERE / f"my_attention_votes_{i}.png")
