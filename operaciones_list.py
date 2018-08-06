mi_lista = []
print(type(mi_lista))
mi_lista.append(1)
mi_lista2 = [2,3,4,5]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)
mi_lista4 = ['a']
mi_lista5 = mi_lista4*10
print(mi_lista5)

#Modificar lista
lista = ['Juan', 'Pedro', 'Pepe']
lista[0] = 'Jose'
print(lista)

#Eliminar elemento
del lista[0]
print(lista)

#De String a lista
casa = 'casa'
lista_casa = list(casa)  #De string a lista
print(lista_casa)

#De Lista a String y viceversa
casa = 'casa'
lista_casa = list(casa)  #De string a lista
str_casa = ''.join(lista_casa)
print(str_casa)
