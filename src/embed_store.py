import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

CHUNK_DIR = "../data/chunks"
INDEX_PATH = "../data/faiss.index"
DATA_PATH = "../data/chunk_data.npy"

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []
chunk_data = []

for file in sorted(os.listdir(CHUNK_DIR)):
    if file.endswith(".txt"):
        with open(os.path.join(CHUNK_DIR, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
            page = lines[0].replace("PAGE:", "").strip()
            text = "".join(lines[1:]).strip()

            texts.append(text)
            chunk_data.append({
                "doc": "pwt_turbine_blade_thermal_fatigue.pdf",
                "page": page,
                "text": text
            })

embeddings = model.encode(texts, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, INDEX_PATH)
np.save(DATA_PATH, chunk_data)

print("✅ Embeddings + text + metadata stored successfully")
