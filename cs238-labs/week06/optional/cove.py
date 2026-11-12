"""Week 6 · Optional: chain-of-verification, the chapter's demo.

On Portugal, checking each claim on its own fixes the draft; on Brazil, it
throws away correct answers. Run from the week06 folder:
    uv run optional/cove.py
"""
from genai import show_cove

print("Chain-of-verification (CoVe). The model lists a country's neighbors,")
print("then checks each name on its own with a yes/no question, without seeing")
print("its first list. Names that fail the check are dropped ('drop'), the rest")
print("are kept ('keep'), and the revised list is shown at the end with how many")
print("names were right.\n")
print("═══ Portugal\n")
show_cove("Portugal")
print("\n═══ Brazil\n")
show_cove("Brazil")
