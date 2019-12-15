from random import randint

def game(num):
    print(num)
    guess = int(input('Your guess: '))
    while guess != num:
        if guess < num:
            print('guess too low')
            guess = int(input('Guess again: '))
        elif guess > num:
            print('guess too high')
            guess = int(input('Guess again: '))
    else:
        print('correct')

num = randint(1, 6)
game(num)