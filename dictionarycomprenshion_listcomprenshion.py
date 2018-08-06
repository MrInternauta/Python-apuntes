#Forma normal
pares = []
for i in range(1, 32):
    if i % 2 == 0:
        pares.append(i)
print(pares)

#list Compreheshion
pairs = [num for num in range(1,31) if num % 2 == 0]
print(pairs)

#Forma normal
cuadrados = {}
for num in range(1,11):
    cuadrados[num] = num **2
print(cuadrados)
# Dictionary Compreheshion
squares = {num: num**2 for num in range(1,11)}
print(squares)
