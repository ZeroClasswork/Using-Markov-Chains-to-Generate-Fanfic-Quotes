import sys
import random

import histogram
import cleanup

def random_word_tuple(input_string):
    input_list = cleanup.clean_text(input_string)
    tuples_histogram = histogram.tuples_histogram(input_list)
    index = random.randrange(len(input_list))
    value = 0
    hist_ind = 0
    while value <= index and hist_ind < len(tuples_histogram):
        value += tuples_histogram[hist_ind][1]
        hist_ind += 1
    return tuples_histogram[hist_ind - 1][0]
        

def random_word_list(input_string):
    input_list = cleanup.clean_text(input_string)
    list_histogram = histogram.lists_histogram(input_list)
    index = random.randrange(len(input_list))
    value = 0
    hist_ind = 0
    while value <= index and hist_ind < len(list_histogram):
        value += list_histogram[hist_ind][1]
        hist_ind += 1
    return list_histogram[hist_ind - 1][0]

def tests():
    # input_list = sys.argv[1:]
    one = 0
    two = 0
    red = 0
    blue = 0
    fish = 0

    input_string = "one fish two fish red fish blue fish"

    for _ in range(100000):
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
  
    print("one:  " + str(1.0 * one  / 1000) + "%")
    print("two:  " + str(1.0 * two  / 1000) + "%")
    print("red:  " + str(1.0 * red  / 1000) + "%")
    print("blue: " + str(1.0 * blue / 1000) + "%")
    print("fish: " + str(1.0 * fish / 1000) + "%")

# if __name__== "__main__":
#     tests()