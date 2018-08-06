# -*- coding: utf-8 -*-
from math import pow, sqrt
import statistics as stats

#Calcular la media
#Restar media a cada dato
#Elevar resultados al cuadrado
#Sumar todos los resultados
#Calcular la media
numbersMean = [1525, 257, 378, 9543, 7854, 152]
numbersMode = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
numbersMedian = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]
ejemp = [0,2,4,5,8,10,10,15,38]
YearsStudents = [13, 14, 15, 15, 15, 16, 17, 18, 20]

def desviacion_estandar(prom):
    desvi = sqrt(prom)
    return desvi

def media(lista):
    lon = len(lista)
    prom = 0.0
    for i in lista:
        prom += (i)
    prom = prom/lon
    return prom

def varianza(lista):
    vari = 0.0
    lon = len(lista)
    promedio = float(media(lista))
    #
    for dat in lista:
        vari += (dat-promedio)**2
        variacion = vari/lon
    return variacion

def impri_list(lista):
    str_list = "...::: LISTA :::...\n"
    for i in lista:
        str_list +=str(i)+" "
    str_list += "\n.............."
    return str_list

#Obtener moda
def moda(datos):
    #Valores a tomar en cuenta
    resultados = []
    repeticiones = 0
    #Contar los valores y obtener los mas repetidos
    for i in datos:
        apariciones = datos.count(i)
        if apariciones >= repeticiones:
            if apariciones == repeticiones and resultados.count(i) == 0:
                resultados.append(i)
            elif resultados.count(i) == 0:
                resultados = [i]
            repeticiones = datos.count(i)
    return resultados


#Obtener mediana
def mediana(datos):
    mediana = 0
    n = len(datos)
    datos.sort()
    if n % 2 == 0: # si es par la formula es: Me = X(n / 2 ) + X((n / 2) + 1)
        mediana = (datos[int((n / 2) + 1) - 1] + datos[int( n / 2)] - 1) / 2
    else: # Si es impar la formula es: Me = X((n + 1) / 2)
        mediana = datos[int((n + 1) / 2) - 1]
    return mediana


def desplegar(Numberslist):
    print(impri_list(Numberslist))
    varia = varianza(Numberslist)
    de_es = desviacion_estandar(varia)
    media_ = media(Numberslist)
    moda_ = moda(Numberslist)
    mediana_ = mediana(Numberslist)
    print('Media o Promedio: {}'.format(media_))
    print('Moda: {}'.format(moda_))
    print('Mediana: {}'.format(mediana_))
    print('Varianza: {}'.format(varia))
    print('Desviación Estándar: {}'.format(de_es))
    print('*-*-*-*\n')

if __name__ == '__main__':
    desplegar(numbersMean)
    desplegar(numbersMode)
    desplegar(numbersMedian)
    desplegar(ejemp)
    desplegar(YearsStudents)
