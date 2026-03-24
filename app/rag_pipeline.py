from app.retriever import retrieve_chunks
from app.llm import generate_answer
from app.logger import logger


def rag_query(question):

    try:

        logger.info(f"Query received: {question}")

        chunks=retrieve_chunks(question)

        logger.info(f"Chunks retrieved: {len(chunks)}")

        if len(chunks)==0:

            logger.warning("No relevant chunks found")

            return "No relevant information found",[]

        answer=generate_answer(question,chunks)

        logger.info("Answer generated successfully")

        return answer,chunks

    except Exception as e:

        logger.error(f"RAG error: {str(e)}")

        return str(e),[]