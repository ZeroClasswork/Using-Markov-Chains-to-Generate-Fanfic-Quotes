import sample
import random
import cleanup

class Narkovogram(dict):
    """Narkovogram is an nth-order markov histogram implemented as a subclass of the dict type."""

    def __init__(self, order, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        
        super(Narkovogram, self).__init__()
        self.types = 0
        self.tokens = 0
        self.order = order

        if word_list is not None:
            for index in range(len(word_list)-1):
                if index + order < len(word_list):
                    key = str(" ".join(word_list[index: index + order])).upper()
                    value = word_list[index + order].upper()
                    self.add_count(key, value)

    def add_count(self, key, value, count=1):
        """Increase frequency count of given word by given count amount."""
        # Increases word frequency by count
        self.tokens += count
        try:
            sub_dict = self[key]
                
        except:
            sub_dict = dict()
            sub_dict[value] = count
            self[key] = sub_dict
            self.types += 1
        
        else:
            try:
                sub_dict[value] += count
                self[key] = sub_dict

            except:
                appended_sub_dict = dict()
                appended_sub_dict[value] = count
                for inner_key, inner_value in self[key].items():
                    appended_sub_dict[inner_key] = inner_value
                self[key] = appended_sub_dict

    def frequency(self, group):
        histogram = self[group.upper()]
        frequency = 0
        for _, value in histogram.items():
            frequency += value
        return value

    def sample_next(self, recent_group):
        try:
            histogram = self[recent_group.upper()]
            index = random.randrange(self.frequency(recent_group))
            outer_value = 0
            last_word = "ISSUEINLASTWORD"
            for word, value in histogram.items():
                last_word = word
                if outer_value <= index:
                    outer_value += value
                else:
                    return word
            return last_word
        except:
            return "buffalo"
        
    def random_walk(self, sentence_length):
        new_sentence = ""
        newest_word = ""
        recent_group = random.choice(list(self.keys()))
        new_sentence += recent_group.capitalize() + " "
        for i in range(sentence_length - self.order):
            newest_word = self.sample_next(recent_group).lower()
            new_sentence += newest_word
            if i != sentence_length:
                new_sentence += " "
            else:
                punctuation = [".", "!", "?", "...", "!?"]
                new_sentence += random.choice(punctuation)
            recent_group = recent_group + " " + newest_word.upper()
            recent_group = recent_group.split()[1:]
            recent_group = " ".join(recent_group)
        return new_sentence

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Narkovogram(3, word_list)
    print('narkovogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))

# def random_walk(word_list, sentence_length):
#     new_sentence = ""
#     recent_word = sample.random_word_tuple(word_list).capitalize()
#     markovogram = Markovogram(word_list)
#     for i in range(sentence_length):
#         new_sentence += recent_word
#         if i != sentence_length - 1:
#             new_sentence += " "
#         else:
#             punctuation = [".", "!", "?", "...", "!?"]
#             new_sentence += random.choice(punctuation)
#         recent_word = markovogram.sample_next(recent_word).lower()
#     return new_sentence

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
    
    contents = cleanup.clean_file('ghosts_on_coruscant.txt')
    narkie = Narkovogram(4, contents)
    print(narkie.random_walk(10))

def main():
    tests()
#     texts = ['rumpelstiltskin.txt', 'tom_thumb.txt']

#     contents = cleanup.clean_file(texts[0])
    
#     print(random_walk(contents, 10))

if __name__ == '__main__':
    main()
