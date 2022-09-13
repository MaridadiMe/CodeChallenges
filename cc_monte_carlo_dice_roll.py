

import random


def roll_dice(*args):
    outcome = ''
    occurence= 0
    for arg in args:
        try:
            outcome += str(arg)
        except Exception as e:
            print(e)

    elements = len(args)
    iterations = 1000000
    if elements > 0:
        for i in range(iterations):
            guess = ""
            for j in range(elements):
                guess += str(random.randint(1,6))
            if guess == outcome:
                occurence += 1
    print(f'{outcome}: iterations : {iterations} occurence : {occurence}: probability : {(occurence/iterations)* 100}%')

if __name__ == '__main__':
    roll_dice(1,2)