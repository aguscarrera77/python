from flask import Flask,render_template,request,url_for,redirect
import csv
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
    #guardo los datos de los valores de la funcion en txt.
    #guardo tambien los valores en un archivo csv.
    with open('datos.txt','a')as f:
        f.write(f"{nombre}-{edad}-{fono}\n")
    with open("datos.csv","a",newline="")as archivo:#a:append,newline: nueva linea evita registro vacios.
        writer=csv.writer(archivo) # type: ignore
        writer.writerow([nombre,edad,fono]) # type: ignore
    
    return redirect("/recepcion")
    #perfiles.append({'nombre':nombre ,'edad':edad ,'fono':fono})
    #return redirect(url_for('ver_lista'))




#guardar los datos en lista. usando la propieda append.

#reedireccionar la lista perfiles a la nueva pagina de html: recepcion.


@app.route('/recepcion')
def lista():
    datos=[]
    with open("datos.txt",'r') as f:
        datos=f.readlines()
    return render_template("recepcion.html",datos=datos)       






if __name__=='__main__':
    app.run(debug=True)
    



