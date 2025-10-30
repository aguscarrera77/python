import pandas as pd 
#Voy a usar la biblioteca pandas para ordenar en celdas los valores de este diccionario. Usamos la propiedad DATAFRAME.
dato={
'Nombre':['Agustin','Carlos','Gerardo','Martin','Santino','Gabi'],
'Edad':[24,87,98,52,20,32],
'Ocupacion':['instructor','conductor','conductor','speaker','hijo','paseadora de perros']

}

tabla= pd.DataFrame(dato)
print(tabla)
#Mostrar una sola columna.

print(tabla['Ocupacion'])
#ejemplo de promedio.
print(tabla['Edad'].mean())

#Ubicacion dentro de la grilla.
print(tabla["Nombre"][2])# Columna Nombre y la ubicacion 2.
#mostrar primeras filas.

print(tabla.head(2))
print(tabla.tail(1))


#filtrar datos.

menores_52=tabla[tabla['Edad']<=52]

print(menores_52)

#filtrar con varias condiciones.

doscondiones=tabla[(tabla["Edad"]>52) & (tabla["Ocupacion"]=='conductor')]

print(doscondiones)

condiciones=tabla[(tabla['Nombre']=='Martin') | (tabla['Ocupacion']=='futbolista')]
print(condiciones)

# mostrar valores todos menos algun valor.

print(tabla[~(tabla['Ocupacion']=='conductor')])

#mostrar entre valores o rango de valores.

print(tabla[tabla['Edad'].between(10,35)])

#Nueva columna.

tabla['Ciudad']=['Buenos Aires','Rosario','Pilar','Pergamino','Rio de Janeiro','Puan']
print(tabla)

#Editar una columna.

tabla['Edad']=tabla['Edad']+5

print(tabla)