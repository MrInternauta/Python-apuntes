#ventas * mes
meses = [1,2,3,4,5,6]
venta = [7000,9000,5000,11000,10000,13000]
productos = []
suma = 0
suma_all_venta = 0
suma_mes=0
suma_num_mes = 0
mes_pow =0
for idx, mes in enumerate(meses):
    mes_pow += mes**2
    suma_num_mes += mes
    suma_all_venta +=venta[idx]
    suma_mes = venta[idx] * mes
    suma += suma_mes
    productos.append(suma_mes)

print(suma)
print(suma_all_venta)
print(suma_num_mes)
print(mes_pow)
