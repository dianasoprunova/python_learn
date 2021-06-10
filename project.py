import speech_recognition as sr

print(sr.Microphone.list_microphone_names())
c = [] #Пустой список для анализа в дальнейшем
p=' ' # СТрока для Дальнейший анализ 
r = sr.Recognizer () # Распознование файла
mic = sr.Microphone() # Распознавание с микро
vybor = input ('Если вы хотите обработать запись с микрофона введите 1, если вы хотите обработать запись введите 2 ')

if vybor == '1':
    with mic as audio_file:
        print("Говорите пожалуйста")
        r.adjust_for_ambient_noise(audio_file)
        audio = r.listen(audio_file)
        print("Перевожу речь в текст")
        print("Вы сказали: " + r.recognize_google(audio, language ='ru-RU'))
elif vybor == '2':
    fail = input('Введите название файла с расширением ')
    harvard = sr.AudioFile(fail)
    with harvard as source:
        audio = r.record(source)
        print(r.recognize_google(audio, language ='ru-RU'))
        '''
        с = list(r.recognize_google(audio, language ='ru-RU'))
        for i, letter in enumerate((r.recognize_google(audio, language ='ru-RU'))):
            if letter !=' ':
                p = p + str(letter)
            else:
                c.append(p)
                p = ' '
                '''
text = ' ' 
text = r.recognize_google(audio, language ='ru-RU')
#print(r.recognize_google(audio, language ='ru-RU'))
#print(c)

with open('q.txt', 'w') as f:
    f.write(text)

f=open('q.txt','r') # cчитываю файл
line=f.readline().lower()# делает все буквы маленькими. Так как для распознавания важен регистр

while line:
    line=line.split()    
    s = {}
    i1=0
    i2=''
    q=0
    t=[]
    min1=0
    for i in line:
        compressed(i)
        if i not in s and count > 2:  
            s[i]=1
        else:
            s[i]= s[i] + 1
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
