"""Week 4 · Part 4: semantic search, the chapter's demo.

Run from this folder:  uv run search.py
"""
from genai import semantic_search

corpus = [
    "Neural networks learn patterns from data",
    "Machine learning powers modern AI systems",
    "The chef simmered the tomato sauce for an hour",
    "Fresh basil and garlic make the pasta fragrant",
    "The telescope captured a distant spiral galaxy",
    "A rocket launched toward the moon at dawn",
]

print("Searching six sentences by meaning, not by matching words.")
for query in ["artificial intelligence", "dinner"]:
    print(f"\nThe 3 closest sentences to '{query}':")
    for rank, doc in enumerate(semantic_search(query, corpus), start=1):
        print(f"   {rank}. {doc}")
