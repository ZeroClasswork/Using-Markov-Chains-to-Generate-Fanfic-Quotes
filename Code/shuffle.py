import random

def shuffle(array):
    length = len(array)

    while length:
        index = random.randrange(length)
        length -= 1
        array[length], array[index] = array[index], array[length]

    return array

def tests():
    print(shuffle([]))
    print(shuffle([1]))
    print(shuffle([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    tests()