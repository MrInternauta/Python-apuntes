# -*- coding: utf-8 -*-
#Funcion deternina el promedio
def average_temps(temps):
    sum_temps = 0
    for temp in temps:
        sum_temps += float(temp)
    return sum_temps/len(temps)

#Main
if __name__ == '__main__':
    temps = [21, 23, 24, 25, 24, 26, 31]
    average = average_temps(temps)
    print('La temperatura promedio es: {}'.format(average))
