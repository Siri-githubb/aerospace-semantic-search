import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "../data/faiss.index"
DATA_PATH = "../data/chunk_data.npy"

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(INDEX_PATH)
chunk_data = np.load(DATA_PATH, allow_pickle=True)

query = input("Enter your aerospace query: ")

query_embedding = model.encode([query])
D, I = index.search(query_embedding, k=3)

print("\n🔍 Top Relevant Results:\n")
for rank, idx in enumerate(I[0], start=1):
    item = chunk_data[idx]
    print(f"Result {rank}")
    print(f"Source: {item['doc']} | Page: {item['page']}")
    print("-" * 50)
    print(item['text'][:800])   # show text
    print("=" * 80)
