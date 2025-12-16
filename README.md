# Proyecto-Final
# Proyecto de Super-Resolución de Imágenes

Este proyecto implementa un método simple de super-resolución de imágenes en escala de grises, utilizando descenso de gradiente y regularización variacional. 
La aplicación está construida con Flask y permite subir una imagen de baja resolución (LR), configurar parámetros y obtener una reconstrucción de alta resolución (HR) desde una interfaz web.

## Estructura del proyecto

superres-project/
├── app.py
├── superres/
│ ├── core.py
│ ├── gd.py
│ └── init.py
├── templates/
│ ├── index.html
│ └── result.html
└── static/
└── results/


## Organización del código

Para simplificar el proyecto, las funcionalidades se agrupan en los siguientes módulos:

- **core.py**: contiene los operadores de degradación (A y Aᵀ), los regularizadores (L2 y Huber-TV) y las funciones auxiliares para manejo de imágenes.
- **gd.py**: implementa el algoritmo de descenso de gradiente para resolver el problema de super-resolución.
- **app.py**: define la aplicación Flask, las rutas web y la integración entre la interfaz y el algoritmo numérico.

Esta organización evita la fragmentación excesiva del código y mantiene el proyecto compacto y fácil de seguir.

## Requisitos

- Python 3.9+
- Flask
- NumPy
- SciPy
- Pillow
- Matplotlib

## Ejecución

Instalar dependencias:
```bash
pip install flask numpy scipy pillow matplotlib

Ejecutar:
python app.py

Luego abrir:
http://localhost:5000


