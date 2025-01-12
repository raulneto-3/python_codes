import random
import nltk
from nltk.corpus import words

# Ensure the 'words' corpus is downloaded
# nltk.download('words')

def generate_valid_words(num_words):
    word_list = words.words()
    return random.sample(word_list, num_words)

if __name__ == '__main__':
    num_words = 8  # Example number of words to generate
    valid_words = generate_valid_words(num_words)
    print(valid_words)