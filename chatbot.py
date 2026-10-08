"""RoboGuide - Rule-Based AI Chatbot."""
from datetime import datetime
import re
from typing import Dict, List, Tuple

RESPONSES: Dict[str, str] = {
    "greeting": "Hello! 👋 I'm RoboGuide. How can I help you?",
    "how_are_you": "I'm running perfectly and ready to chat! 🤖",
    "name": "I'm RoboGuide, a rule-based AI chatbot built with Python.",
    "creator": "I was created as a Python rule-based chatbot project.",
    "capabilities": "I can handle greetings, basic questions, help requests, thanks, simple conversation, and common chatbot commands.",
    "help": "You can try: hello, what is your name?, how are you?, what can you do?, tell me the time, tell me the date, thank you, or bye.",
    "thanks": "You're welcome! 😊",
    "good_morning": "Good morning! ☀️ Hope you have a great day.",
    "good_afternoon": "Good afternoon! 🌤️ How can I help you?",
    "good_evening": "Good evening! 🌆 What would you like to know?",
    "time": "The current time is {time}.",
    "date": "Today's date is {date}.",
    "python": "Python is a high-level programming language known for its readability and wide range of applications.",
    "rule_based": "A rule-based system uses predefined rules to map user inputs to responses. RoboGuide uses explicit conditions and a knowledge base.",
    "ai": "Artificial Intelligence is the field of building systems that perform tasks that normally require human-like intelligence.",
    "project": "This project demonstrates a simple rule-based conversational system using Python, condition checks, and a response knowledge base.",
    "goodbye": "Goodbye! 👋 Have a great day!",
}

EXIT_COMMANDS = {"bye", "goodbye", "exit", "quit", "stop"}
INTENT_PHRASES: Dict[str, set] = {
    "greeting": {"hello", "hi", "hey", "hello there", "hi there", "hey there"},
    "how_are_you": {"how are you", "how are you doing", "how's it going"},
    "name": {"name", "your name", "what is your name", "what's your name"},
    "creator": {"who created you", "who made you", "who built you"},
    "capabilities": {"what can you do", "your capabilities", "what do you do"},
    "help": {"help", "help me", "commands", "options"},
    "thanks": {"thanks", "thank you", "thx", "thanks a lot"},
    "good_morning": {"good morning"}, "good_afternoon": {"good afternoon"},
    "good_evening": {"good evening"},
    "time": {"time", "what time is it", "tell me the time", "current time"},
    "date": {"date", "what is the date", "today's date", "tell me the date"},
    "python": {"python", "what is python"},
    "rule_based": {"rule based", "rule-based", "what is a rule based system"},
    "ai": {"ai", "artificial intelligence", "what is ai"},
    "project": {"project", "tell me about the project"},
}
KEYWORD_INTENTS: List[Tuple[str, Tuple[str, ...]]] = [
    ("name", ("your name", "who are you")), ("creator", ("created you", "made you", "built you")),
    ("capabilities", ("what can you do", "capabilities")), ("how_are_you", ("how are you", "how's it going")),
    ("thanks", ("thank", "thanks")), ("help", ("help", "commands")),
    ("time", ("what time", "current time")), ("date", ("what date", "today's date", "todays date")),
    ("python", ("python",)), ("rule_based", ("rule based", "rule-based")),
    ("ai", ("artificial intelligence",)), ("project", ("project",)),
]


def sanitize_input(user_input: str) -> str:
    """Normalize user input for deterministic matching."""
    if not isinstance(user_input, str):
        return ""
    cleaned = user_input.lower().strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return re.sub(r"[!?.,]+$", "", cleaned)


def get_intent(user_input: str) -> str:
    """Detect an intent using exit, exact-phrase, then keyword rules."""
    text = sanitize_input(user_input)
    if not text:
        return "empty"
    if text in EXIT_COMMANDS:
        return "goodbye"
    for intent, phrases in INTENT_PHRASES.items():
        if text in phrases:
            return intent
    for intent, keywords in KEYWORD_INTENTS:
        if any(keyword in text for keyword in keywords):
            return intent
    return "fallback"


def generate_response(intent: str) -> str:
    """Generate a response for a detected intent."""
    if intent == "empty":
        return "Please type a message. Try 'help' to see what I can do."
    if intent == "fallback":
        return "I'm sorry, I don't understand that yet. Try 'help' to see supported topics."
    if intent == "time":
        return RESPONSES[intent].format(time=datetime.now().strftime("%I:%M %p"))
    if intent == "date":
        return RESPONSES[intent].format(date=datetime.now().strftime("%d %B %Y"))
    return RESPONSES[intent]


def update_context(context: Dict[str, object], intent: str) -> None:
    """Store lightweight session-level information."""
    context["last_intent"] = intent
    context["turn_count"] = int(context.get("turn_count", 0)) + 1


def print_banner() -> None:
    """Display the terminal interface."""
    print("=" * 62)
    print("                 ROBOGUIDE")
    print("          Rule-Based AI Chatbot")
    print("=" * 62)
    print("Type 'help' for supported topics.")
    print("Type 'bye', 'exit', 'quit', or 'stop' to end the chat.")
    print("-" * 62)


def run_chatbot() -> None:
    """Run the chatbot until an exit command is received."""
    context: Dict[str, object] = {"last_intent": None, "turn_count": 0}
    print_banner()
    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nRoboGuide: Goodbye! 👋")
            break
        intent = get_intent(user_input)
        update_context(context, intent)
        print(f"RoboGuide: {generate_response(intent)}")
        if intent == "goodbye":
            break


def run_tests() -> None:
    """Run lightweight built-in checks for core behavior."""
    assert sanitize_input("  HELLO!!! ") == "hello"
    assert get_intent("hello") == "greeting"
    assert get_intent("WHAT IS YOUR NAME?") == "name"
    assert get_intent("tell me the time") == "time"
    assert get_intent("this is completely unknown") == "fallback"
    assert get_intent("bye") == "goodbye"
    assert "Please type" in generate_response("empty")
    print("All chatbot tests passed.")


if __name__ == "__main__":
    run_chatbot()
