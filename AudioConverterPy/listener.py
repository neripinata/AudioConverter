import speech_recognition as sr

def AudioToTxt():
    r = sr.Recognizer()
    f = open("info.txt", "w+")

    song = sr.AudioFile('fuente.wav')

    with song as source:
        audio = r.record(source)

    f.write(r.recognize_google(audio))