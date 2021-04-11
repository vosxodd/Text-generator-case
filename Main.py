# Case-study #8
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
import random
text = input().replace('/n', ' ')


def correct_text():
    """Удаление из текста символов кроме чисел, букв и разрешённых знаков препинания"""
    global text
    chars = (
    '~', '`', '@', '#', '№', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', ':', ';', '{', '}', '[', ']', '/',
    '|', '<', '>', '\'', '\"', "—")
    for letter in text:
        if letter in chars:
            text = text.replace(letter, '')


correct_text()
#print(text, 'после удаления ненужных символов')
text = text.split(" ")
for word in text:
    if word == '':
        text.remove(word)
#print(text, 'после сплита')
unic = []
b = 0
for i in text:
    for j in unic:
        if i == j:
            b = 1
    if b != 1:
        unic.append(i)
    b = 0
big = []
for i in unic:
    if i == i.capitalize():
        big.append(i)
nexty=[] #список списков
dop="" #переменная для создания списка списков
for i in unic:
    dop=""
    for j in range(len(text)):
        if i==text[j] and j!=len(text)-1:
            dop=dop+text[j+1]+" "
    if dop!="":
        dop=dop.split(" ")
        for word in dop:
            if word == '':
                dop.remove(word)
        nexty.append(dop)
#print(unic)
#print(nexty)
#print(big)
start=random.choice(big)#случайное слово с большой буквы
helpy=""#вспомогательная переменная
for i in range(0,len(text)):#версия где столько же слов сколько в оригинале
    if start==unic[len(unic)-1]:
        start=random.choice(big)
    for j in range(0,len(unic)):
        if start==unic[j] and j!=len(unic)-1:
            helpy=helpy+start+" "
            start=random.choice(nexty[j])
            break
print(helpy)
