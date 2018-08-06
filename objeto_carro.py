# -*- coding: utf-8 -*-
from Carro import CarroF

def main():
    carrito = CarroF()
    while True:
        command = str(raw_input('''
        Seleciona una opcion
        [a]gregar datos
        [c]ambiar estado
        [s]alir
        '''))
        if command == 'a':
            model = str(raw_input('Ingresa un modelo: '))
            color = str(raw_input('Ingresa un color: '))
            estado = str(raw_input('Ingresa un estado: a: True, b: False'))
            if estado == 'a':
                status = True
            elif estado == 'b':
                status = False
            else:
                print('Opcion invalida')
                status = False
            carrito.set_information(model,color, type, status)
        elif command == 'c':
            carrito.change_status()
            print('Estado cambiado')

        elif command == 's':
            break
        else:
            print('Comando invalido')


if __name__ == '__main__':
    main()
