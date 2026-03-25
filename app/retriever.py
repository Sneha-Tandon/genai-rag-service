import numpy as np

from app.embeddings import get_model
from app.vector_store import load_vector_store


def retrieve_chunks(query,top_k=5):

    index,chunks=load_vector_store()

    model=get_model()

    query_embedding=model.encode([query])

    distances,indices=index.search(query_embedding,top_k)

    results=[]

    for score,i in zip(distances[0],indices[0]):

        if score<1.5:   

            results.append(chunks[i])

    return results