import pandas as pd
ruta=r"C:\Users\acerd\OneDrive\Desktop\alumnos.csv"
db=pd.read_csv(ruta)
print(db)
print(db.head(3))
print(db["notas"])