import pyttsx3

engine = pyttsx3.init()
name = input("What is your name? ")
engine.say(f"Hello {name}")
engine.runAndWait()

text = input("Say something! ")
engine.say(text)
engine.runAndWait()
