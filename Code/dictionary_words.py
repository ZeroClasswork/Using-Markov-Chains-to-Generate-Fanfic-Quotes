import random

f = open("/usr/share/dict/words", "r")
contents = f.read()
words_list = contents.split("\n")

def generateSentence(number):
    sentence = ""
    for i in range(number):
        sentence += random.choice(words_list)
        if i == 0:
            sentence = sentence.capitalize()
        if i != number -1:
            sentence += " "
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            sentence += random.choice(punctuation)

    return sentence

print(generateSentence(5))
print(generateSentence(3))
print(generateSentence(6))
print(generateSentence(2))
print(generateSentence(3))
print(generateSentence(6))