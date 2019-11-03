import sys
import random

import frequency_analysis

def random_word_tuple(input_string):
    histogram = frequency_analysis.tuples_histogram(input_string)
    index = random.randrange(len(input_string.split(" ")))
    value = 0
    hist_ind = 0
    while value <= index and hist_ind < len(histogram):
        value += histogram[hist_ind][1]
        hist_ind += 1
    return histogram[hist_ind - 1][0]
        

def random_word_list(input_string):
    histogram = frequency_analysis.lists_histogram(input_string)
    index = random.randrange(len(input_string.split(" ")))
    value = 0
    hist_ind = 0
    while value <= index and hist_ind < len(histogram):
        value += histogram[hist_ind][1]
        hist_ind += 1
    return histogram[hist_ind - 1][0]

if __name__== "__main__":
    # input_list = sys.argv[1:]
    one = 0
    two = 0
    red = 0
    blue = 0
    fish = 0

    input_string = "one fish two fish red fish blue fish"

    for count in range(100000):
        # word = random_word_tuple(input_string)
        word = random_word_list(input_string)
        if word == "ONE":
            one += 1
        elif word == "TWO":
            two += 1
        elif word == "RED":
            red += 1
        elif word == "BLUE":
            blue += 1
        elif word == "FISH":
            fish += 1 
  
    print("one:  ", (1.0 * one  / 1000), "%")
    print("two:  ", (1.0 * two  / 1000), "%")
    print("red:  ", (1.0 * red  / 1000), "%")
    print("blue: ", (1.0 * blue / 1000), "%")
    print("fish: ", (1.0 * fish / 1000), "%")