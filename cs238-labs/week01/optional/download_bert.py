"""Week 1 · Optional: download BERT (about 420 MB, one time only).

Run from the week01 folder:  uv run optional/download_bert.py
"""
from transformers import BertModel, BertTokenizer

print("Downloading BERT (about 420 MB). This only happens once...")
BertTokenizer.from_pretrained("bert-base-uncased")
BertModel.from_pretrained("bert-base-uncased")
print("BERT is downloaded. You can now run optional/attention.py.")
