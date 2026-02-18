from difflib import get_close_matches

def ask_question(question: str, chatbot_json: dict):
    for intent in chatbot_json.get("intents", []):
        match = get_close_matches(
            question.lower(),
            [u.lower() for u in intent.get("utterances", [])],
            n=1,
            cutoff=0.6
        )
        if match:
            if chatbot_json.get("responses"):
                return chatbot_json["responses"][0]
    return "Je n'ai pas compris. Pouvez-vous reformuler ?"
