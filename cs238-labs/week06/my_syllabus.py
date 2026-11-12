"""Week 6 · Part 5: ask my syllabus (the chapter's Exercise 5).

Reads my_syllabus.txt (the course website comes with the lab; paste in your
own document if you like), chunks it, and answers each question using ONLY
what it retrieves, with citations. Replace the questions with five you care
about, including one whose answer isn't in the document.
Run from this folder:  uv run my_syllabus.py
"""
from pathlib import Path
from genai import DocumentStore, ask, chunk, show_grounded

questions = [                                    # ← your five questions
    "What am I allowed to use generative ai for?",
    "Where does the class meet?",
    "What grade weight do quizzes have?",
    "What is unique about week 10's quiz?",
    "What is a study habit that will help me succeed?",    # ← not in there!
]

text = (Path(__file__).parent / "my_syllabus.txt").read_text()
if not text.strip():
    raise SystemExit("my_syllabus.txt is empty. Paste a document into it "
                     "(see the README).")

store = DocumentStore()
for piece in chunk(text, size=60, overlap=15):
    store.add(piece)

def grounded_rag(question, store, k=3):
    sources = store.search(question, k=k)
    context = "\n\n".join(f"[{i+1}] {d}" for i, d in enumerate(sources))
    prompt = ("Answer using ONLY the numbered sources below. "
              "Cite with [1], [2] etc. If the answer isn't in the "
              f"sources, say you don't know.\n\n{context}\n\n"
              f"Question: {question}")
    return ask(prompt, max_tokens=150, system=None), sources

print("For each question: the model's answer, built only from the 3 retrieved")
print("pieces of your document. Each [1], [2], [3] in an answer points to a")
print("source listed below it.")
for question in questions:
    answer, sources = grounded_rag(question, store)
    print(f"\n── Question: {question}\n")
    show_grounded(answer, sources)
