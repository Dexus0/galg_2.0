from os import system
from time import sleep
from sys import stdout

empty = [

    #_______________
    # |/           |
    " |            ",
    " |          ",
    " |         ",
    " |          ",
    " |           ",
    " |           ",
    # |________
]

boi = [
    "|",
    '',
    "__| |__",
    "(_._)",
    "| |",
    "| |"]

eyes = [
    "(UwU)",
    "(owO)",
    "(Owo)",
    "(XwX)",
    "(^w^)"
]


def clear():
    system('cls')


def draw():
    global fout, boi, empty, eye_Mode
    boi[1] = eyes[eye_Mode]

    clear()
    stdout.write("_______________\n"
                 " |/           |\n")
    for i, line in enumerate(empty):
        stdout.write(line)
        if i < fout:
            stdout.write(boi[i])

        stdout.write('\n')
    stdout.write(" |________\n")
    stdout.flush()

alphabet = "abcdefghijklmnopqrstuvwxyz"

#while True
eye_Mode = 0
fout = 0
guesslist = set()

letter = ''
while not letter:

    word = input("Gib word ples: ").lower()
    if word[:5] == '/stop':
        exit(0)

    for letter in word:
        if letter not in alphabet and letter != '-':
            clear()
            print("word needs to consist of letters or an '-'")
            letter = ''
            break



fout = 0
maxfouten = 7

while True:
    guess = ''

    draw()
    print(f'Nog {maxfouten - fout} fouten tot de dood.')

    stdout.write('{')
    for letter in guesslist:
        if letter not in word:
            stdout.write(letter + ', ')
    else:
        stdout.write('\b\b}\n')
        stdout.flush()

    for letter in word:
        if letter in guesslist:
            stdout.write(letter)
        elif letter == '-':
            stdout.write('-')
        else:
            stdout.write('#')
    else:
        stdout.write('\n\n')
        stdout.flush()

    while not guess:
        guess = input('Enter a letter here: ').lower()

        if len(guess) == 1 and guess in alphabet:
            if guess in guesslist:
                print(f"You already guessed the letter {guess}.")
            else:
                guesslist.add(guess)
        elif guess == '/stop':
            exit(0)
        else:
            for letter in guess:
                if not (letter in alphabet or letter == '-'):
                    guess = ''
                    break


    if guess == word or all( 0 for letter in word if not (letter in guesslist or letter == '-')):
        eye_Mode = 4
        draw()
        print('Congrats you won!')
        print(word)
        exit(0)
    elif len(guess) == 1 and guess in word:
        count = word.count(guess)
        draw()
        print(f'{guess}, zit er, {count}, keer in.')
    else:
        fout += 1
        draw()
        print(f'De letter {guess} zit er niet in.')


    if fout > maxfouten - 1:
        break


for eye_Mode in range(15):
    eye_Mode = eye_Mode % 2 + 1
    draw()
    print(f'Het word was: {word}.')
    print('You lost!')
    sleep(0.2)

eye_Mode = 3
draw()
print(f'Het word was: {word}.')
print('You lost!')

input('Press any key to continue.')
