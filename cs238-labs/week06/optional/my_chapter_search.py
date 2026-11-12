"""Week 6 · Optional: search a whole chapter.

optional/my_chapter.txt comes with the Augmentation chapter in it; paste in any
other chapter you've read if you like, and put your questions in the list.
Embedding a whole chapter takes a minute or two. Run from the week06 folder:
    uv run optional/my_chapter_search.py
"""
from pathlib import Path
from genai import DocumentStore, chunk, rag, show_grounded

questions = [                                           # ← your questions
    "What is the main idea of this chapter?",
    "What is hybrid search, and why use it?",
]

text = (Path(__file__).parent / "my_chapter.txt").read_text()
if not text.strip():
    raise SystemExit("optional/my_chapter.txt is empty. Paste a chapter into it.")

chunks = chunk(text, size=80, overlap=20)
print(f"Embedding {len(chunks)} chunks from your chapter...")
store = DocumentStore()
for piece in chunks:
    store.add(piece)

print("For each question: the model's answer, built only from the 3 retrieved")
print("chunks. Each [1], [2], [3] in an answer points to a source below it.")
for question in questions:
    print(f"\n── Question: {question}\n")
    sources = store.search(question)
    show_grounded(rag(question, sources), sources)
