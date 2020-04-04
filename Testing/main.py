import random


def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
    except TypeError as err:
        return err


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('Nice!')
            return True
        else:
            print('Wrong input')
            return False


if __name__ == '__main__':

    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1 to 10'))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('Please enter a number')
            continue
