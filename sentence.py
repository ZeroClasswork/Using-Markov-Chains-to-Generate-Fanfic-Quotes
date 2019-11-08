import sample
import random
import cleanup

def generate_sentence(number, contents):
    new_sentence = ""
    for i in range(number):
        new_sentence += sample.random_word_list(contents).lower()
        if i == 0:
            new_sentence = new_sentence.capitalize()
        if i != number - 1:
            new_sentence += " "
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            new_sentence += random.choice(punctuation)
    return new_sentence

def tests():
    texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']

    contents = cleanup.clean_file(texts[0])
    
    generate_sentence(10, contents)

if __name__== "__main__":
    tests()