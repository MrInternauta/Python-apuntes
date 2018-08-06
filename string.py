# -*- coding: utf-8 -*-

if __name__ == '__main__':
    my_string = 'platzi'

    print(my_string[0] +# p
    my_string[1] + # l
    my_string[2]  +# a
    my_string[3] + # t
    my_string[4] + # z
    my_string[5]) # i
    print(len(my_string)) # 6
print(my_string.upper()) # retorna el string en máyusculas
print(my_string.lower()) # retorna el string en minúscula
print(my_string.find('p')) # retorna el índice donde se encuentra
print(my_string[1:]) #latzi
print(my_string[1:3]) #la
print(my_string[0:5]) #platz
print(my_string[0:6]) #platzi
print(my_string[0:6:2]) #salto cada 2 letras
print(my_string[::-1]) #voltea la palabra
#print(my_string[start:end:steps]) #inicio hasta elfinal y faltos
#Documentacion https://docs.python.org/3.6/library/stdtypes.html#string-methods
