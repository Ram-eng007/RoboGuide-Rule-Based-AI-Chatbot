import chatbot

def test_sanitize_input():
    assert chatbot.sanitize_input("  HELLO!!! ") == "hello"

def test_greeting():
    assert chatbot.get_intent("hello") == "greeting"

def test_phrase_matching():
    assert chatbot.get_intent("What is your name?") == "name"

def test_keyword_matching():
    assert chatbot.get_intent("Can you tell me the time?") == "time"

def test_fallback():
    assert chatbot.get_intent("Explain quantum computing") == "fallback"

def test_exit():
    assert chatbot.get_intent("bye") == "goodbye"
