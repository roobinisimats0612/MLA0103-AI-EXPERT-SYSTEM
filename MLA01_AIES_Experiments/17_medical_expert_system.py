"""Educational symptom-rule demo only; not a diagnostic tool."""
RULES = [
    ({"fever", "cough"}, "Fever and cough can have several causes; consider professional medical advice."),
    ({"sneezing", "runny nose"}, "Symptoms may occur with allergies or a cold; seek advice if concerned."),
    ({"headache", "fever"}, "Fever with headache has many possible causes; seek prompt advice if severe.")
]

def infer(symptoms):
    facts = {s.strip().lower() for s in symptoms if s.strip()}
    results = [message for conditions, message in RULES if conditions <= facts]
    return results or ["No rule matched. This program cannot diagnose illness."]

if __name__ == "__main__":
    symptoms = input("Enter symptoms separated by commas: ").split(",")
    for result in infer(symptoms):
        print(result)
