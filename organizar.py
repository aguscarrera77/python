import os
import shutil

#CCrear una carpeta llamada textos.

carpeta_actual=os.getcwd()
print('trabajando es esta carpeta',carpeta_actual)

#Crear la carpeta que recibe los archivos.

os.makedirs('Textos',exist_ok=True)

#mover los arhivos.

for archivo in os.listdir():
    if archivo.endswith('.txt'):
        shutil.move(archivo,'Textos')
        print('Archivo movido: ',archivo)





    

