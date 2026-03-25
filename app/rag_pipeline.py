from app.logger import logger
from app.memory import get_context, add_to_history


def rag_query(question, session_id=None):

    try:

        # Lazy imports (important for cloud memory)
        from app.retriever import retrieve_chunks
        from app.llm import generate_answer

        logger.info(f"Query received: {question}")

        chunks = retrieve_chunks(question)

        logger.info(f"Chunks retrieved: {len(chunks)}")

        if len(chunks) == 0:

            return "No relevant information found", []

        # Get conversation history if session exists
        context = ""

        if session_id:

            context = get_context(session_id)

        # Combine history + question
        full_query = context + "\nUser Question: " + question

        answer = generate_answer(full_query, chunks)

        logger.info("Answer generated")

        # Store conversation history
        if session_id:

            add_to_history(session_id, question, answer)

        return answer, chunks

    except Exception as e:

        logger.error(str(e))

        return str(e), []