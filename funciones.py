#funciones son bloques de codigo con nombre y que pueden ser reutilizadas en cuelquier parte del codigo.
#primera funcion saludar sin parametros ni returno.
def saludar():
    print('Hola a todos')
saludar()
saludar()

#Funcion con parametros: los parametros son argumentos que tienen las funciones que me permiten pasarles valores.

def sumar(a,b):
    resultado=a + b
    return resultado
    


suma=sumar(10,4)
print(suma)

#Valores defecto.

def perfil(nombre,saludo='hola'):
    print(f"{saludo},soy {nombre}")

perfil('Carlos')
perfil('Lucas')
perfil('Guillermo')
perfil('Melisa','Hello')
