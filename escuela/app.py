from flask import Flask,request,render_template,redirect,url_for,flash
import sqlite3

app=Flask(__name__)
app.secret_key="clave_secreta_1234"

#Conexion y creacion de una base de datos.la funcion propia de python get_db conecta a la base de datos.
def get_db():
    conn=sqlite3.connect('escuela.db') #creo la base de datos.
    conn.row_factory=sqlite3.Row
    return conn
#crear la tabla de datos.

with get_db() as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS  estudiantes( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre text not null,
        apellido text not null,
        edad integer not null,
        grado text not null)
""")#comando CREATE crea estructuras en sql por ej una base de datos, una tabla. Los tipos de valores que usan las bases de datos son los enteros, text (strings), boleanos y float para decimales.
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/agregar",methods=["GET","POST"]) #metodos procesan el envio del formulario(post) y muestra el formulario en la pagina por pedido de get.
def agregar():
    if request.method=="POST":#compruebo si la solicitud es post o no. el usuario lleno los datos y envio el formulario.
        nombre=request.form['nombre'].strip()
        apellido=request.form['apellido'].strip()
        edad=request.form['edad'].strip()
        grado=request.form['grado'].strip()
        #validar linea por linea
        if len(nombre)<2:
            flash("El nombre debe tenar 2 o mas caracteres.","error")
            return redirect(url_for("agregar"))
        if len(apellido)<2:
            flash("El apellido debe tener 2 o mas caracteres","error")
            return redirect(url_for("agregar"))
        if not edad.isdigit(): 
            flash("Introducir numero entero.",'error')
            return redirect(url_for("agregar"))
        edad=int(edad)
        if edad <18 or edad>110:
            flash("Edad permitida mayores a 18.",'error')
            return redirect(url_for("agregar"))
        if len(grado)<1:
            flash("El grado no puedo estar vacio.","error")
            return redirect(url_for("agregar"))
        with get_db() as db:
            db.execute(
            "INSERT INTO estudiantes(nombre,apellido,edad,grado) VALUES (?,?,?,?)",(nombre,apellido,edad,grado))#Ejecuta la insersion de los valores.
        db.commit()
        flash("Estudiante agregado correctamente.",'exito')
        return redirect(url_for('ver_estudiantes'))
    return render_template("agregar.html")

@app.route("/ver")
def ver_estudiantes():
    db=get_db()
    estudiantes= db.execute("SELECT * FROM estudiantes").fetchall()
    return render_template("ver.html",estudiantes=estudiantes)

@app.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):
    db=get_db()
    if request.method== "POST":
        nombre=request.form["nombre"]
        apellido=request.form["apellido"]
        edad=request.form["edad"]
        grado=request.form["grado"]
        db.execute("UPDATE estudiantes SET nombre=?,apellido=?,edad=?,grado=? WHERE id=?",(nombre,apellido,edad,grado,id))
        db.commit()
        db.close()
        return redirect(url_for("ver_estudiantes"))
    estudiantes=db.execute("SELECT * FROM estudiantes WHERE id=?",(id,)).fetchone()
    return render_template('editar.html',e=estudiantes)
    
@app.route("/eliminar/<int:id>")
def eliminar(id):
    db=get_db()
    db.execute("DELETE FROM estudiantes WHERE id=?",(id,))
    db.commit()
    return redirect(url_for("ver_estudiantes"))

if __name__=="__main__":
    app.run(debug=True)












        

    