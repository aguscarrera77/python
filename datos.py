import pandas as pd 
#Voy a usar la biblioteca pandas para ordenar en celdas los valores de este diccionario. Usamos la propiedad DATAFRAME.
dato={
'Nombre':['Agustin','Carlos','Gerardo'],
'Edad':[24,87,98],
'Ocupacion':['instructor','cantautor','conductor']

}

tabla= pd.DataFrame(dato)
print(tabla)
#Mostrar una sola columna.

print(tabla['Ocupacion'])