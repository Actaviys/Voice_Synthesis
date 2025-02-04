import pyttsx3

eng = pyttsx3.init()

eng.setProperty("rate", 150)
eng.setProperty("volume", 0.9)

texts = "Hello Dima"

print(texts)
eng.say(text=texts)

eng.runAndWait()

# # Привіт Діма. Як твої справи?