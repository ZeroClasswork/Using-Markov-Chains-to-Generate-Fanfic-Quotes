def reverse_string(string):
    new_string = ""

    for char_num in range(len(string)):
        new_string += string[len(string) - char_num - 1]

    return new_string

def tests():
    print(reverse_string("Hello friend"))

if __name__ == "__main__":
    tests()