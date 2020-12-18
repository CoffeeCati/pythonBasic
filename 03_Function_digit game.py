import random

print('Hello there is one NUMBER I am thinking now(Integrate)')
print('Can you guess the NUMBER what I thinking?(From 1 to 20)')
secretNum = random.randint(1, 20);
for i in range(6):
    guesses = int(input())
    if guesses < secretNum:
        print('You guess is too low.')
    elif guesses > secretNum:
        print('Your guess is too high.')
    else:
        break
if guesses == secretNum:
    print('Good job! You guess my NUMBER in ' + str(i+1) + ' guesses!')
else:
    print('Nope. The NUMBER I was thinking of was ' + str(secretNum))
