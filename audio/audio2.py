import pyttsx3

engine = pyttsx3.init()

# Customize voice, rate, and volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
engine.setProperty('rate', 150)  # Slow down the speech
engine.setProperty('volume', 0.9)  # Set volume to 90%

# Speak the text
engine.say("Hello, Jyotirmaya Behera. Welcome to Python programming.")
engine.runAndWait()
