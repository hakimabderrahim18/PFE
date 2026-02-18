from meta_model import Procedure

def validate_procedure(proc: Procedure):
    errors = []

    if len(proc.documents) == 0 or all(doc.name.strip() == "" for doc in proc.documents):
        errors.append("La procédure doit contenir au moins un document")
    if len(proc.steps) == 0 or all(step.description.strip() == "" for step in proc.steps):
        errors.append("La procédure doit contenir au moins une étape")
    if len(proc.intents) == 0 or all(intent.name.strip() == "" for intent in proc.intents):
        errors.append("La procédure doit contenir au moins une intention")
    if len(proc.responses) == 0 or all(resp.text.strip() == "" for resp in proc.responses):
        errors.append("La procédure doit contenir au moins une réponse")

    return errors
