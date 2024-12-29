import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

# Define a frase
phrase = "esta frase ira se tornar um vetor de embedding"

# Define o modelo de embeddings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Gera o embedding para a frase
phrase_embedding = embeddings.embed_query(phrase)

# Mostra o tamanho do embedding
embedding_size = len(phrase_embedding)
print(f"Tamanho do embedding: {embedding_size}")

# Exibe o vetor de embedding
print(f"\nFrase: {phrase}")
print(f"Vetor de Embedding: {phrase_embedding[:10]}\n")
