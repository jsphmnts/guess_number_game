import random

print('----------------------------------------')
print('--------GUESS THAT NUMBER GAME----------')
print('----------------------------------------')
print()
the_number = random.randint(0, 100)
name = input('What is your name? ')

guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    # print(guess_text, type(guess_text))
    # print(guess, type(guess))
    if guess < the_number:
        #print('Your guess of ' + guess_text + ' was too low, ' + name + '. Try again!')
        print('Sorry {}, your guess of {} was too LOW'.format(name, guess))
    elif guess > the_number:
        #print('Your guess of ' + guess_text + ' was too high, ' + name + '. Try again!')
        print('Sorry {}, your guess of {} was too HIGH'.format(name, guess))
    else:
        #print('Great job! You guessed it, ' + name + '! ' + guess_text + ' was the correct number!')
        print('Great job, {}! Your guess of {} was CORRECT!'.format(name, guess))