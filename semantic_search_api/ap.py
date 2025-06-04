import httpx
import numpy as np
from numpy.linalg import norm
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
API_KEY = os.getenv("OPENAI_API_KEY")  
url = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
app= FastAPI()

# create similarity endpoint
@app.post("/similarity")

# function to get top matches based on cosine similarity
def get_top_match(docs: list[str], query: str, top_k: int = 3):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-embedding-3-small",
        "input": docs + [query]
    }

    # Send request to OpenAI
    response = httpx.post(url, headers=headers, json=data, timeout=30.0)
    result = response.json()
    
    # Extract embeddings from the response
    embeddings = result['data']
    doc_embeddings = [item['embedding'] for item in embeddings[:-1]]  # All except last (docs)
    query_embedding = embeddings[-1]['embedding']  # Last one is the query
    
    # Calculate cosine similarities
    similarities = []
    for i, doc_embedding in enumerate(doc_embeddings):
        # Cosine similarity calculation
        cos_sim = np.dot(query_embedding, doc_embedding) / (norm(query_embedding) * norm(doc_embedding))
        similarities.append((i, cos_sim))
    
    # Sort by similarity score (descending order)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Get top_k matches in order
    sorted_docs = [docs[i] for i, _ in similarities[:top_k]]
    
    return {
        "matches": sorted_docs
    }

ç

