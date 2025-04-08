# 🕷️ Spider-Man SmartWatch - Reloj con Listas Circulares Dobles 🕰️

**Autor:** David Fernando Ramírez de la Parra  
**Profesor:** Jhonatan Andrés Mideros Narváez  
**Asignatura:** Estructura de Datos  
**Institución:** Universidad Cooperativa de Colombia

---

## 📌 Descripción del Proyecto
¡Bienvenido al Spider-Man SmartWatch! Un reloj analógico interactivo desarrollado en Python usando listas circulares dobles y diseñado con temática del Hombre Araña. Este proyecto demuestra la implementación práctica de estructuras de datos en un caso de estudio real.

---

## 🌟 Características Principales
- ✅ Reloj de manecillas con movimiento fluido (horas, minutos, segundos)
- ✅ 3 skins intercambiables de Spider-Man (rojo, azul, blanco)
- ✅ Borde RGB animado que cambia de color
- ✅ Botones interactivos para mostrar/ocultar fecha y hora digital
- ✅ Interfaz intuitiva con flechas de navegación

---

## 🧠 Caso de Estudio: Listas Circulares Dobles

### 🔄 ¿Qué es una Lista Circular Doble?
Una lista circular doblemente enlazada es una estructura de datos donde:

- Cada nodo tiene dos punteros: `prev` (anterior) y `next` (siguiente).
- El último nodo apunta al primero (circularidad).
- El primer nodo apunta al último (doble enlace).

### 📊 Implementación en el Proyecto

```python
class Node:
    def __init__(self, data):
        self.data = data  # Valor almacenado (ej: hora)
        self.prev = None  # Puntero al nodo anterior
        self.next = None  # Puntero al nodo siguiente

class CircularDoublyLinkedList:
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # Circularidad
            new_node.prev = new_node  # Doble enlace
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head  # Conecta el final con el inicio
            self.head.prev = new_node  # Doble enlace circular
```

**Uso en el reloj:**
- Las horas (1-12) se almacenan en una lista circular doble.
- Las flechas de navegación recorren los nodos para cambiar de skin.

### ⚡ Ventajas Aplicadas
- ✔ Recorrido bidireccional: Puedes avanzar/retroceder entre skins con las flechas ← →.
- ✔ Eficiencia: Inserción en O(1) gracias a los punteros `prev` y `next`.
- ✔ Ciclos infinitos: Ideal para representar las horas de un reloj (1-12 y vuelve a empezar).

---

## 🛠️ Instalación y Ejecución

### 📥 Requisitos
- Python 3.8+
- Librerías: `tkinter`, `Pillow (PIL)`

### 🔧 Pasos

1. Clona el repositorio:
```bash
git clone [URL_del_repositorio]
```

2. Instala dependencias:
```bash
pip install pillow
```

3. Ejecuta el programa:
```bash
python reloj.py
```

---

## 🗂️ Estructura de Archivos

```
proyectoRelojListasCircularesDobles/
├── assets/               # Imágenes de Spider-Man
│   ├── spiderman1.gif
│   ├── spiderman2.gif
│   └── spiderman3.gif
├── reloj.py              # Código principal
└── README.md             # Este archivo
```

---

## 🎮 Cómo Usar el Reloj
- Cambiar skins: Haz clic en las flechas ← → para rotar entre diseños.
- Mostrar/ocultar fecha: Botón "FECHA" (abajo a la izquierda).
- Mostrar/ocultar hora digital: Botón "DIGITAL" (abajo a la derecha).

---

## 📚 Aprendizajes Obtenidos
- Implementación práctica de listas circulares dobles.
- Manejo de interfaces gráficas con tkinter.
- Uso de matemáticas para posicionar manecillas (ángulos, radianes).
- Integración de imágenes y efectos visuales.

---

## 🎯 Bonus Track
- ✨ Efecto RGB: El borde del reloj cambia de color automáticamente.
- 🕷️ Temática Spider-Man: Diseño personalizado con tus imágenes favoritas.

---

## 🤝 Contribuciones
¿Quieres mejorar el proyecto? ¡Abre un Pull Request!

¡Gracias por usar el Spider-Man SmartWatch! 🚀 Desarrollado con pasión por **David Fernando Ramírez de la Parra**.

📜 **Nota:** Este proyecto fue desarrollado para la asignatura de *Estructura de Datos* bajo la supervisión del profesor **Jhonatan Andrés Mideros Narváez**.
