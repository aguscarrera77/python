# trabajar con la biblioteca os que significa system operation es el sistema de trabajo desde la terminal.
import os

def sistema():
    print('Sistema operativo: ', os.name)# me devuelve el nombre del sistema operativo.
    print('La carpeta de trabajo Actual es: ', os.getcwd())#llamo a la carpeta que estoy laburando ahora mismo. 
    #getcwd get current working directory. Te muestra la ruta de la carpeta actual.

#Voy a crear una carpeta nueva en mi carpeta python.
print('Carpeta Actual', os.getcwd())
print('Creo una carpeta nueva llamada Backup')

os.makedirs('Backup',exist_ok=True)

#Voy a mostrar el contenido de la carpeta listdir().

print('La carpeta contiene los siguientes objetos: ', os.listdir())

#cambiar de carpeta o sea cambiar la ruta de trabajo.chdir()

os.chdir('Backup')

print('La nueva carpeta donde estoy laburando es ',os.getcwd())

