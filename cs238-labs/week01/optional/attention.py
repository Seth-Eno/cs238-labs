"""Week 1 · Optional: paying attention, the chapter's BERT demo.

Needs BERT first:  uv run optional/download_bert.py
Then run:          uv run optional/attention.py
"""
from pathlib import Path
from genai.viz import plot_attention, plot_attention_votes

HERE = Path(__file__).parent

# One word changes, and "it" points somewhere else
print('Chart 1 (attention_it.png): how much the word "it" looks back at each')
print("earlier word, in two sentences that differ by one word. The longest")
print('(green) bar is the word BERT ties "it" to.')
print("Close the chart window to continue.\n")
plot_attention([
    "The cat sat on the laptop because it was tired.",
    "The cat sat on the laptop because it was warm.",
], pronoun="it", path=HERE / "attention_it.png")

# All 144 of BERT's heads vote on what "standing" attends to most
print('Chart 2 (attention_standing.png): BERT has 144 attention "heads".')
print('Each one votes for the word that "standing" pays the most attention to.')
print("The bars count the votes; the green bar is the winner.")
print("Close the chart window to finish.")
plot_attention_votes("She opened the door and saw a man standing.",
                     word="standing",
                     path=HERE / "attention_standing.png")
