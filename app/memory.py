sessions = {}


def get_history(session_id):

    if session_id not in sessions:

        sessions[session_id] = []

    return sessions[session_id]


def add_to_history(session_id, question, answer):

    if session_id not in sessions:

        sessions[session_id] = []

    sessions[session_id].append({

        "question": question,

        "answer": answer

    })


def get_context(session_id, limit=3):

    history = sessions.get(session_id, [])

    context = ""

    for item in history[-limit:]:

        context += f"User: {item['question']}\nAssistant: {item['answer']}\n"

    return context


def list_sessions():

    return list(sessions.keys())