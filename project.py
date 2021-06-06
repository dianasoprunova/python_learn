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
text = ' ' 
text = r.recognize_google(audio, language ='ru-RU')
#print(r.recognize_google(audio, language ='ru-RU'))
#print(c)

with open('q.txt', 'w') as f:
    f.write(text)

f=open('q.txt','r') # cчитываю файл
line=f.readline().lower()

while line:
    line=line.split()    
    s={}
    i1=0
    i2=''
    q=0
    t=[]
    min1=0
    for i in line: 
        if i not in s:  
            s[i]=1
        else:
            s[i]+=1
    for values in s.values(): 
        if values>i1:
            i1=values
    for keys , values in s.items():
        if values==i1:
            min1=keys
    for keys , values in s.items(): 
        if values==i1:               
            if min1>keys:
                min1=keys
    print(min1,i1)
    line=f.readline().lower()
f.close()

