import speech_recognition as sr

c = []
p=' ' 
r = sr.Recognizer ()
harvard = sr.AudioFile('golos.wav')
with harvard as source:
    audio = r.record(source)
#print(type(audio))     # <class 'speech_recognition.AudioData'>
с=list(r.recognize_google(audio, language ='ru-RU'))
#print(r.recognize_google(audio, language ='ru-RU'))

for i, letter in enumerate((r.recognize_google(audio, language ='ru-RU'))):
    if letter !=' ':
        p = p + str(letter)
    else:
        c.append(p)
        p = ' '
c.append(p)        
print(c)
