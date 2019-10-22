import random

f = open("/usr/share/dict/words", "r")
contents = f.read()
words_list = contents.split("\n")

def generateSentence(number):
    sentence = ""
    for i in range(number):
        sentence += random.choice(words_list)
        if i != number -1:
            sentence += " "
        else:
            sentence += "."

    return sentence

print(generateSentence(5))
print(generateSentence(3))
print(generateSentence(6))
print(generateSentence(2))
print(generateSentence(3))
print(generateSentence(6))