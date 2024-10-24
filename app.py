from flask import Flask, render_template, redirect, request
import mysql.connector
conexion=mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root",
      database="esquemabrido",
      
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



@app.route('/cargarclientes')
def cargarclientes():
   return render_template('cargarclientes.html')
@app.route('/modificarclientes')
def modificarclientes():
   return render_template('modificarclientes.html')

@app.route('/cargar',methods=['POST'])
def cargar():
   
   nombre=request.form.get('Nombre')
   cant=request.form.get('CantidadArt')
   articulo=request.form.get('Articulos')
   direccion=request.form.get('direccion')
   query=f"INSERT INTO cliente(NombreApellido) values('{nombre}');"
   cursor.execute(query)
   print(nombre,"\n",cant,"\n",articulo,"\n",direccion)
   return redirect('/')
   


if __name__ == '__main__':
   ascii_art = """
███████ ███████ ██████  ██    ██ ███████ ██████      ██ ███████      ██████  ███    ██ 
██      ██      ██   ██ ██    ██ ██      ██   ██     ██ ██          ██    ██ ████   ██ 
███████ █████   ██████  ██    ██ █████   ██████      ██ ███████     ██    ██ ██ ██  ██ 
     ██ ██      ██   ██  ██  ██  ██      ██   ██     ██      ██     ██    ██ ██  ██ ██ 
███████ ███████ ██   ██   ████   ███████ ██   ██     ██ ███████      ██████  ██   ████
"""

   print(ascii_art)
   app.run(host='0.0.0.0',port=5000,debug=True)
