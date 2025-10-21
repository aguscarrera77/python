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

# Return con varias variables. Multiples retornos.

#def operaciones(a,b):
    #suma= a + b
    #resta= a - b
    #producto= a * b
    #division= a/b
    #print(f"Suma:{suma},Resta:{resta},Multipliacion:{producto},y divide: {division}")
    #return suma,resta,producto,division

#operaciones(10,2)

#w,x,y,z= operaciones(20,4)

#print(y)

#def datos_alumno(apellido,nota):
    #aprobado= nota>=70
    #return apellido,nota,aprobado

#nombre,nota,estado= datos_alumno('Agustin',70)
#print(nombre,'-','Aprobado' if estado else 'Desaprobado')

#def datos_alumnos(nombre,nota):
    #if nota >=70:
        #condicion='Aprobado'
    #else: condicion='Desaprobado'
    #return {
        #'nombre':nombre,
       # 'nota':nota,
        #'estado':condicion,
   # }

#alumno=datos_alumnos('Carlos',65)
#alumno1=datos_alumnos('Roberto',70)
#print(f"{alumno['nombre']}-{alumno['estado']}")
#print(f"{alumno['nombre']}-{'Aprobado' if alumno['aprobado']else 'Desaprobado'}-{alumno['nota']} ")
#print(f"{alumno1['nombre']}-{'Aprobado' if alumno1['aprobado']else 'Desaprobado'}  ")

# parametro definido. Multiples retornos. Cambio en el valor de la moneda.

def convertir_moneda(pesos,dolar=1000):
    en_dolares=pesos/dolar
    en_euros=pesos/(dolar*1.10)
    return en_dolares,en_euros

usd,eur=convertir_moneda(20000,1500)
print('Son dolares',usd)
print('Son euros',eur)



#funciones lambda funciones anonimas. Aquellas que no tienen nombre. Son funciones simples de poco codigo. 
#Sintaxis es lambda argumento: expresion.

doble= lambda x: x*2

print(doble(10))

adicion= lambda a,b: a+b

print(adicion(10,4))

mayor=lambda a,b: a if a>b else b 
print(mayor(10,5))
print(mayor(4,8))

#Lambda sin argumentos.

hi= lambda: 'Hola a todos'
print(hi())

#map() aplicar la funcion a cada elemento.

numeros=[1,2,3,4]

doblete=list(map(lambda x:x*2,numeros))
print(doblete)

#filter filtra elementos que cumplen con una condicion.

numeros1=[1,2,3,4,5]
pares=list(filter(lambda x:x%2==0,numeros1))

print(pares)

#sorted. ordenar de acuerdo a un criterio. Vamos usar un diccionario y ordenados de acuerdo a una key.

persons=[('Carlos',104),('Roberto',98),('Agustin',48),('Lucas',30)]

personas_ordenadas= sorted(persons,key=lambda x:x[1])
print(personas_ordenadas)



#Docstring dentro de la funcion dar una explicacion de lo que hace esa funcion.

def recibimiento(name):
    """ Saludar con un nombre """
    return "hola" + name

print(recibimiento('Carolina'))
print(recibimiento.__doc__)
















