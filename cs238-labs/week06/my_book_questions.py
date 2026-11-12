"""Week 6 · Task 2: your own questions about the two sections.

Write two questions the sections answer and one they never cover, then run:
    uv run my_book_questions.py
"""
from pathlib import Path
from genai import DocumentStore, chunk, rag, show_grounded

questions = [
    "Why does a high temperature make the output more varied?",   # ← yours
    "What is one-shot prompting?",                                 # ← yours
    "What is a vector database?",                                  # ← not covered
]

text = (Path(__file__).parent / "my_prompting_sections.txt").read_text()
if not text.strip():
    raise SystemExit("my_prompting_sections.txt is empty. Paste the two Prompting "
                     "sections back in (see the README).")

store = DocumentStore()
for piece in chunk(text, size=80, overlap=20):
    store.add(piece)

print("For each question: the model's answer, built only from the 3 retrieved")
print("chunks. Each [1], [2], [3] in an answer points to a source below it.")
for question in questions:
    print(f"\n── Question: {question}\n")
    sources = store.search(question)
    show_grounded(rag(question, sources), sources)
