import requests

#request es un modulo de python que nos permite trabajar mejor con internet. Usamos para conectarnos estructuras externas.
#Metodos que nos permiten hacer por ej estas consultas.
#GET: Obtener datos de un servidor.
#POST: Enviar datos al servidor.
#PUT: Actualiza datos. Cambiando o editando algu dato ya existente.
#DELETE: Es para borrar algun dato o registro remoto.
print(requests.__version__)

url="https://jsonplaceholder.typicode.com/users"

respuesta=requests.get(url)

if respuesta.status_code==200:
    datos=respuesta.json() #convertir los datos de Json a diccionario.
    for usuario in datos:
        print(usuario["name"],"-",usuario["email"])
else: print("Error al recibir datos del servidor externo: ",respuesta.status_code)


#print('Codigo de estado de conexion: ',respuesta.status_code)
#print("El contenido: ")
#print(respuesta.text)
#Metodo Post que era el que enviaba datos.

nuevo_post={
"titulo":'Mi primer envio post',
"cuerpo":'Este es mi contenido de prueba.',
"idUsuario":1
}

respuesta=requests.post(url,json=nuevo_post)
#json=nuevo_post significa transformar el diccionariod de python en json que es como lo esta guardando el servidor.
print('Codigo: ',respuesta.status_code)
print("Respuesta del servidor ")
print(respuesta.json())

#PUT se envian datos para modificar un post ya enviado.

print("\n=== PUT:Actualice el post existente")
post_actualizado={
    'idUsuario':1,
    'titulo':"Titulo Actualizado",
    'cuerpo':"Este posta a sido modificado",
    'id':1
}

respuesta=requests.put(f"{url}/1",json=post_actualizado)
print('Codigo: ',respuesta.status_code)
print('Respuesta:',respuesta.json())

#DELETE borra un post.

respuesta=requests.delete(f"{url}/1") # indico que busque la marca 1 que es la que deje en el post_actualizado.
#https://jsonplaceholder.typicode.com/post/1
print('Codigo: ',respuesta.status_code)
print('Respuesta ',respuesta.text)#el cuerpo de la repuesta esta vacia porque el post fue borrado.