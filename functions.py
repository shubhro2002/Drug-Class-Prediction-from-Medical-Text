import re
import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r"[\|;/]", ",", text)
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-z0-9,\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def simple_tokenize_and_stem(text):
    tokens = text.split()
    tokens = [t for t in tokens if t not in ENGLISH_STOP_WORDS and len(t) > 1]
    tokens = [stemmer.stem(t) for t in tokens]
    return " ".join(tokens)

def parse_classes(cell):
    if pd.isna(cell) or str(cell).strip()=="":
        return []
    s = clean_text(cell)
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    final = []
    for p in parts:
        subparts = re.split(r"\band\b", p)
        for sp in subparts:
            sp = sp.strip()
            if sp:
                final.append(sp)
    final = [re.sub(r"\s+"," ",item).strip() for item in final]
    return list(dict.fromkeys(final))

