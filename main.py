"""
Mini AI Chatbot (rule-based)
Portfolio project: demonstrates basic AI logic via intent matching.
"""

from datetime import datetime
import re


def normalize_text(text: str) -> str:
    """Lowercase and remove extra spaces for reliable matching."""
    return re.sub(r"\s+", " ", text.strip().lower())


def classify_intent(user_text: str) -> str:
    """
    Classify user input into a simple intent.
    This is the "AI component": rule-based intent detection.
    """
    text = normalize_text(user_text)

    if any(word in text for word in ["hallo", "hoi", "hey", "goedemorgen", "goedenavond"]):
        return "greeting"
    if any(word in text for word in ["naam", "wie ben je", "wat ben je"]):
        return "identity"
    if any(word in text for word in ["tijd", "hoe laat"]):
        return "time"
    if any(word in text for word in ["datum", "welke dag", "vandaag"]):
        return "date"
    if any(word in text for word in ["help", "wat kan je", "mogelijkheden"]):
        return "help"
    if any(word in text for word in ["doei", "bye", "tot ziens", "stop", "exit", "quit"]):
        return "goodbye"
    return "unknown"


def generate_response(intent: str) -> str:
    """Generate chatbot response based on detected intent."""
    now = datetime.now()

    responses = {
        "greeting": "Hoi! Ik ben jouw mini AI-chatbot. Stel gerust een vraag.",
        "identity": "Ik ben een rule-based Python chatbot voor jouw schoolportfolio.",
        "time": f"Het is nu {now.strftime('%H:%M:%S')}.",
        "date": f"Vandaag is {now.strftime('%A %d-%m-%Y')}.",
        "help": (
            "Je kunt bijvoorbeeld vragen: 'Hoe laat is het?', 'Welke datum is het?', "
            "'Wie ben je?' of je kunt 'stop' typen om te afsluiten."
        ),
        "goodbye": "Bedankt! Succes met je portfolio en tot de volgende keer.",
        "unknown": (
            "Die vraag begrijp ik nog niet helemaal. "
            "Typ 'help' om te zien wat ik al kan."
        ),
    }
    return responses[intent]


def print_header() -> None:
    """Show clean terminal header."""
    print("=" * 55)
    print("   MINI AI CHATBOT - PYTHON PORTFOLIO PROJECT")
    print("=" * 55)
    print("Typ een vraag en druk op Enter. Typ 'stop' om te sluiten.\n")


def run_chatbot() -> None:
    """Main chatbot loop with basic error handling."""
    print_header()

    while True:
        try:
            user_input = input("Jij  > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot  > Sessie veilig afgesloten. Tot ziens!")
            break

        if not user_input:
            print("Bot  > Voer eerst een bericht in (niet leeg).")
            continue

        intent = classify_intent(user_input)
        response = generate_response(intent)
        print(f"Bot  > {response}")

        if intent == "goodbye":
            break


if __name__ == "__main__":
    run_chatbot()
