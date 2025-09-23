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
    