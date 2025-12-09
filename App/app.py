from flask import Flask,render_template
app=Flask(__name__)
#@app.route('/')
#def inicio():
 #   return render_template("index.html")
#@app.route('/saludar')
#def saludo():

def perfiles():
    alumnos=[
    {"nombre":"Roberto","nota":10},
    {"nombre":"Lucas","nota":7},
    {"nombre":"Gabi","nota":4},
    {"nombre":"Martin","nota":1}
    ]
    return render_template('index.html',alumnos=alumnos)


if __name__=="__main__":
    app.run(debug=True)
