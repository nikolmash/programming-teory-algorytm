import json
import random
import re


class FlashCards():
    def __init__(self, path: str):
        with open(path) as f:
            self._cards = json.loads(f.read())
        self._words = list(self._cards.keys())

    @property
    def words(self):
        return self._words

    def play(self) -> str:
        correct = 0
        if len(self._words) > 0:
            for rusword in random.sample(self._words, len(self._words)):
                print(rusword)
                user_input = input()
                if not isinstance(user_input, str):
                    return 'Your input must be string'
                else:
                    user_input = ''.join([x.lower() for x in user_input])
                    if user_input == self._cards[rusword]:
                        correct += 1
        else:
            return 'The dictionary is empty'
        return 'Done! {} of {} correct!'.format(correct, len(self._words))

    def add_word(self, russian: str, english: str) -> str:
        if not isinstance(russian, str) or not isinstance(english, str):
            return 'Russian and english words must be strings!'
        elif russian == '' or english == '':
            return 'Russian and english words must not be empty'
        elif re.match(r'[А-ЯЁа-яё]', russian) is None:
            return('First word should be russian and second - english')
        if re.match(r'[A-Za-z]', english) is None:
            return ('First word should be russian and second - english')
        elif russian in self._words:
            return 'Word "{}" is already in dictionary'.format(russian)
        else:
            self._cards[russian] = english
            self._words.append(russian)
            return 'Successfully added word "{}"'.format(russian)

    def delete_word(self, russian: str) -> str:
        if not isinstance(russian, str):
            return 'Russian word must be string!'
        elif russian == '':
            return 'Russian word must not be empty'
        elif re.match(r'[А-ЯЁа-яё]', russian) is None:
            return 'Your russian word is not russian'
        elif len(self._words) == 0:
            return('The dictionary is empty')
        elif russian in self._words:
            self._words.remove(russian)
            self._cards.pop(russian)
            return 'Successfully deleted word "{}"'.format(russian)
        else:
            return 'Word "{}" is not in dictionary'.format(russian)









