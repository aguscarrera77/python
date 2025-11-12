from flask import Flask,render_template
app=Flask(__name__)
#@app.route('/')
#def inicio():
 #   return render_template("index.html")
@app.route('/saludar')
def saludo():
    return render_template("saludar.html")

@app.route("/usuario/<nombre>")
def perfil(nombre):
    nombre='Agustin'
    return render_template("usuario.html",nombre=nombre)

@app.route('/')
def curso():
    datos={
        "nombre":"Agustin",
        "curso":'Python',
        "nota":10
    }
    return render_template("index.html",info=datos)


if __name__=="__main__":
    app.run(debug=True)
