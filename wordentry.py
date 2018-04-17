class WordEntry:
    def __init__(self, word: str, total_score: int):
        self._word = word.lower()
        self._total_score = total_score
        self._frequency = 1

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, word):
        print('You\'re not allowed to set a word already defined')

    @property
    def total_score(self) -> int:
        return self._total_score

    @total_score.setter
    def total_score(self, score):
        print('You\'re not allowed to set a score like this')

    @property
    def frequency(self) -> int:
        return self._frequency

    @frequency.setter
    def frequency(self, freq):
        print('You\'re not allowed to set a frequency like this')


def main():
    test = WordEntry('memes', 0)
    print(test.word)
    print(test.frequency)
    print(test.total_score)
    test.word = 'nice'
    print(test.word)
    test.frequency = 435
    print(test.frequency)


if __name__ == '__main__':
    main()
