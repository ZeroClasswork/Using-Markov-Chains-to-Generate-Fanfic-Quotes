import sys
import random

import frequency_analysis

def random_word(input_list):
    return input_list[random.randrange(len(input_list))]

if __name__== "__main__":
    input_list = sys.argv[1:]