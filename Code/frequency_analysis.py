import re

def tuples_histogram(source_text):
    text_list = re.split(r'\W+', source_text)
    histogram = list()
    for word in text_list:
        found = False
        for pair in histogram:
            if pair[0] == word.upper() and not found:
                number = pair[1] + 1
                histogram.remove(pair)
                histogram.append((word.upper(), number))
                found = True
        if not found:
            histogram.append((word.upper(), 1))

    for pair in histogram:
        if pair[0] == "":
            histogram.remove(pair)

    return histogram

def lists_histogram(source_text):
    text_list = re.split(r'\W+', source_text)
    histogram = list()
    for word in text_list:
        found = False
        for pair in histogram:
            if pair[0] == word.upper() and not found:
                pair[1] += + 1
                found = True
        if not found:
            histogram.append([word.upper(), 1])

    for pair in histogram:
        if pair[0] == "":
            histogram.remove(pair)

    return histogram

def dictionary_histogram(source_text):
    text_list = re.split(r'\W+', source_text)
    histogram = dict()
    for word in text_list:
        if word.upper() in histogram:
            histogram[word.upper()] += 1
        else:
            histogram[word.upper()] = 1

    if "" in histogram:
        histogram.pop("")

    return histogram

def counts_histogram(source_text):
    text_list = re.split(r'\W+', source_text)
    histogram = list()
    for word in text_list:
        found = False
        for pair in histogram:
            if word.upper() in pair[1] and not found:
                added = False
                number = pair[0] + 1
                found = True
                if len(pair[1]) == 1:
                    histogram.remove(pair)
                else:
                    pair[1].remove(word.upper())
                for new_pair in histogram:
                    if new_pair[0] == number:
                        new_pair[1].append(word.upper())
                        added = True
                if not added:
                    histogram.append((number, [word.upper()]))
        if not found:
            added = False
            for new_pair in histogram:
                if new_pair[0] == 1:
                    new_pair[1].append(word.upper())
                    added = True
            if not added:
                histogram.append((1, [word.upper()]))
                
    for pair in histogram:
        if "" in pair[1]:
            pair[1].remove("")
    
    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency_tuples_and_lists(word, histogram):
    for pair in histogram:
        if pair[0] == word.upper():
            return pair[1]
    return 0

def frequency_dictionary(word, histogram):
    if word.upper() in histogram:
        return histogram[word.upper()]
    else:
        return 0

def sort_tuples_and_lists(histogram):
    new_histogram = list()
    for _ in range(len(histogram)):
        lowest_val = histogram[0][0]
        lowest_pair = histogram[0]
        for pair in histogram:
            if pair[0] < lowest_val:
                lowest_val = pair[0]
                lowest_pair = pair
        new_histogram.append(lowest_pair)
        histogram.remove(lowest_pair)
    return new_histogram

def tests():
    #string = "one fish two fish red fish blue fish"

    string = "To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer-excellent for drawing the veil from men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory."

    result = tuples_histogram(string)

    print(result)
    print(unique_words(result))
    print(frequency_tuples_and_lists("Killer", result))
    print(frequency_tuples_and_lists("to", result))
    print(sort_tuples_and_lists(result))

    result = lists_histogram(string)

    print(result)
    print(unique_words(result))
    print(frequency_tuples_and_lists("Killer", result))
    print(frequency_tuples_and_lists("to", result))
    print(sort_tuples_and_lists(result))

    result = dictionary_histogram(string)

    print(result)
    print(unique_words(result))
    print(frequency_dictionary("Killer", result))
    print(frequency_dictionary("to", result))

    result = counts_histogram(string)

    print(result)

# if __name__== "__main__":
#     tests()