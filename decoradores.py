def decorador(func): #A(B)
    def before_action():
        print('Vamos a ejecutar la funcion')

    def after_action():
        print('Se ejecuto la funcion')
    def nueva_funcion(*args, **kwargs):
        #Antes de ejecutar agregar mas funcionalidad
        before_action()
        resultado = func(*args, **kwargs)
        #Despues de ejecutar agregar mas funcionalidad
        after_action()
        return resultado
    return nueva_funcion #C (retorna la funcion no la ejecuta)

@decorador #Decorar una funcion
def saluda():
    print('Hola mundo')

@decorador
def suma(num, num2):
    return (num+num2)

#Decorador es una funcion que recibe una funcion y regresa otra funcion
#A recibe B para poder crear C
if __name__ == '__main__':
    saluda()
    result =  suma(20,10)
    print(result)
