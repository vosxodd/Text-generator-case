# Case-study #8
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)

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
print(text, 'после удаления ненужных символов')
text = text.split(" ")
for word in text:
    if word == '':
        text.remove(word)
print(text, 'после сплита')
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
print(unic)
print(nexty)
print(big)
