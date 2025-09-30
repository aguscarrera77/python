#print('hola mundo') 
#edad = 35
#experiencia= 4

#nombre='Agustin'
#profesion='Instructor'

#enviado=True
#noenviado=False

#print('Mi edad es',edad)
#print('Mi tiempo de laburo',experiencia)
#print("Mi nombre es ",nombre)
#print("Soy ",profesion)
#print('Enviado',enviado)
#print('No enviado',noenviado)

#Concatenar y mostrar el texto

#nombre='Roberto'
#edad=30

#Concatenar con comas.

#print('Hola soy ',nombre,'como estas? y tengo',edad)

#Concatenar con el signo +

#print('Hola soy '+ nombre + ' como estas? y tengo '+ str(edad))

#Operaciones Matematicas.

#a=10 #int
#b=3 #int
#c=2.5 #float

#print('Suma', a+b)
#print('Resta', a-b)
#print('Multiplacion', a*b)
#print('Division',round ((a/b),2))#decimal
#print('Division entera',a//b)
#print('Resto',a%b)
#print('Potencia',a**b )
 
#Combinar operaciones.

#total=(a-b)**b

#print('Calculo total',total)

#name='JA'*5

#print(name)

#Conversiones de valores.

#age= input('Mi edad es')

#print(type(age))

#edades=int(input('Ingresa tu edad: '))
#print('El ano que viene tendras ',edades + 1)

#altura=float(input('Cuanto medis en metros:'))

#print('tu altura en centimetros es',altura*100)

#numero=30

#print("el numero es "+ str(numero))

#Combinar input.

#numero1=int(input('Ingrese un numero '))
#numero2=int(input('Ingreso un numero '))

#print(numero1+numero2)

#Area 
#base=float(input('Ingrese la base de su triangulo '))
#altura=float(input('Ingrese la altura de su triangulo'))
#area=float((base*altura)/2)

#print('El area de su triangulo es :',area)


#number=10

#print(number>8)
#numeros mayores a 0 y pares
#num=50
#num1=45
#print(num>0 and  num%2==0)
#print(num1>0 and num1%2==0)

#Usuario sean mayor o igual a 18 y que sea usuario.

#usuario=True
#edad=17
#mensaje={True:'Usted es usuario y tiene mas de 18',False:'Usted no cumple las condiciones'}
#print(mensaje[usuario and edad>18])

#Comparar 3 numeros y determinar que al menos 2 sean iguales

#a=3
#b=5
##c=3

#print((a==b)or(a==c)or(b==c))

#numero=int(input('Ingrese un numero'))

#print(numero>100)

#x=int(input('Ingreso un numero mayor a 0'))
#y=int(input('Ingrese numero menor a 100'))

#print(x>=y)

#verificar un password

#clave=input('Su password es:')

#print(clave=='agus') 

#Transformar letras.

#letra=input('Ingrese vocales').lower()

#print(letra in 'aeiou')

#dos condiciones para poder anotarse a un curso. Si es o no estudiante y si es mayor a 21.

#estudiante= input('Sos estudiante?(s/n)').lower()
#edad=int(input('Que edad tenes?'))

#print(estudiante== 's' and edad>=21)

#Primer if genera una condicion esa condicion es true se imprime el codigo si es false no se imprime el codigo genero una respuesta con el metodo else para salvar el false.

age=20

if age>20:
    print('Es mayor a 18')
else:
     print('Es menor a 18')

#elseif es generar una condicion mas al if.

nota=45

if nota>=90:
     print('Su nota es Excelente')
elif nota>=70:
     print('Esta aprobado.')
else:
     print('Usted va a recuperatorio')

#combinamos condicionales con operadores (and or not)

edad=40
anotado_curso=False

if edad>=18 and anotado_curso:
     print('Usted es mayor a 18 y esta anotado')
elif edad>=18 and not anotado_curso:
     print('Es mayor pero no esta anotado')
else: 
    print('Usted es menor,necesita autorizacion')

#Combinar condiciones con or y dos booleanos.

llueve=True
uso_paraguas= False

if llueve or uso_paraguas:
     print('Me mojo')
else:
    print('Salio el sol no me voy a mojar')


#usar not ....invierte el valor de la condicion.

conectado=False #False 

if not conectado:
     print('No estas conectado')#not conectado es true.if se imprime.
else:
     print('Estas conectado.')

#Mezclar and or not.

#edad= 17
#tiene_permiso=True
#acompanado=True

#if(edad>=18 or tiene_permiso) and not acompanado:
    # print('Puedo conducir') 
#else:
     #print('No puedo conducir')

#Operacion matematica dentro del condicional
#edad=int(input('Ingrese la edad'))
#jubilacion=65 - edad

#if edad<65:
     #print(f'Te faltan {jubilacion} anos para jubilarte'.upper())
#else:
    #print('ya podes jubilarte')
#METODOS DE CADENA.

#1.LOWER es convertir el string en minisculas.

name='PYTHON'

print(name.lower())

#de forma directa un metodo.

print('HOLA ESTOY HACIENDO EL CURSO'.lower())

#upper es mayuscula.

nombrado='agustin'
print(f'Mi nombre es {nombrado.upper()}')

#title transforma en mayusculas la primera letra de las palabras que componen el string.

frase='mi buenos aires querido.'
print(f'el tango se llama: {frase.title()}')

#strip quitar espacios.

password='   hola.    '
print(password.strip())

#replace reemplaza texto del string.

lenguaje='Me gusta usar Java.'

print(f'Cambio mi lenguaje {lenguaje.replace("Java","Python")}')

#split elijo el caracter que voy a usar para separar los elementos de la lista.

colores='Rojo,negro,blanco'
print(colores.split(','))

#find buscar la posicion de un caracter.
palabra='Estoy aprendiendo Python'

#variable
print(palabra.find('Python'))
#f string
print(f"Posicion de thon {palabra.find('thon')}")
#directamente.
print("banana ".find('na'))

#count cuenta los caracteres.

frutas= 'frutilla'

#variable.
print(frutas.count('o'))

#directo

print('otorrinolaringologo'.count('o'))

#lista colecciones de valores ordenadas y mutables.

fruta=['anana','melon','pera',3]
print(fruta)

print(fruta[0])
print(fruta[-1])#trae el ultimo valor de la lista.

#agregar un valor a la lista.

fruta.append('sandia')#agrega al final de la lista.
fruta.insert(1,10) #insert elegimos primero la posicion coma el elemento a insertar.
print(fruta)

#elimino elementos de la lista.

fruta.remove('pera')#remove elimina un elemento con su nombre.Al primero que coincide.
print(fruta)

borrar=fruta.pop(0)#borra por indice.
print(borrar)
print(fruta)

#tuple grupo de elementos que estan ordenados pero no se pueden modificar.

numbers=(10,20,30,40)#Sintaxis entre parentisis.
print(numbers[-1])#busco por indice.

#Combinamos listas y tuple

coordenadas=[(0,0),(1,1),(2,2),(3,3)]
print(coordenadas[0])
print(coordenadas[2][0])

coordenadas.append((4,4))
print(coordenadas)







