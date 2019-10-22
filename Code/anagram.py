import random

def anagram(original_string):
    new_string = ""
    string_list = list(original_string)

    for index in range(len(string_list)):
        list_item = random.choice(string_list)
        new_string += list_item
        string_list.remove(list_item)

    return new_string

print(anagram("hello"))
print(anagram("hello"))
print(anagram("hello"))
print(anagram("hello"))
print(anagram("hello"))