from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)
#lista de datos. Simulamos base de datos.
perfiles=[]
@app.route('/')
def inicio():
    return render_template("index.html")
@app.route('/agregar',methods=['POST'])
def agregar():
    nombre=request.form['nombre']
    edad=request.form['edad']
    fono=request.form['fono']
    perfiles.append({'nombre':nombre ,'edad':edad ,'fono':fono})
    return redirect(url_for('ver_lista'))



#guardar los datos en lista. usando la propieda append.

#reedireccionar la lista perfiles a la nueva pagina de html: recepcion.


@app.route('/recepcion')
def ver_lista():
    return render_template('recepcion.html',perfiles=perfiles)

if __name__=='__main__':
    app.run(debug=True)
    



