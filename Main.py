# Case-study #8
# Developers:   Aksenov A. (60%),
#               Soloveychik D. (20%),
#               Labuzov A. (30%)
import random

text = input().replace('/n', ' ')


def correct_text():
    """Удаление из текста символов кроме чисел, букв и разрешённых знаков препинания"""
    global text
    chars = (
        '~', '`', '@', '#', '№', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', ':', ';', '{', '}', '[', ']',
        '/',
        '|', '<', '>', '\'', '\"', "—")
    for letter in text:
        if letter in chars:
            text = text.replace(letter, '')


correct_text()
# print(text, 'после удаления ненужных символов')
text = text.split(" ")
for word in text:
    if word == '':
        text.remove(word)
# print(text, 'после сплита')

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
nexty = []  # список списков
for i in unic:
    dop = ""  # переменная для создания списка списков
    for j in range(len(text) - 1):
        if i == text[j]:
            dop = dop + text[j + 1] + " "
    if dop != "":
        dop = dop.split(" ")
        for word in dop:
            if word == '':
                dop.remove(word)
        nexty.append(dop)
#print(unic, 'список уникальных слов')
#print(nexty, 'список звеньев и связок')
#print(big, 'список слов с заглавной буквы')

start = random.choice(big)  # случайное слово с большой буквы
helpy = ""  # вспомогательная переменная
for i in range(len(text)):  # версия, где столько же слов, сколько в оригинале
    if start == unic[-1]:
        start = random.choice(big)
    for j in range(len(unic) - 1):
        if start == unic[j]:
            helpy = helpy + start + " "
            start = random.choice(nexty[j])
            break
print(helpy)
