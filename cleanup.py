import re

def get_words(file_name):
    f = open("./text/"+ file_name, "r")
    contents = f.read()
    f.close()
    return contents

def clean_text(source_text):
    all_words_text = re.sub(r'[^\w\s]', '', str(source_text)).upper()
    all_words_text = re.sub('_', '', all_words_text)
    text_list = re.split(r'\W+', all_words_text)

    for word in text_list:
        if word == "":
            text_list.remove(word)

    return text_list

def clean_file(file_name):
    return clean_text(get_words(file_name))

def tests():
    texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']

    print("Rumpelstiltskin cleaned:")
    print(clean_file(texts[0]))
    
    print("Tom Thumb cleaned:")
    print(clean_file(texts[1]))

# if __name__ == "__main__":
#     tests()
