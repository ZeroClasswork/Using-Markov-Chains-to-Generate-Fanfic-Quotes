import random

f = open("/usr/share/dict/words", "r")
contents = f.read()
words_list = contents.split("\n")
f.close()

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
            if isinstance(little_list, list):
                all_anagram_list += little_list
            else:
                all_anagram_list.append(little_list)
            

            if size % 2 == 1:
                original_string[0], original_string[size - 1] = original_string[size - 1], original_string[0]
            else:
                original_string[index], original_string[size - 1] = original_string[size - 1], original_string[index]

    return all_anagram_list
    
def unique_anagrams(all_anagrams_list):
    unique_list = list() 

    for item in all_anagrams_list: 
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

def real_anagrams(original_string):
    all_anagrams_list = unique_anagrams(all_anagrams(list(original_string), len(original_string)))

    real_anagrams_list = list()

    for anagram in words_list:
        if anagram in all_anagrams_list:
            real_anagrams_list.append(anagram)

    return real_anagrams_list

def tests():
    print(real_anagrams("dolphin"))
    print(real_anagrams("salad"))

if __name__== "__main__":
    tests()


# use a set instead of list for uniqueness and quicker accessing