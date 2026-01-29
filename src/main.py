def detect_intent(text):
    text = text.lower()
    if "apply" in text:
        return "application"
    if "eligible" in text:
        return "eligibility"
    if "deadline" in text:
        return "deadline"
    return "general"

def generate_response(intent):
    responses = {
        "application": "You can apply through the official internship portal.",
        "eligibility": "Eligibility depends on year and skill requirements.",
        "deadline": "Deadlines vary by internship. Check the listing.",
        "general": "I can help with internships, eligibility, and deadlines."
    }
    return responses[intent]

def run_bot():
    print("MoltBot Starter (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        intent = detect_intent(user_input)
        response = generate_response(intent)
        print("Bot:", response)

if __name__ == "__main__":
    run_bot()
