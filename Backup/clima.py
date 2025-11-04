import requests

api_key='3241777d5fc1784b3d223f9bb0ecc4d9' #mi api key generada en la url weathermap.

ciudad=input("Ingresa el nombre de la ciudad: ")

#llamo url.

url= f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

respuesta=requests.get(url)

if respuesta.status_code==200:
    datos=respuesta.json()
    #Mostrar datos.
    nombre=datos["name"]
    temperatura=datos['main']["temp"]
    humedad=datos['main']['humidity']
    viento=datos['wind']['speed']
    descripcion=datos['weather'][0]['description']

    print('\n Clima en ',nombre)
    print("Temperatura: ",temperatura)
    print('Humedad: ',humedad)
    print('viento',viento)
    
    print('Descripcion del tiempo: ',descripcion.capitalize())
else:print("Error al consultar el clima Codigo de error: ",respuesta.status_code)
