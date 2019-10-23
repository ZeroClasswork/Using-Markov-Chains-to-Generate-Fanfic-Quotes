import sys
import random

def rearrange(original_list, num_arguments):
    new_list = list()

    for index in range(num_arguments):
        list_item = random.choice(original_list)
        new_list.append(list_item)
        original_list.remove(list_item)

    for item in new_list:
        print(item, end=" ")

    print()

if __name__== "__main__":
    num_arguments = len(sys.argv) - 1
    original_list = sys.argv[1:]

    rearrange(original_list, num_arguments)