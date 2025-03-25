# EstructuraDatos

DR Music 🎶

Descripción del Proyecto

DR Music es una aplicación web para gestionar y reproducir archivos de audio en formato MP3. Permite a los usuarios:

✅ Subir canciones a la lista de reproducción.
✅ Reproducir, pausar y navegar entre canciones.
✅ Eliminar canciones con opción de recuperarlas desde la papelera.
✅ Eliminar canciones de manera permanente.

La aplicación está construida con Flask (Python) y usa HTML y CSS para la interfaz.

📂 Estructura del Proyecto

/DR_Music/
│── /static/
│   ├── /music/   # Archivos MP3
│── /templates/
│   ├── index.html  # Página principal
│── app.py         # Servidor Flask
│── README.md      # Este archivo

🛠 Instalación y Configuración

1️⃣ Instalar dependencias

Asegúrate de tener Python 3 instalado. Luego, instala Flask:

pip install flask

2️⃣ Crear carpetas necesarias
Si no existen, crea la carpeta para las canciones:

mkdir -p static/music templates
3️⃣ Agregar canciones
Guarda archivos .mp3 en static/music/.

4️⃣ Ejecutar la aplicación

python app.py

Luego, abre tu navegador en http://127.0.0.1:5000/ 🎶

El código o el sistema o reproductor permite añadir cualquier canción formato .mp3 que se tenga y así mismo con cada función.

💡 Listas Doblemente Enlazadas en el Proyecto

En este proyecto usamos una lista doblemente enlazada de manera conceptual para manejar la lista de reproducción.

¿Cómo funciona?

Cada canción tiene un nodo que almacena su información y referencia la canción anterior y la siguiente. Esto permite:
🔄 Navegar entre canciones con "Siguiente" y "Anterior".
📥 Insertar y eliminar canciones de forma eficiente.
♻ Manejar la papelera sin perder el orden de la lista.

En el código, esto se implementa con listas de Python en lugar de nodos explícitos, pero sigue la misma lógica de estructura.

🎤 Desarrollado por:

David Ramírez de la Parra

📅 Fecha: 25 de marzo de 2025
