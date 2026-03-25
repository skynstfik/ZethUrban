from flask import Flask, render_template, request, jsonify, session
import json

app = Flask(__name__)
app.secret_key = 'zethurban_secret_2024'

# Base de datos simulada de productos
PRODUCTOS = [
    {"id": 1, "nombre": "Hoodie ZethUrban Classic", "categoria": "Ropa", "precio": 29990, "talla": ["S", "M", "L", "XL"], "imagen": "https://images.unsplash.com/photo-1556821840-3a63f15732ce?w=400&h=500&fit=crop", "descripcion": "Hoodie urbano de algodón premium"},
    {"id": 2, "nombre": "Pantalón Cargo Street", "categoria": "Pantalones", "precio": 34990, "talla": ["28", "30", "32", "34"], "imagen": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=500&fit=crop", "descripcion": "Cargo con bolsillos laterales estilo urbano"},
    {"id": 3, "nombre": "Polera Oversize Urban", "categoria": "Ropa", "precio": 19990, "talla": ["S", "M", "L", "XL"], "imagen": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=500&fit=crop", "descripcion": "Polera oversize fit con diseño minimalista"},
    {"id": 4, "nombre": "Pantalón Jogger ZU", "categoria": "Pantalones", "precio": 27990, "talla": ["S", "M", "L", "XL"], "imagen": "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?w=400&h=500&fit=crop", "descripcion": "Jogger cómodo para el día a día urbano"},
    {"id": 5, "nombre": "Chaqueta Bomber Night", "categoria": "Ropa", "precio": 49990, "talla": ["S", "M", "L", "XL"], "imagen": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=500&fit=crop", "descripcion": "Bomber con detalles reflectantes nocturnos"},
    {"id": 6, "nombre": "Pantalón Slim Fit Dark", "categoria": "Pantalones", "precio": 31990, "talla": ["28", "30", "32", "34", "36"], "imagen": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=400&h=500&fit=crop", "descripcion": "Slim fit oscuro para looks elegantes"},
]

@app.route('/')
def index():
    return render_template('index.html', productos=PRODUCTOS)

@app.route('/catalogo')
def catalogo():
    categoria = request.args.get('categoria', 'todos')
    if categoria == 'todos':
        productos = PRODUCTOS
    else:
        productos = [p for p in PRODUCTOS if p['categoria'].lower() == categoria.lower()]
    return render_template('catalogo.html', productos=productos, categoria=categoria)

@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/agregar_carrito', methods=['POST'])
def agregar_carrito():
    data = request.get_json()
    carrito = session.get('carrito', [])
    
    producto_id = data.get('id')
    producto = next((p for p in PRODUCTOS if p['id'] == producto_id), None)
    
    if producto:
        item_existente = next((i for i in carrito if i['id'] == producto_id), None)
        if item_existente:
            item_existente['cantidad'] += 1
        else:
            carrito.append({
                'id': producto['id'],
                'nombre': producto['nombre'],
                'precio': producto['precio'],
                'imagen': producto['imagen'],
                'cantidad': 1
            })
        session['carrito'] = carrito
        return jsonify({'success': True, 'total_items': sum(i['cantidad'] for i in carrito)})
    
    return jsonify({'success': False})

@app.route('/eliminar_carrito', methods=['POST'])
def eliminar_carrito():
    data = request.get_json()
    carrito = session.get('carrito', [])
    carrito = [i for i in carrito if i['id'] != data.get('id')]
    session['carrito'] = carrito
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return jsonify({'success': True, 'total': total, 'total_items': sum(i['cantidad'] for i in carrito)})

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

import os

if __name__ == '__main__':
    # Railway asigna un puerto automáticamente a través de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' permite que el servidor sea accesible externamente
    app.run(host='0.0.0.0', port=port)
