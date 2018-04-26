"""
    Tokenizing and Parsing Utilities
"""
import os
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from .models.wordentry import WordEntryModel

UNWANTED_STRINGS = ['LRB', 'RRB', '-LRB-', '-RRB-']
ENGLISH_STOP_WORDS = set(stopwords.words('english'))
PUNCTUATION_CLEAN_UP = str.maketrans(
    '', '', ''.join(p for p in string.punctuation if p != '-' or p != '\''))


def acceptable_word(word: str):
    """
        Check if word is valid 
        (ie. not a stopword, not punctuation, not braces, not space of not a digit or single letter)
    """
    return (word.lower() not in ENGLISH_STOP_WORDS and
            word.lower() not in string.punctuation and
            word not in UNWANTED_STRINGS and
            not word.isspace() and
            (word.isdigit() or len(word) > 1))


def tokenize(words: str):
    """
        Splits sentence into tokens
    """
    cleaned_words = [word.translate(PUNCTUATION_CLEAN_UP)
                     for word in words]
    return [word.lower().strip()
            for word in cleaned_words if acceptable_word(word.strip())]


def parse_review(rating: int, words: list):
    """
        Takes review and applies rating to each word in the list
        and then saves rating to database
    """
    for word in words:
        word_entry = WordEntryModel.find_by_word(word)
        if word_entry:
            word_entry.update(rating)
        else:
            word_entry = WordEntryModel(word, rating)
        word_entry.save_to_db()


def set_up_words():
    """
        Utility function for parsing through movieReviews.txt 
        and scoring words
    """
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'movieReviews.txt')) as reviews:
        for line in reviews:
            words = tokenize(word_tokenize(line))
            rating = int(words[0])
            parse_review(rating, words[1:])
    print('SETUP COMPLETE')


def analyze(word_entries: list):
    """
        Calculates the average of all Word_Entry objects in a list
    """
    if len(word_entries) <= 0:
        return 0
    return sum(word.average for word in word_entries) / len(word_entries)
