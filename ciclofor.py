#Ciclo For: repite un bloque codigo una vez por cada elemento que itere.
frutas=['pera','frutilla','manzana']

#for f in frutas:
#    print(f)

#range nos devuelve un listado de esa coleccion de elementos. range(inicio,final,paso)inicio es donde se comienza a contar listado, final es donde corta el listado (no figura en la terminal)y el paso es por si yo quiero hacer un salto en ese listado.

for i in range(5):
    print(i)

for r in range(1,10):
    print(r)

for x in range(0,10):
    print(x)

for n in range(10,1,-1):
    print(n)

#Ejemplos que podes usar en programacion web.

for h in range(1,5):
    print(f"<h1>Secciones {h}</h1>")


for conexion in range(3):
    print(f"Intento de conexion al servidor {conexion + 1}")

deportes=['golf','rugby','basket']

for deporte in range(len(deportes)):
    print(deporte,deportes[deporte])

#enumarate chequea y trae segun el indice que tienen las colecciones. Sintaxis: for indice,item in enumerate(iterable,start=0)

prendas=['short','buzo','remera','boxer']

for indice,prenda in enumerate(prendas):
    print(indice,prenda)

for i,prenda in enumerate(prendas,start=1):
    print(i,prenda)

#zip recorrer dos listas o mas al mismo tiempo.Sintaxis for a,b in zip (lista1,lista2)

names=['Agustin','Meli','Caro']
edades=[39,52,56]

for name,edad in zip(names,edades):
    print('nombre',name,'edad',edad)

sports=['basket','tenis','futbol']
horarios=[18,20]

for sport,horario in zip(sports,horarios):
    print(sport,horario)

#Ejemplos de Progamacion.
#Ecommerce nombre producto y el valor del producto.

productos=['Iphone17','Samsung Edge','Nokia 1100']
precios=[1100,800,100]

for producto,precio in zip(productos,precios):
    print(f"<li>Nombre del producto: {producto} Precio: {precio}</li>")

#Recorrer con for los diccionarios.

perfiles={'nombre':'Agustin','edad':47,'Profesion':'Instructor'}

#Solo las claves.

for clave in perfiles:
    print(clave)

#claves y valores a la vez: items()

for clave,valor in perfiles.items():
    print(clave,'su valor es',valor)

#solo valores values().

for valor in perfiles.values():
    print(valor)


from flask  import requests


ver_form():

for campo,valor in requests.form.items():
    print(campo,valor)

# input name='nombre'
#input name='email'

# nombre : Roberto
# email: robertogalan@gmail.com