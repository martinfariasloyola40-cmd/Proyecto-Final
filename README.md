# Proyecto-Final

Super-Resolución de Imágenes con Optimización y Flask
Este proyecto implementa una aplicación web en Flask que realiza super-resolución de imágenes 
El usuario puede elegir el algoritmo, número de iteraciones, el regularizador y visualizar el resultado final en la aplicación web.

Instalacion: 

python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

Instalar dependencias:

pip install -r requirements.txt

Ejecutar:

python app.py

Cómo usar la demo paso a paso:

Abrir la app Flask
Subir una imagen LR
Elegir:

número de iteraciones,
  τ (learning rate)
  λ (regularización)
  tipo de regularizador (L2 grad / Huber)

Ejecutar super-resolución
Ver la imagen HR reconstruida
