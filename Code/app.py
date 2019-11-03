from flask import Flask
import sample
import re
import random
import os

app = Flask(__name__)

@app.route('/')
def generate_sentence():
    f = open("./text/rumpelstiltskin.txt", "r")
    contents = f.read()
    # words_list = re.split('\W+', contents)
    f.close()
    new_sentence = ""
    number = 10
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
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))