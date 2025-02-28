db = db.getSiblingDB('apirest2');

db.createCollection('productos');

db.productos.insertMany([
    { "nombre": "Producto 1", "precio": 10 },
    { "nombre": "Producto 2", "precio": 20 }
]);
