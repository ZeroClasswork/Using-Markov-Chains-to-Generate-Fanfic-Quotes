from flask import Flask, request, render_template
import re
import random
import os
import sample
import cleanup
import markovogram

import sentence

app = Flask(__name__)

contents = cleanup.clean_file('ghosts_on_coruscant.txt')
markie = markovogram.Markovogram(contents)

# def get_words():
#     f = open("./text/ghosts_on_coruscant.txt", "r")
#     contents = f.read()
#     f.close()
#     return contents
    
@app.route('/', methods=['GET'])
def generate_sentence():
    number = request.args.get('num')
    if number is None:
        number = 10
    else:
        number = int(number)
    new_sentence = markie.random_walk(number)
    return render_template("base.html", new_sentence=new_sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))