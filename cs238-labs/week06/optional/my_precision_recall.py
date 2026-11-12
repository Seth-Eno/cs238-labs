"""Week 6 · Optional: precision and recall by hand (the chapter's Exercise 4).

Write six short documents, mark which ones are relevant to your query, and
compare retrieving the top 3 with the top 5. Run from the week06 folder:
    uv run optional/my_precision_recall.py
"""
from genai import DocumentStore

query = "how to care for a houseplant"                    # ← your query
docs = {                                                   # ← your documents: relevant?
    "Water most succulents only when the soil is dry.": True,
    "Ferns like humid air and indirect light.": True,
    "Repot a plant when its roots circle the pot.": True,
    "The bus to campus leaves every twenty minutes.": False,
    "Tomatoes grow best in full summer sun.": False,
    "Our cat likes to chew on leaves.": False,
}

store = DocumentStore()
for d in docs:
    store.add(d)
relevant = sum(docs.values())

print(f"Search: '{query}'")
print("Precision = how many of the results are relevant.")
print(f"Recall    = how many of the {relevant} relevant documents were found.")
for k in [3, 5]:
    hits = store.search(query, k=k)
    found = sum(docs[h] for h in hits)
    print(f"\n── Top {k} results:")
    for h in hits:
        print(f"   {'relevant    ' if docs[h] else 'NOT relevant'}  {h}")
    print(f"   Precision: {found} of {k} results are relevant ({found / k:.0%})")
    print(f"   Recall:    found {found} of the {relevant} relevant documents "
          f"({found / relevant:.0%})")
