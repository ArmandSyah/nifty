import string
import pprint
from nltk.corpus import stopwords
from wordentry import WordEntry

word_entries = {}
english_stop_words = set(stopwords.words('english'))
punctuation_clean_up = str.maketrans('', '', string.punctuation)


def parse_review(rating: int, words: list):
    for word in words:
        if word in word_entries:
            word_entry = word_entries[word]
            word_entry.update(rating)
            word_entries[word] = word_entry
        else:
            word_entries[word] = WordEntry(word, rating)


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


if __name__ == '__main__':
    main()
