import string
import pprint
from functools import reduce
from nltk.corpus import stopwords
from wordentry import WordEntry

word_entries = {}
english_stop_words = set(stopwords.words('english'))
punctuation_clean_up = str.maketrans('', '', string.punctuation)


def parse_review(rating: int, words: list):
    for word in words:
        if word in word_entries:
            word_entries[word].update(rating)
        else:
            word_entries[word] = WordEntry(word, rating)


def analyze():
    while True:
        sentence = input('Type something: ')
        sentence = [word.lower().translate(punctuation_clean_up)
                    for word in sentence.split() if word not in english_stop_words]
        total, useful_words = 0, 0
        for word in sentence:
            if word in word_entries:
                total += word_entries[word].get_average()
                useful_words += 1
        print(
            f"This review has an average value of {total / useful_words}")


def main():
    with open('movieReviews.txt') as reviews:
        for line in reviews:
            words = line.lower().split()
            words = [word.translate(punctuation_clean_up)
                     for word in words if word not in english_stop_words]
            rating = int(words[0])
            parse_review(rating, words[1:])
        print('Finished parsing reviews')
    for _, v in word_entries.items():
        print(
            f"Word: {v.word}, Total: {v.total_score}, Frequency: {v.frequency}, Average: {v.get_average()}")
    analyze()


if __name__ == '__main__':
    main()
