import numpy as np
import random


def check(secret_number,guessed_number):
    cows=0
    bulls=0
    secret_num_str = str(secret_number)
    guessed_num_str = str(guessed_number)
    for i in range(len(guessed_num_str)):
        if guessed_num_str[i] in secret_num_str:
            if guessed_num_str[i]== secret_num_str[i]:
                bulls+=1
            else:
                cows+=1
    return bulls,cows

def gen_sec_num(num_digits):
    digits = list(range(10))
    sec_num = 0
    for i in range(num_digits):
        if i==0:
            rand_idx = random.randint(1,len(digits)-1)
        else:
            rand_idx = random.randint(0,len(digits)-1)
        dig = pow(10,i) * digits.pop(rand_idx)
        sec_num += dig
    return sec_num

def main():
    num_digits = int(input('\nEnter number of digits: '))
    secret_number = gen_sec_num(num_digits)
    bulls=0
    steps=0
    while(bulls!=num_digits):
        guessed_number = int(input('\nGuess a {} digit number: '.format(num_digits)))
        bulls,cows = check(secret_number,guessed_number)
        print('Bulls:',bulls,'Cows:',cows)
        steps+=1
    print('Success, You guessed the nubmer correctly in {} steps. The number was {}'.format(steps,secret_number))
    
if __name__ == "__main__":
    main()

