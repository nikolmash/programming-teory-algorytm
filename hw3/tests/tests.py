import unittest
from flashcards import FlashCards

class FlashCardsTestCase(unittest.TestCase):
    def setUp(self):
        self.cards_imitator = FlashCards('a.json')

    def tearDown(self):
        pass

    def test_play_empty_dict(self):
        for i in ['дуб', 'ель', 'береза', 'клен', 'лиственница', 'липа']:
            self.cards_imitator.delete_word(i)
        self.assertEqual('The dictionary is empty',
                         self.cards_imitator.play())

    def test_add_word_not_string(self):
        for message, arguments in [
            (('Russian and english words must be strings!'), (3, 4)),
            (('Russian and english words must be strings!'), (3, 'baobab')),
            (('Russian and english words must be strings!'), ('баобаб', 4))]:
            self.assertEqual(message,
                             self.cards_imitator.add_word(arguments[0], arguments[1]))

    def test_add_word_empty_argument(self):
        for message, arguments in [
            (('Russian and english words must not be empty'), ('', 'baobab')),
            (('Russian and english words must not be empty'), ('', '')),
            (('Russian and english words must not be empty'), ('баобаб', ''))]:
            self.assertEqual(message,
                             self.cards_imitator.add_word(arguments[0], arguments[1]))

    def test_add_word_not_right_alphabet(self):
        for message, arguments in [
            (('First word should be russian and second - english'),
             ('baobab', 'baobab')),
            (('First word should be russian and second - english'),
             ('baobab', 'баобаб')),
            (('First word should be russian and second - english'),
             ('баобаб', 'баобаб'))]:
            self.assertEqual(message,
                             self.cards_imitator.add_word(arguments[0], arguments[1]))

    def test_add_word_already_in(self):
        self.assertEqual('Word "береза" is already in dictionary',
                         self.cards_imitator.add_word('береза', 'birch'))
        self.assertEqual('Word "дуб" is already in dictionary',
                         self.cards_imitator.add_word('дуб', 'oak'))

    def test_add_word_new(self):
        self.assertEqual('Successfully added word "пальма"',
                         self.cards_imitator.add_word('пальма', 'palm'))
        self.assertTrue('пальма' in self.cards_imitator.words)

    def test_delete_word_not_string(self):
        self.assertEqual('Russian word must be string!',
                         self.cards_imitator.delete_word(3))

    def test_delete_word_empty_argument(self):
        self.assertEqual('Russian word must not be empty',
                         self.cards_imitator.delete_word(''))

    def test_delete_word_not_russian(self):
        self.assertEqual('Your russian word is not russian',
                         self.cards_imitator.delete_word('birch'))

    def test_delete_word_empty_dictionary(self):
        for i in ['дуб', 'ель', 'береза', 'клен', 'лиственница', 'липа']:
            self.cards_imitator.delete_word(i)
        self.assertEqual('The dictionary is empty',
                         self.cards_imitator.delete_word('береза'))

    def test_delete_word_not_in_dict(self):
        for i in ['дуб', 'ель', 'береза', 'клен', 'лиственница']:
            self.cards_imitator.delete_word(i)
            self.assertEqual('Word "{}" is not in dictionary'.format(i),
                             self.cards_imitator.delete_word(i))
        self.assertEqual('Word "кошка" is not in dictionary',
                         self.cards_imitator.delete_word('кошка'))

    def delete_word_old(self):
        for i in ['дуб', 'ель', 'береза', 'клен', 'лиственница']:
            self.assertEqual('Successfully deleted word "{}"'.format(i),
                             self.cards_imitator.delete_word(i))

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
