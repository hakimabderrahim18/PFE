from meta_model import Procedure

def generate_chatbot(proc: Procedure):
    chatbot = {
        "procedure": proc.name,
        "intents": [],
        "responses": []
    }

    for intent in proc.intents:
        chatbot["intents"].append({
            "name": intent.name,
            "utterances": intent.utterances
        })

    for resp in proc.responses:
        chatbot["responses"].append(resp.text)

    return chatbot
