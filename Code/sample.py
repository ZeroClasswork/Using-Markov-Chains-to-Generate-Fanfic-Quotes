import sys
import random

import frequency_analysis

def random_word(input_list):
    return input_list[random.randint(0, len(input_list) - 1)]

if __name__== "__main__":
    # input_list = sys.argv[1:]
    one = 0
    two = 0
    red = 0
    blue = 0
    fish = 0

    input_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]

    for count in range(10000):
        word = random_word(input_list)
        if word == "one":
            one += 1
        elif word == "two":
            two += 1
        elif word == "red":
            red += 1
        elif word == "blue":
            blue += 1
        elif word == "fish":
            fish += 1
  
    print("one:  ", (1.0 * one  / 100), "%")
    print("two:  ", (1.0 * two  / 100), "%")
    print("red:  ", (1.0 * red  / 100), "%")
    print("blue: ", (1.0 * blue / 100), "%")
    print("fish: ", (1.0 * fish / 100), "%")