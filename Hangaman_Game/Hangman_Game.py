import random
import string
from words import words
from visuals import hangman_visuals

words_list = words


def hangman_game():
    word = random.choice(words_list).upper()
    used_word = set()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    life = 7

    while len(word_letters) > 0 and life > 0:
        underscores = [letters if letters in used_word else "_" for letters in word]
        print(hangman_visuals[life])
        print('the word is ', " ".join(underscores))
        print(f'you have {life} life\'s')
        print('the used letters are : ', " ".join(used_word))
        user_input = input('guess the word :- ').upper()
        if user_input in alphabet - used_word:
            used_word.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                life -= 1
                print('you guess WRONG letter ')
        elif user_input in used_word:
            print('this letter already there !')
        else:
            print('this character is not valid ')

    if life == 0:
        print(hangman_visuals[life])
        print('\n SORRY :( GAME OVER', '\nthe word is ', word)
    else:
        print('you guessed the word :)')


if __name__ == '__main__':
    hangman_game()
