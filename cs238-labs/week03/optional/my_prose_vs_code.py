"""Week 3 · Optional: prose versus code (Tokens Exercise 3).

Put a paragraph of English and a Python snippet of about the same length on
screen in the marked strings. Predict which costs more, then run from the
week03 folder:  uv run optional/my_prose_vs_code.py
"""
from genai import count_tokens

prose = ("Tokenization is the very first thing that happens to your text "     # ← yours
         "before a language model ever sees it, the step that chops words "
         "and code into the units a model reads.")

code = '''def first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None
'''                                                                              # ← yours

print("How many tokens each text costs. More characters per token means the")
print("tokenizer packs that kind of text more efficiently.\n")
for label, text in [("Prose", prose),
                     ("Code indented with spaces", code),
                     ("Code indented with tabs", code.replace("    ", "\t"))]:
    n = count_tokens(text)
    print(f"{label}:")
    print(f"   {len(text)} characters, {n} tokens, {len(text) / n:.1f} characters per token")
