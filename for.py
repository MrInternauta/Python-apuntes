# -*- coding: utf-8 -*-
print(range(1,40, 1))
for i in range(5):
    print (i)

for i in range(5):
    print ('Hola')

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)


for i in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        print('Exit')
        break
print('\n')
for i in range(0, 30, 1):
    print(i)
    if i == 20:
        break
print('\n')
for i in range(30, 0, -1):
    print(i)
    if i == 20:
        break

print('\n')
my_string = 'felipe'
for i in range(0, len(my_string), 1):
    print(my_string[i])

print('\n')
my_string = 'felipe'
for i in my_string:
    print(i)
