# -*- coding: utf-8 -*-

#Funcion principal
def main():
    word = raw_input('Ingresa una palabra: ') #Pide y guarda una palabra
    result = is_palindromo(word) #Pasa la palabra a la funcion
    if result == True:
        print ('Es palindromo')
    else:
        print ('No es palindromo')

#Funcion determina si es palindromo
def is_palindromo(word):
    if word == word[::-1]: #voltea la palabra
        return True
    else:
        return False

#inicio del programa
if __name__ == '__main__':
    main()
