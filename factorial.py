# -*- coding: utf-8 -*-



def fac(number):
    if number == 0:
        return 1
    return number * fac(number-1)

if __name__ == '__main__':
        number = int(raw_input("Ingresa un numero"))
        numero = fac(number)
        print( numero )
