"""Week 4 · Task 5: a semantic search you can fool (the chapter's Exercise 5).

Replace the corpus with six to eight sentences of your own on two or three
topics, then set the two queries on the marked lines. Run:
    uv run my_search.py
"""
from genai import semantic_search

corpus = [                                                   # ← your sentences
    "strike out",
    "He hit the ball",
    "What uses echolocation to eat bugs?",
    "Don't go in the cave, you might get bit",
    "I popped a tire on my bike",
    "Want to go for a ride this afternoon",
]
finds_it = "baseball"                                    # ← your query
fools_it = "flying bat"                                   # ← your tricky query

print("Searching your sentences by meaning, not by matching words.")
for kind, query in [("your query", finds_it), ("your tricky query", fools_it)]:
    print(f"\nThe 3 closest sentences to {kind}, '{query}':")
    for rank, doc in enumerate(semantic_search(query, corpus), start=1):
        print(f"   {rank}. {doc}")
