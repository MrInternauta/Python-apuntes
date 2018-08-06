#Son como listas pero no se repiten sus elementos

#Union: x = s.union(t) suma los elementos sin repetir = 1,2,3,4,5
#Interseccion: s.intersecion(t) elementos en comun = 3
#Diferencia: s.difference(t) elementos en s que no estan en t = 1,2
#Diferencia: t.difference(s) = 4,5
s = set([1,2,3])
t = set([3,4,5])
print('union')
print(s.union(t))
print('intersection')
print(s.intersection(t))
print('difference s to t')
print(s.difference(t))
print('difference t to s')
print(t.difference(s))
#Determinar si un valor esta en el set
print(1 in s)
print(1 in t)
#Determinar si un valor NO esta en el set
print(1 not in s)
print(1 not in t)
