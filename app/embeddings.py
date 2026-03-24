from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

model = None


def get_model():

    global model

    if model is None:

        model = SentenceTransformer(EMBEDDING_MODEL)

    return model


def create_embeddings(chunks):

    embedding_model = get_model()

    embeddings = embedding_model.encode(chunks)

    return embeddings