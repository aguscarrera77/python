#Parametros variables: no sabemos cuantos parametros va a recibir la funcion.
#args sintaxis * antes del nombre del argumento. Organiza los valores que traen los parametros en una tupla.
def sumar (*argumentos):
    print('La suma de los valores pasados por los parametros argumento: ',argumentos)
    return sum(argumentos)

print(sumar(8,4))
print(sumar(10,20,34,43,50))

#kwargs recibe los valores los parametros variables en diccionario. No saber ni que cuantas key ni cuantos valores de esas key van a pasar por esa funcion. Sintaxis **

def mostrar_perfil(**kwargs):
    print ('Los datos del perfil son: ',kwargs)
    for clave,valor in kwargs.items(): #clavo valor traen los valores del tandem key:value.
        print(f"{clave}:{valor}")

mostrar_perfil( nombre="Carlos", edad=140,ciudad="Buenos Aires",profesion='El zorzal criollo')

#Sistema de registro de empleados. Soy un RRHH. Combinando args y kwargs.

def registro_empleados(*args,**kwargs):
    #args van a definir nombre edad apellido etc
    print('Datos principales del Empleado: ',args)
    #kwargs seran datos adicionales.
    print('Datos adicionales: ')
    for key,value in kwargs.items():
        print(f"  -{key}:{value}")

    print('Empleado registrado exitosamente \n')



registro_empleados('Roberto','Galan',98,"Gerente",sector='Ventas',antiguedad=45,ciudad='Pergamino')
registro_empleados('Monica','Gonzaga',telefono=244587575)
registro_empleados('Tomas',45,"Empleado",mail= 'tomas@gmail.com')









