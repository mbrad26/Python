import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sequence({reprlib.repr(self.text)})'

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]


seq = Sentence('kaj jashdjhd ajshdhd adhlshasalhdla sadhasa s ashdalsas')

print(repr(seq))
print(seq)
print(seq[3])
print(len(seq))
print(type(seq))

################################################################################

RE_WORDS = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORDS.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self
































