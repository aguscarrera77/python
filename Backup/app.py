from flask import Flask
app=Flask(__name__)#creamos una app nueva en flask.app es una variable que tiene como objeto principal marcar una nueva app.
#__name__  propiedad de python y guarda el nombre del archivo.Flask busca en ese nombre el desarrollo de las plantillas.
#rutas.
@app.route('/') #abriendo una ruta que me permite a partir del caracter / entrar el url y todo lo viene despues se ejecuta.
def inicio():
    return "Hola a todos esto es python."
@app.route('/contacto')
def contacto():
    return "Contacto."

@app.route('/html')
def pagina_html():
    return "<h1>Bienvenido estoy usando flask con html.</h1>"

@app.route('/usuario/<nombre>')
def saludar(nombre):
    return f"Hola bienvenido: {nombre}  a tu carpeta local."

if __name__=="__main__":#name guarda el nombre del archivo si es extremadamente igual a main se ejecuta la app.
    app.run(debug=True)# hace correr el programa se ejecuta en el servidor local.



