from flask import Flask, request, render_template
import re
import random
import os
import sample
import cleanup
import narkovogram

import sentence

app = Flask(__name__)

contents = cleanup.clean_file('ghosts_on_coruscant.txt')
last_order = 5

# def get_words():
#     f = open("./text/ghosts_on_coruscant.txt", "r")
#     contents = f.read()
#     f.close()
#     return contents
    
@app.route('/', methods=['GET'])
def generate_sentence():
    narkie = narkovogram.Narkovogram(5, contents)
    number = request.args.get('num')
    order = request.args.get('order')
    if number is None:
        number = 10
    else:
        number = int(number)
    if order is not None and last_order != int(order):
        narkie = narkovogram.Narkovogram(int(order), contents)
    new_sentence = narkie.random_walk(number)
    return render_template("base.html", new_sentence=new_sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))