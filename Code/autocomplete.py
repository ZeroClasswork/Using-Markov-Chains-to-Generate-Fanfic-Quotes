import random

f = open("/usr/share/dict/words", "r")
contents = f.read()
words_list = contents.split("\n")

long_words_list = list()

for word in words_list:
    if len(word) > 2:
        long_words_list.append(word)

first_characters = random.choice(words_list)[0:3]

print("Words starting with {}:".format(first_characters))

for word in words_list:
    if first_characters == word[0:3]:
        print(word)