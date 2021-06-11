import speech_recognition as sr
import os

# print(sr.Microphone.list_microphone_names())
search_dir = 'audio'
c = []
p=' ' 
r = sr.Recognizer ()
# mic = sr.Microphone()
my_files = []

# определение ключевого слова для поиска
word = input('Введите слово или его часть для поиска ')
vybor = input ('если вы хотите обработать запись с микрофона введите 1, если вы хотите обработать запись введите 2 ')
# запись и распознавание через микрофон
if vybor == '1':
    with mic as audio_file:
        print("Speak Please")
        r.adjust_for_ambient_noise(audio_file)
        audio = r.listen(audio_file)
        print("Преобразование речи в текст...")
        print("Вы сказали: " + r.recognize_google(audio, language ='ru-RU'))
# Разпознавание речи из аудиофайлов
elif vybor == '2':

    # чтение файлов из директории и создание списка с названиями
    for x in os.listdir(search_dir):
        if '.wav' in x:
            my_files.append(x)
    print(my_files)
    for f in my_files:
        print(f)
        harvard = sr.AudioFile(search_dir+'/'+f)
        with harvard as source:
            audio = r.record(source)
            с = c + list(r.recognize_google(audio, language ='ru-RU'))
            for i, letter in enumerate((r.recognize_google(audio, language ='ru-RU'))):
                if letter !=' ':
                    p = p + str(letter)
                else:
                    c.append(p)
                    p = ' '
# запись разпознанного текста в файл
with open('q.txt', 'w') as f:
    f.write(' '.join(c))

# чтение файла с распознанной речью
f=open('q.txt','r')
line=f.readline().lower()

# Поиск совпадений по ключевому слову или части слова
counter = len(line.split(word))-1
print(word, counter)

f.close()

