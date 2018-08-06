
#Definir diccionario
calificaciones = {}
#Asignar valores en el diccionario
calificaciones['Algoritmos'] = 9
calificaciones['Base de datos'] = 10
calificaciones['Probabilidad'] = 10
calificaciones['Web'] =  10
#Iterar en el diccionario en las llaves
for key in calificaciones:
    print(key)
#Iterar en el diccionario en las valores
for value in calificaciones.values():
    print(value)

#Iterar en el diccionario en las valores 
for value in calificaciones.items():
    print(value)

#Iterar en el diccionario en las llaves y valores
for key, value in calificaciones.iteritems():
    print('key: {} - valor: {}'.format(key, value))

#Promedio de calificaciones
suma = 0
for  value in calificaciones.values():
    suma +=  value
promedio = suma/len(calificaciones)
print(promedio)
