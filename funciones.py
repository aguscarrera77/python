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
perfil('Charles','Hi')

#Funciones combinan acciones y retorno.

def promedios(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    print('El promedio del resultado es:', promedio)
    return promedio

resultado= promedios(10,14,2)
print('Ahora el resultado se muestra:',resultado)

#Funcion con return y sin return.
#Sin return.

def calcular_iva(precio):
    precio_total= precio * 1.21
    print(f"El precio final del producto es:${precio_total}")

calcular_iva(100)

#Version con return.

def calculadora_iva(valor):
    total_precio=valor * 1.21
    return total_precio

total= calculadora_iva(100)
print(total)

precio1=calculadora_iva(200)
precio2=calculadora_iva(800)
total_compra_con_iva= precio1 + precio2
print('El total de la compra con iva es:',total_compra_con_iva)

#Funciones print y return. print muestra return devuelve resultado.

def compra_descuento(importe,descuento):
    descuentos= importe*(descuento/100)
    total=importe-descuentos
    print(f"El producto queda con descuento a este precio:${total} y el descuento que te otorgo Visa es de:${descuentos}")
    return total

importe_producto= compra_descuento(100,20)

compra_descuento(200,40)

# Return con varias variables.

def operaciones(a,b):
    suma= a + b
    resta= a - b
    producto= a * b
    division= a/b
    print(f"Suma:{suma},Resta:{resta},Multipliacion:{producto},y divide: {division}")
    return suma,resta,producto,division

operaciones(10,2)

w,x,y,z= operaciones(20,4)

print(y)

def datos_alumno(apellido,nota):
    aprobado= nota>=70
    return apellido,nota,aprobado

apellido,nota,estado=datos_alumno()



print(apellido,"-",'aprobado' if estado else 'desaprobado')




