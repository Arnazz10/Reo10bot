
import datetime
import random

def sample_responses(text):
    text = text.lower()

    greetings = ["hi", "hello", "hey", "yo", "sup"]
    if any(word in text for word in greetings):
        return random.choice(["Hey there! 😊", "Hello! How’s your day going?", "Hi! I’m Reo10bot. Here for you."])

    if "how are you" in text:
        return "I'm a bot, but I feel great when you're around! 😄"

    if "who are you" in text:
        return "I'm Reo10bot — your always-on digital buddy and chat partner! 🤖"

    if "sad" in text or "depressed" in text:
        return "I'm sorry to hear that 💔. I'm here to talk if you need anything. Want a joke or quote?"

    if "thank" in text:
        return "You're always welcome! 🤗"

    if "love" in text:
        return "Aww, sending digital hugs your way! ❤️"

    return "I'm still learning. Try asking me something else or use a command like /motivate or /joke!"
