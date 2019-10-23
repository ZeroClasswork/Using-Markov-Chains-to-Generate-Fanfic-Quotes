import re

def histogram(source_text):
    text_list = re.split('\W+', source_text)
    histogram = list()
    for word in text_list:
        found = False
        for pair in histogram:
            if pair[0] == word:
                number = pair[1] + 1
                histogram.append((word, number))
                histogram.remove(pair)
                found = True
        if not found:
            histogram.append((word, 1))
    return histogram
