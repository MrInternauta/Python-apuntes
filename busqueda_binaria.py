# -*- coding: utf-8 -*-
def binary_search(numbers, number_find, low, high):
    mid = (low+high)/2
    if(low>high):
        return False
    if numbers[mid] == number_find:
        return True
    if numbers[mid] > number_find:
        return binary_search(numbers, number_find, low, mid-1)
    else:
        return binary_search(numbers, number_find, mid+1, high)


if __name__ == '__main__':
    numbers = [1,3,4,5,6,7,8,11,12,14,15,21,23]
    number_find = int(raw_input('Ingresa un numero: '))
    result = binary_search(numbers, number_find, 0, len(numbers)-1)
    if result is True:
        print('El numero {} si esta en la lista'.format(number_find))
    else:
        print('El numero {} no esta en la lista'.format(number_find))
