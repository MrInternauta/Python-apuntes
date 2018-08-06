# -*- coding: utf-8 -*-

def run(num):
    # caso base
    if num == 0:
        return 0
    #caso recursivo
    else:
        return run(num - 1) + num

if __name__ == '__main__':
    num = int(input('Cuantos números deseas sumar: '))
    resultado = run(num)
    print('La suma de los {} primeros números es {}'.format(num, resultado))
