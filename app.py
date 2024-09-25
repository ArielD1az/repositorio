from flask import Flask, render_template, redirect
import mysql.connector
conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root",
      database="esquemabrido"
)
cursor=conexion.cursor()

app = Flask(__name__)
#
@app.route('/prueba')
def prueba():
   query="SELECT * FROM cliente"
   cursor.execute(query)
   clientes=cursor.fetchall()
   print("prueba: ",clientes)
   return render_template('index.html')

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
   app.run(host='0.0.0.0',port=5000,debug=True)
