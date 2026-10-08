# RoboGuide — Rule-Based AI Chatbot

RoboGuide is a beginner-friendly conversational chatbot developed in Python using **deterministic rule-based logic**. It maps user inputs to predefined intents and responses using input sanitization, exact phrase matching, keyword rules, and a dictionary-based knowledge base.

The project demonstrates introductory AI and Python programming without machine learning, large language models, external APIs, or third-party packages.

## Objective

Build a simple conversational system that can recognize common intents, respond to predefined questions, handle different phrasings, continue a conversation, and provide a fallback for unsupported inputs.

## Features

- 15+ conversational intents
- Greeting and farewell handling
- Help and capability commands
- Identity and creator responses
- Basic conversational responses
- Date and time responses
- Python, AI, and rule-based-system explanations
- Exact phrase and keyword matching
- Input sanitization with `lower()`, `strip()`, whitespace normalization, and punctuation cleanup
- Lightweight session context with turn count and last intent
- Empty-input handling
- Keyboard interruption and EOF handling
- Deterministic fallback response
- Built-in lightweight tests
- No external Python packages required

## How the Rule-Based System Works

RoboGuide does not learn from data. Its behavior is explicitly defined by rules.

```text
User Input
    ↓
Input Sanitization
    ↓
Exit Command Check
    ↓
Exact Phrase Matching
    ↓
Keyword Matching
    ↓
Intent Detection
    ↓
Response Generation
    ↓
Update Session Context
    ↓
Display Response
    ↓
Continue / Exit
```

The system normalizes input, checks for exit commands, tries exact phrase rules, then keyword rules. If nothing matches, it returns a fallback response.

## Technologies Used

- **Python 3**
- Python standard library: `datetime`, `re`, `typing`
- No external packages

## Project Structure

```text
RoboGuide/
├── chatbot.py
├── README.md
├── sample_output.txt
└── tests/
    └── test_chatbot.py
```

## Installation

1. Install Python 3.
2. Open a terminal in the project directory.
3. No package installation is required because the project uses the Python standard library.

## How to Run

```bash
python chatbot.py
```

Try commands such as:

```text
hello
what is your name?
how are you?
what can you do?
tell me the time
what is Python?
what is artificial intelligence?
what is a rule-based system?
help
thank you
bye
```

## Example Conversation

```text
You: hello
RoboGuide: Hello! 👋 I'm RoboGuide. How can I help you?

You: what is your name?
RoboGuide: I'm RoboGuide, a rule-based AI chatbot built with Python.

You: what can you do?
RoboGuide: I can handle greetings, basic questions, help requests, thanks, simple conversation, and common chatbot commands.

You: what is quantum computing?
RoboGuide: I'm sorry, I don't understand that yet. Try 'help' to see supported topics.

You: bye
RoboGuide: Goodbye! 👋 Have a great day!
```

## Supported Intents

| Intent | Example input |
|---|---|
| Greeting | `hello`, `hi`, `hey` |
| How are you | `how are you?` |
| Identity | `what is your name?` |
| Creator | `who created you?` |
| Capabilities | `what can you do?` |
| Help | `help` |
| Thanks | `thank you` |
| Morning greeting | `good morning` |
| Afternoon greeting | `good afternoon` |
| Evening greeting | `good evening` |
| Time | `what time is it?` |
| Date | `what is today's date?` |
| Python | `what is Python?` |
| Rule-based systems | `what is a rule-based system?` |
| Artificial Intelligence | `what is AI?` |
| Project | `tell me about the project` |
| Farewell | `bye`, `exit`, `quit`, `stop` |

## Testing

The project includes lightweight assertions for important behavior.

Run:

```bash
python -c "import chatbot; chatbot.run_tests()"
```

Expected result:

```text
All chatbot tests passed.
```

An additional `tests/test_chatbot.py` file can be used with a standard test runner such as `pytest` if that is installed separately.

## Limitations

Because RoboGuide is intentionally rule-based:

- It does not learn from conversations.
- It cannot understand arbitrary natural-language questions.
- It has no external knowledge source.
- Responses are limited to predefined rules and responses.
- Session context is lightweight and is not persisted after the program closes.

These limitations are intentional because the project demonstrates deterministic rule-based AI rather than machine learning.

## Future Enhancements

1. Graphical user interface.
2. Web-based chat interface.
3. Larger intent and response knowledge base.
4. More advanced text preprocessing.
5. Sentiment-related rules.
6. Persistent conversation history.
7. Database-backed responses.
8. Separate automated test suite.
9. Comparison of rule-based and machine-learning approaches.
10. Optional NLP/ML integration as a separate advanced version.

## Learning Outcomes

This project demonstrates Python functions, dictionaries, sets, conditional statements, loops, string processing, regular expressions, exception handling, software testing, deterministic intent classification, knowledge-base design, command-line application development, and introductory AI system design.

## Author

**Student Project — Rule-Based AI Chatbot**

Developed as an educational demonstration of rule-based conversational AI using Python.
