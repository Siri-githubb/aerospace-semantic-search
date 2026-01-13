import os
import nltk
from nltk.tokenize import sent_tokenize

INPUT_PATH = "../data/text/pwt_turbine_blade_thermal_fatigue.txt"
OUTPUT_DIR = "../data/chunks"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

chunks = []
current_chunk = []
current_length = 0
current_page = None

MAX_WORDS = 350
OVERLAP_WORDS = 50

for line in lines:
    if line.startswith("--- Page"):
        current_page = int(line.replace("-", "").replace("Page", "").strip())
        continue

    sentences = sent_tokenize(line)
    for sentence in sentences:
        words = sentence.split()
        current_chunk.append(sentence)
        current_length += len(words)

        if current_length >= MAX_WORDS:
            chunks.append({
                "page": current_page,
                "text": " ".join(current_chunk)
            })

            # overlap logic
            overlap = []
            overlap_length = 0
            for sent in reversed(current_chunk):
                overlap.insert(0, sent)
                overlap_length += len(sent.split())
                if overlap_length >= OVERLAP_WORDS:
                    break

            current_chunk = overlap
            current_length = overlap_length

if current_chunk:
    chunks.append({
        "page": current_page,
        "text": " ".join(current_chunk)
    })

# Save chunks with metadata
for i, chunk in enumerate(chunks):
    chunk_path = os.path.join(OUTPUT_DIR, f"chunk_{i+1}.txt")
    with open(chunk_path, "w", encoding="utf-8") as f:
        f.write(f"PAGE:{chunk['page']}\n")
        f.write(chunk["text"])

print(f"Chunking with page numbers complete! Created {len(chunks)} chunks.")

