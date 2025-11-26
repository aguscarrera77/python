from flask import Flask,request,render_template,redirect,url_for
import sqlite3

app=Flask(__name__)

#Conexion y creacion de una base de datos.la funcion propia de python get_db conecta a la base de datos.
def get_db():
    conn=sqlite3.connect('escuela.db')
    conn.row_factory=sqlite3.Row
    return conn
#crear la tabla de datos.

with get_db() as db:
    db.execute("""
CREATE TABLE IF NOT EXIST estudiantes(
               id INTEGER PRIMARY KEY AUTO INCREMENT,
               nombre text not null,
               apellido text not null,
               edad intenger not null,
               grado text not null)
""")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/agregar",method=["get"] ["post"])
def agregar():
    if request.method=="post":
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        edad=request.form['edad']
        grado=request.form['grado']
        db=get_db()
        db.execute(
            "INSERT INTO estudiantes(nombre,apellido,edad,grado) VALUES (?,?,?,?)",(nombre,apellido,edad,grado))
        db.commit()
        return redirect(url_for('/ver'))
    return render_template("agregar.html")

@app.route("/ver")
def ver_estudiantes():
    db=get_db()
    estudiantes= db.execute("SELECT * FROM estudiantes").fetchall()
    return render_template("ver.html",estudiantes=estudiantes)









        

    