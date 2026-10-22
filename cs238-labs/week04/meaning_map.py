"""Week 4 · Part 1.3: a map of meaning.

Run from this folder:  uv run meaning_map.py
"""
from pathlib import Path
from genai.viz import plot_tsne_embeddings

HERE = Path(__file__).parent

word_groups = {
    "animals":  ["cat", "kitten", "dog", "puppy", "fish", "bird"],
    "vehicles": ["car", "truck", "bus", "motorcycle", "bicycle", "vehicle"],
    "fruits":   ["apple", "banana", "orange", "mango", "grape", "cherry"],
    "code":     ["python", "javascript", "java", "code", "algorithm", "software"],
}

print("Each word's embedding is 768 numbers long, far too many to draw. A")
print("technique called t-SNE squashes them down to two dimensions, keeping")
print("words that were close together still close together. The exact")
print("positions don't mean anything, but the clusters do. Each word is")
print("colored by the group we put it in:\n")
for group, words in word_groups.items():
    print(f"   {group:9} {', '.join(words)}")
print("\nThe chart is opening (also saved as meaning_map.png).")
print("Close the chart window to finish.")
plot_tsne_embeddings(word_groups, save_path=HERE / "meaning_map.png")
