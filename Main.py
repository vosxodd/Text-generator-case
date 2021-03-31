# Case-study #8
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)

text = input().replace('/n', ' ')


def correct_text():
    """Удаление из текста символов кроме чисел, букв и разрешённых знаков препинания"""
    global text
    chars = ('~', '`', '@', '#', '№', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', ':', ';', '{', '}', '[', ']', '/', '|', '<', '>', '\'', '\"')
    for letter in text:
        if letter in chars:
            text = text.replace(letter, '')

correct_text()
text=text.split(" ")
unic=[]
b=0
for i in text:
    for j in unic:
        if i==j:
            b=1
    if b!=1:
        unic.append(i)
    b=0        
big=[]
for i in unic:
    if i==i.capitalize():
        big.append(i)
print(big)
