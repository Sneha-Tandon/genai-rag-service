sessions={}


def get_history(session_id):

    if session_id not in sessions:

        sessions[session_id]=[]

    return sessions[session_id]


def add_to_history(session_id,question,answer):

    sessions[session_id].append({

        "question":question,

        "answer":answer

    })


def get_context(session_id,limit=3):

    history=sessions.get(session_id,[])

    context=""

    for item in history[-limit:]:

        context+=f"Q:{item['question']}\nA:{item['answer']}\n"

    return context