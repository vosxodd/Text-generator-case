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
