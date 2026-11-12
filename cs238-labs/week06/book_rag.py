"""Week 6 · Part 2: your first RAG system.

Reads my_prompting_sections.txt (two sections of the Prompting chapter; a copy
comes with the lab), splits it into chunks, loads them into a DocumentStore
(which embeds each one), and answers from whatever it retrieves.
Run from this folder:  uv run book_rag.py
"""
from pathlib import Path
from genai import DocumentStore, chunk, rag, show_grounded

text = (Path(__file__).parent / "my_prompting_sections.txt").read_text()
if not text.strip():
    raise SystemExit("my_prompting_sections.txt is empty. Paste the two Prompting "
                     "sections back in (see the README).")

chunks = chunk(text, size=80, overlap=20)   # about 80 words each, overlapping a little
print(f"Split the Prompting sections into {len(chunks)} chunks of about 80 words.")

store = DocumentStore()
for piece in chunks:
    store.add(piece)     # embeds each chunk once

question = "What does temperature do to the model's output?"
print(f"Question: {question}")
print("Retrieving the 3 chunks closest in meaning and handing them to the model.\n")
sources = store.search(question)          # retrieve the top 3
print("The model's answer (each [1], [2], [3] points to a source listed below it):\n")
show_grounded(rag(question, sources), sources)
