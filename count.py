from collections import Counter
import json

text = "text1.txt"

# txt = """
#      Язык программирования Python 3 — это мощный инструмент для создания программ самого разнообразного назначения, доступный даже для новичков. С его помощью можно решать задачи различных типов.
# Сайт о Python призван помочь начинающим и чайникам научиться программировать на python 3. Также здесь можно подробнее узнать об особенностях функционирования этого языка Python 3.
# Язык Python обладает некоторыми примечательными особенностями, которые обуславливают его широкое распространение. Поэтому прежде чем изучать python, следует рассказать о его достоинствах и недостатках.
# """

word_list = []

some = input("Напишите текст для проверки: \n")


with open(text, 'w', encoding="utf-8") as f:
    json.dump(some, f, ensure_ascii=False)

with open (text) as R:
    read_text = json.load(R)


for world in read_text.split():
    clear_world = ""
    for letter in world:
        if letter.isalpha():
            clear_world += letter.lower()

    word_list.append(clear_world)

print(Counter(word_list))


# symbols = "!@#$%^&*()\"_<>?,.[]{}`~'"