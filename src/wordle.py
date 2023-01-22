from src.utils import print_error, print_grey, print_success, print_warning
import random

random.seed(20)

class Wordle:

    def __init__(self, file_path, limit=1000000000000000000, length=5):
        self.words = self.generate_words(file_path=file_path, limit=limit, length=length)
        self.length = length

    def generate_words(self, file_path, limit, length):

        # Build Data
        words = []
        with open(file_path) as f:
            for line in f:
                word, word_freq = line.split(', ')
                words.append((word, int(word_freq)))

        # Filter number of letters
        words = list(filter(lambda x: len(x[0])==length, words))

        # Sort top freq
        words.sort(key=lambda x: x[1], reverse=True)

        # Limit
        words = words[:limit]

        # Delete freq
        words = [item[0] for item in words]

        return words


    def run(self, number_of_try=6):
        word = random.choice(self.words)
        word = word.upper()
        print(word)
        while number_of_try:
            guess_word = input(f'enter guess with {self.length} letters or q to quit: ').upper()

            #Congrats
            if guess_word == word:
                print_success(f' {guess_word} ')
                print()
                print_success('Congrats!')
                break

            #How to quit
            if guess_word == 'Q':
                break

            #Length check
            if len(guess_word) != self.length:
                print_warning(f'guess must have {self.length} letters')
                continue

            #Db Check
            if guess_word.lower() not in self.words:
                print_warning(f'{guess_word} is not a valid word. Try again')
                continue

            #Lets start
            for g_letter, w_letter in zip(guess_word, word):
                if g_letter == w_letter:
                    print_success(f' {g_letter} ', end=' ')
                    print(' ', end='')
                elif g_letter in word:
                    print_warning(f' {g_letter} ', end=' ')
                    print(' ', end='')
                else:
                    print_error(f' {g_letter} ', end=' ')
                    print(' ', end='')

            print()
            number_of_try -= 1
            if not number_of_try:
                print_error(f'{word} was the word. You lost, maybe next time!! ')