import cleanup

def tuples_histogram(source_list):
    histogram = list()
    for word in source_list:
        found = False
        for pair in histogram:
            if pair[0] == word and not found:
                number = pair[1] + 1
                histogram.remove(pair)
                histogram.append((word, number))
                found = True
        if not found:
            histogram.append((word, 1))

    return histogram

def lists_histogram(source_list):
    histogram = list()
    for word in source_list:
        found = False
        for pair in histogram:
            if pair[0] == word and not found:
                pair[1] += + 1
                found = True
        if not found:
            histogram.append([word, 1])

    return histogram

def dictionary_histogram(source_list):
    histogram = dict()
    for word in source_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram

def counts_histogram(source_list):
    histogram = list()
    for word in source_list:
        found = False
        for pair in histogram:
            if word in pair[1] and not found:
                added = False
                number = pair[0] + 1
                found = True
                if len(pair[1]) == 1:
                    histogram.remove(pair)
                else:
                    pair[1].remove(word)
                for new_pair in histogram:
                    if new_pair[0] == number:
                        new_pair[1].append(word)
                        added = True
                if not added:
                    histogram.append((number, [word]))
        if not found:
            added = False
            for new_pair in histogram:
                if new_pair[0] == 1:
                    new_pair[1].append(word)
                    added = True
            if not added:
                histogram.append((1, [word]))
    
    return histogram

def unique_words_lists_tuples_dictionary(histogram):
    return len(histogram)

def unique_words_counts(histogram):
    count = 0
    for _, list_of_words in histogram:
        count += len(list_of_words)
    return count

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
    texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']

    story_list = cleanup.clean_file(texts[0])

    result = tuples_histogram(story_list)

    # print(result)
    print(unique_words_lists_tuples_dictionary(result))
    print(frequency_tuples_and_lists("Killer", result))
    print(frequency_tuples_and_lists("to", result))
    # print(sort_tuples_and_lists(result))

    result = lists_histogram(story_list)

    # print(result)
    print(unique_words_lists_tuples_dictionary(result))
    print(frequency_tuples_and_lists("Killer", result))
    print(frequency_tuples_and_lists("to", result))
    # print(sort_tuples_and_lists(result))

    result = dictionary_histogram(story_list)

    # print(result)
    print(unique_words_lists_tuples_dictionary(result))
    print(frequency_dictionary("Killer", result))
    print(frequency_dictionary("to", result))

    result = counts_histogram(story_list)

    # print(result)
    print(unique_words_counts(result))

if __name__== "__main__":
    tests()