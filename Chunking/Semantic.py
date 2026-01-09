import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Download tokenizer (run once)
nltk.download("punkt")

# -----------------------------
# Long text input
# -----------------------------
text = """
Artificial Intelligence is transforming modern technology. It is widely used in healthcare for disease detection
and drug discovery. Doctors rely on AI-powered tools to analyze medical images accurately.

Machine learning is a subset of AI that focuses on learning from data. Supervised learning requires labeled datasets,
while unsupervised learning works with unlabeled data. Deep learning is a branch of machine learning that uses neural networks.

Climate change is one of the biggest global challenges today. Rising temperatures are causing glaciers to melt.
Governments around the world are investing in renewable energy sources like solar and wind power.

Renewable energy reduces carbon emissions and helps fight global warming. Solar panels and wind turbines are now
more affordable and efficient than ever before.
"""

# -----------------------------
# Step 1: Sentence Tokenization
# -----------------------------
sentences = sent_tokenize(text)

# -----------------------------
# Step 2: Generate Embeddings
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")
print(model)
embeddings = model.encode(sentences)
print(embeddings)
# -----------------------------
# Step 3: Semantic Chunking
# -----------------------------
chunks = []
current_chunk = [sentences[0]]

SIMILARITY_THRESHOLD = 0.65

for i in range(1, len(sentences)):
    sim = cosine_similarity(
        [embeddings[i - 1]],
        [embeddings[i]]
    )[0][0]

    if sim >= SIMILARITY_THRESHOLD:
        current_chunk.append(sentences[i])
    else:
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]

chunks.append(" ".join(current_chunk))

# -----------------------------
# Step 4: Output Chunks
# -----------------------------
for idx, chunk in enumerate(chunks, 1):
    print(f"\n--- Chunk {idx} ---")
    print(chunk)