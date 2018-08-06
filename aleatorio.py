import random
def run():
    number_found = True
    random_number = random.randint(0,20) # crea numero aleatorio desde 0 a 20
    while  number_found:
        number = int(raw_input('Intenta ingresar un numero: '))
        if number == random_number:
            print('Lo encontraste')
            number_found = False
        elif number > random_number:
            print('El numero ingresado es mayor')
        elif number < random_number:
            print('El numero ingresado es menor')

if __name__ == '__main__':
    run()
