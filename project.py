import speech_recognition as sr


r = sr.Recognizer ()
harvard = sr.AudioFile('my_audio.wav')
with harvard as source:
    audio = r.record(source)
print(type(audio))     # <class 'speech_recognition.AudioData'>
print(r.recognize_google(audio))
