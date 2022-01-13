
import speech_recognition

# obtain audio from the mic
recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# recognize speech using Google Speech Recognition
print("You said:")
print(recognizer.recognize_google(audio))

