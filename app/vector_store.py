import faiss
import numpy as np
import os
import pickle

from app.config import VECTOR_PATH

os.makedirs(VECTOR_PATH,exist_ok=True)


def store_vectors(chunks,embeddings):

    dimension=len(embeddings[0])

    index=faiss.IndexFlatL2(dimension)

    embeddings_array=np.array(embeddings)

    index.add(embeddings_array)

    faiss.write_index(index,f"{VECTOR_PATH}/index.faiss")

    with open(f"{VECTOR_PATH}/chunks.pkl","wb") as f:

        pickle.dump(chunks,f)


def load_vector_store():

    index=faiss.read_index(f"{VECTOR_PATH}/index.faiss")

    with open(f"{VECTOR_PATH}/chunks.pkl","rb") as f:

        chunks=pickle.load(f)

    return index,chunks