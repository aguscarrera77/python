import requests

url='https://dolarapi.com/v1/dolares'

respuesta=requests.get(url)

if respuesta.status_code==200:
    datos=respuesta.json()
    for dolar in datos:
        print(f"Variables de dolar {dolar['nombre']}:compra {dolar['compra']}-venta{dolar['venta']}")
else:print("Error de conexion al servidor: ",respuesta.status_code)

url="https://dolarapi.com/v1/dolares/blue"
r=requests.get(url)
if r.status_code==200:
    d=r.json()
    print(f"Dolar Blue hoy: compra {d['compra']}- venta p{d['venta']}")
else:print('Error de conexion al servidor vuelva mas tarde ',r.status_code)