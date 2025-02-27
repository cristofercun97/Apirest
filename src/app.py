from flask import Flask, jsonify, request
from config import Config
from flask_mysqldb import MySQL
from flask_pymongo import PyMongo

# Instancias 
app = Flask(__name__) 
app.config.from_object(Config)

mysql = MySQL(app)
mongo = PyMongo(app)

# Rutas
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API funcionando'})

@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.json 
    nombre_producto = data.get('nombre_producto', 'Desconocido')
    precio = data.get('precio', 0)
    cantidad = data.get('cantidad', 0)

    # Agregar a la base de datos de MySQL 
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO productos(nombre_producto, precio, cantidad) VALUES(%s, %s, %s)', 
                       (nombre_producto, precio, cantidad))
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
        return jsonify({'error': f'Error al insertar en MySQL: {str(e)}'}), 500

    # Agregar a la base de datos de MongoDB
    try:
        mongo.db.productos.insert_one({
            'nombre_producto': nombre_producto,
            'precio': precio,
            'cantidad': cantidad
        })
    except Exception as e:
        return jsonify({'error': f'Error al insertar en MongoDB: {str(e)}'}), 500

    return jsonify({'message': 'Producto agregado correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
