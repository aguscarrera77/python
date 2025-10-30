import requests
print(requests.__version__)

url="https://jsonplaceholder.typicode.com/users"

respuesta=requests.get(url)

print('Codigo de estado de conexion: ',respuesta.status_code)