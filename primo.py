# -*- coding: utf-8 -*-
def run():
    number = int(raw_input('Ingresa un numero: '))
    state = is_prime(number)
    if state == True:
        print('Es primo')
    else:
        print('No es primo')

def is_prime(number):

    if number < 2:
       return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            print(i)
            if number % i == 0:
                return False
    return True
        

if __name__ == '__main__':
    run()          