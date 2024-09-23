from flask import Flask, render_template, redirect
import mysql.connector
conexion=mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="esquemabrido"
)
cursor=conexion.cursor()

app = Flask(__name__)



@app.route('/')
def index():
   return render_template('index.html')
@app.route('/clientes')
def clientes():
   return render_template('clientes.html')


@app.route('/inicio')
def inicio():
   return redirect('/')


@app.route('/cargarclientes.html')
def cargarclientes():
   return render_template('cargarclientes.html')



if __name__ == '__main__':
   app.run(debug=True)
