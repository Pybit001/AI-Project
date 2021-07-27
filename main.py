### Hello ###

### Name of AI is under development ###

### AI itself is under development ###

# There are resources for voice recognition and speech #
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak():
    engine.say("abc")
    engine.runAndWait()


speak()
