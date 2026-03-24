from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_SIZE
from app.config import CHUNK_OVERLAP


def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_text(text)

    return chunks