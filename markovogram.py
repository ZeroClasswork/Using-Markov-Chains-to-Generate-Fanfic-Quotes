from __future__ import division, print_function  # Python 2 and 3 compatibility


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

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Markovogram(word_list)
    print('markovogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))

def main():
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


if __name__ == '__main__':
    main()
