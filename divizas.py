# -*- coding: utf-8 -*-

def run():
    print('C A L C U L A D O R A   D E   DIVISAS')
    print('Convierte pesos MXN a Colombianos')
    print('')
    ammount = float(raw_input('Ingresa de MXN'))
    resul = foreign_exchange_calculation(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, resul))

def foreign_exchange_calculation(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount



if __name__ == '__main__':
    run()