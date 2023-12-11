alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']


def cipher_text(cipher_direction, user_text, shift_number):
    ciphertext = ''
    if cipher_direction == 'decode':
        shift_number *= -1
    for character in user_text:

        if character in alphabets:
            text_position = alphabets.index(character)
            position = text_position + shift_number
            ciphertext += alphabets[position]
        else:
            ciphertext += character

    print(f'the {cipher_direction}d code is -> {ciphertext}')


Run = True

while Run:

    direction = input('Do you want to encrypting TYPE "encode"'
                      ' or decrypting TYPE "decode" : '.title()).lower()
    text = input('enter the word : '.title()).lower()
    shifting = int(input('enter the shift number : '.title()))

    shifting %= 26
    cipher_text(user_text=text, shift_number=shifting, cipher_direction=direction)

    Run_Again = input('Do You Wanna do again ? [y/n] : ').lower()

    if Run_Again == 'n':
        Run = False
