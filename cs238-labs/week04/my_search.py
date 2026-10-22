"""Week 4 · Task 5: a semantic search you can fool (the chapter's Exercise 5).

Replace the corpus with six to eight sentences of your own on two or three
topics, then set the two queries on the marked lines. Run:
    uv run my_search.py
"""
from genai import semantic_search

corpus = [                                                   # ← your sentences
    "The Seahawks won in overtime on a last-second field goal",
    "Our soccer team practices twice a week at the park",
    "Sourdough needs a starter that has been fed for days",
    "The croissants came out flaky and golden",
    "Our cat naps in the sunniest spot in the house",
    "The puppy chewed through another shoe this morning",
]
finds_it = "bread baking"                                    # ← your query
fools_it = "football club"                                   # ← your tricky query

print("Searching your sentences by meaning, not by matching words.")
for kind, query in [("your query", finds_it), ("your tricky query", fools_it)]:
    print(f"\nThe 3 closest sentences to {kind}, '{query}':")
    for rank, doc in enumerate(semantic_search(query, corpus), start=1):
        print(f"   {rank}. {doc}")
