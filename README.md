# ZethUrban 🔥

Tienda online de ropa urbana desarrollada con Python (Flask) + HTML + CSS.

## ¿Cómo ejecutar la tienda?

### 1. Instala las dependencias
Abre la terminal en la carpeta del proyecto y ejecuta:
```
pip install flask
```

### 2. Inicia el servidor
```
python app.py
```

### 3. Abre tu tienda
Ve a tu navegador y entra a:
```
http://localhost:5000
```

## Estructura del proyecto
```
zethurban/
├── app.py               ← Servidor Python (Flask)
├── requirements.txt     ← Dependencias
├── templates/
│   ├── base.html        ← Plantilla base (navbar + footer)
│   ├── index.html       ← Página de inicio
│   ├── catalogo.html    ← Catálogo de productos
│   ├── carrito.html     ← Carrito de compras
│   ├── nosotros.html    ← Página "Sobre nosotros"
│   └── contacto.html    ← Página de contacto
└── static/
    ├── css/
    │   └── style.css    ← Estilos visuales
    └── js/
        └── main.js      ← Funciones del carrito
```

## ¿Cómo agregar productos?
Abre `app.py` y modifica la lista `PRODUCTOS` con tus productos reales.

## ¿Cómo cambiar el número de WhatsApp?
Busca `56912345678` en todos los archivos y reemplázalo con tu número real.

## Publicar en internet
Sigue las instrucciones de Railway: https://railway.app
