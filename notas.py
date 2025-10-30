import pandas as pd
notas={
'Alumno':['Roberto','Mario','Alberto','Sofia'],
'Nota':[90,87,100,55]
}

df=pd.DataFrame(notas)

promedio=df['Nota'].mean()
print("Promedio General: ",promedio)

aprobados=df[df['Nota']>=70]
print('\nAprobados')
print(aprobados)
ruta=r"C:\Users\acerd\OneDrive\Desktop\alumnos.csv"
#guardar resultados.

aprobados.to_csv(ruta,index=False)