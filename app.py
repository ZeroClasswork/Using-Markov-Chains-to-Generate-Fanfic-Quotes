from flask import Flask
import re
import random
import os
import sample
import cleanup
import markovogram
from flask import request, render_template

import sentence

app = Flask(__name__)

def get_words():
    f = open("./text/rumpelstiltskin.txt", "r")
    contents = f.read()
    f.close()
    return contents
    
@app.route('/', methods=['GET'])
def generate_sentence():
    texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']
    contents = cleanup.clean_file(texts[0])
    number = request.args.get('num')
    if number is None:
        number = 10
    else:
        number = int(number)
    new_sentence = markovogram.random_walk(contents, number)
    return render_template("base.html", new_sentence=new_sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))