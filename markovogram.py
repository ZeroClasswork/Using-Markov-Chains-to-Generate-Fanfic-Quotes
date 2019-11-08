from __future__ import division, print_function  # Python 2 and 3 compatibility
import sample
import random
import cleanup

class Markovogram(dict):
    """Markovogram is a markov histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markovogram, self).__init__()  # Initialize this as a new dict
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for index in range(len(word_list) - 1):
                if self.tokens == 0:
                    self.tokens = 1
                self.add_count(word_list[index], word_list[index + 1])

    def add_count(self, word1, word2, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increases word frequency by count
        self.tokens += count
        try:
            sub_dict = self[word1]
                
        except:
            sub_dict = dict()
            sub_dict[word2] = count
            self[word1] = sub_dict
            self.types += 1
        
        else:
            try:
                sub_dict[word2] += count
                self[word1] = sub_dict

            except:
                appended_sub_dict = dict()
                appended_sub_dict[word2] = count
                for key, value in self[word1].items():
                    appended_sub_dict[key] = value
                self[word1] = appended_sub_dict

    def frequency(self, word):
        histogram = self[word.upper()]
        frequency = 0
        for _, value in histogram.items():
            frequency += value
        return value

    def sample_next(self, recent_word):
        try:
            histogram = self[recent_word.upper()]
            index = random.randrange(self.frequency(recent_word))
            value = 0
            last_word = "ISSUEINLASTWORD"
            for word, value in histogram.items():
                last_word = word
                if value <= index:
                    value += value
                else:
                    return word
            return last_word
        except:
            return "ISSUEINEXCEPT"
        

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markovogram(word_list)
    print('markovogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))

def random_walk(word_list, sentence_length):
    new_sentence = ""
    recent_word = sample.random_word_tuple(word_list).capitalize()
    markovogram = Markovogram(word_list)
    for i in range(sentence_length - 1):
        new_sentence += recent_word
        if i != sentence_length - 2:
            new_sentence += " "
        else:
            punctuation = [".", "!", "?", "...", "!?"]
            new_sentence += random.choice(punctuation)
        recent_word = markovogram.sample_next(recent_word).lower()
    return new_sentence

def tests():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())

def main():
    texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']

    contents = cleanup.clean_file(texts[0])
    
    print(random_walk(contents, 10))

if __name__ == '__main__':
    main()
