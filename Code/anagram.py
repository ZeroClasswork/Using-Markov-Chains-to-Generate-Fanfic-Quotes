import random

# uses heap permutation algorithm
def all_anagrams(original_string, size):
    all_anagram_list = list()
    if (size == 1):
        new_string = ""
        for letter in original_string:
            new_string += letter
        return new_string
    else:
        for index in range(size):
            little_list = all_anagrams(original_string, size - 1)
            all_anagram_list.append(little_list)

            if size % 2 == 1:
                original_string[0], original_string[size - 1] = original_string[size - 1], original_string[0]
            else:
                original_string[index], original_string[size - 1] = original_string[size - 1], original_string[index]

    return all_anagram_list
    


def conv_all_anagrams(original_string):
    return (all_anagrams(list(original_string), len(original_string)))

print(conv_all_anagrams("ten"))