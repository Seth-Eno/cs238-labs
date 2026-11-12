"""Week 6 · Part 4: dense versus keyword retrieval.

Dense retrieval compares meaning; keyword (sparse) retrieval compares exact
words. Run from this folder:  uv run dense_vs_sparse.py
"""
import re
from collections import Counter
from genai import DocumentStore

STOPWORDS = {"the", "a", "an", "is", "in", "of", "for",
             "and", "or", "to", "with", "do", "i"}

def kw_score(query, text):
    """Keyword overlap: a simplified BM25."""
    terms = [w for w in re.findall(r"\w+", query.lower())
             if w not in STOPWORDS]
    counts = Counter(re.findall(r"\w+", text.lower()))
    return sum(counts[t] for t in terms) / (sum(counts.values()) or 1)

def keyword_search(query, docs):
    """The note with the most shared words, or None if no note shares any."""
    best = max(docs, key=lambda d: kw_score(query, d))
    return best if kw_score(query, best) > 0 else None

docs = [
    "Run pip install with the --upgrade flag to get the newest release.",
    "Error E1045 means the license server could not be reached.",
    "Restart the router if your laptop keeps dropping off the wifi.",
    "Back up your files before reinstalling the operating system.",
    "The fan gets loud when the processor is working hard.",
    "Clear your browser cache if pages look out of date.",
]
store = DocumentStore()
for d in docs:
    store.add(d)

searches = [
    ("A paraphrase that shares one misleading word", "why is my laptop so noisy"),
    ("A paraphrase that shares no words at all",     "websites show old versions"),
    ("Something none of the notes cover",            "my printer is jammed"),
    ("An exact error code",                          "E1045"),
]

print("Two ways to search six help-desk notes. Each shows its single best match.")
print("  Dense search:   compares meanings (embeddings).")
print("  Keyword search: counts shared words.")
for label, query in searches:
    found = keyword_search(query, docs)
    print(f"\n── {label}: '{query}'")
    print(f"   Dense search found:   {store.search(query, k=1)[0]}")
    print(f"   Keyword search found: {found or 'nothing (no shared words)'}")
