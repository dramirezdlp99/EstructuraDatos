import tkinter as tk
import time
import math
import os
from PIL import Image, ImageTk

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

class SpiderManSmartWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Spider-Man SmartWatch")
        self.root.configure(bg="#121212")
        self.root.geometry("500x500")
        
        # Variables de control
        self.show_date = False
        self.show_digital = False
        
        # Cargar imágenes
        self.skins = self.load_skins()
        self.current_skin = 0
        
        # Canvas principal
        self.canvas = tk.Canvas(root, width=500, height=500, bg="#121212", highlightthickness=0)
        self.canvas.pack()
        
        # Flechas de navegación
        self.create_navigation_arrows()
        
        # Botones de control
        self.create_control_buttons()
        
        # Lista circular para horas
        self.hours_list = self.create_hours_list()
        
        # Iniciar reloj
        self.rgb_index = 0
        self.draw_clock_face()
        self.update_clock()

    def load_skins(self):
        skins = []
        skin_files = ["spiderman1.gif", "spiderman2.gif", "spiderman3.gif"]
        for file in skin_files:
            try:
                img_path = os.path.join("assets", file)
                img = Image.open(img_path)
                img = img.resize((220, 220), Image.LANCZOS)
                skins.append(ImageTk.PhotoImage(img))
            except Exception as e:
                print(f"Error al cargar {file}: {e}")
                backup = Image.new("RGBA", (220, 220), (18, 18, 18, 0))
                skins.append(ImageTk.PhotoImage(backup))
        return skins

    def create_navigation_arrows(self):
        # Flecha izquierda
        self.canvas.create_polygon(
            50, 250,
            70, 230,
            70, 270,
            fill="white", outline="#444", width=2, tags="left_arrow"
        )
        self.canvas.tag_bind("left_arrow", "<Button-1>", lambda e: self.change_skin(-1))
        
        # Flecha derecha
        self.canvas.create_polygon(
            450, 250,
            430, 230,
            430, 270,
            fill="white", outline="#444", width=2, tags="right_arrow"
        )
        self.canvas.tag_bind("right_arrow", "<Button-1>", lambda e: self.change_skin(1))

    def create_control_buttons(self):
        # Botón de fecha
        self.date_btn = tk.Button(
            self.root,
            text="FECHA",
            command=self.toggle_date,
            bg="#FF3333",
            fg="white",
            font=("Arial", 8, "bold"),
            borderwidth=0,
            relief="flat",
            activebackground="#CC0000",
            activeforeground="white"
        )
        self.date_btn.place(x=80, y=440, width=80, height=30)
        
        # Botón de hora digital
        self.digital_btn = tk.Button(
            self.root,
            text="DIGITAL",
            command=self.toggle_digital,
            bg="#FF3333",
            fg="white",
            font=("Arial", 8, "bold"),
            borderwidth=0,
            relief="flat",
            activebackground="#CC0000",
            activeforeground="white"
        )
        self.digital_btn.place(x=340, y=440, width=80, height=30)

    def toggle_date(self):
        self.show_date = not self.show_date
        self.update_clock_display()

    def toggle_digital(self):
        self.show_digital = not self.show_digital
        self.update_clock_display()

    def update_clock_display(self):
        self.canvas.delete("digital")
        
        if self.show_date or self.show_digital:
            now = time.localtime()
            
            if self.show_date:
                date_str = time.strftime("%a, %d %b %Y")
                self.canvas.create_text(
                    250, 450, 
                    text=date_str, 
                    fill="#AAAAAA", 
                    font=("Arial", 10), 
                    tags="digital"
                )
            
            if self.show_digital:
                time_str = time.strftime("%I:%M:%S %p")
                self.canvas.create_text(
                    250, 480, 
                    text=time_str, 
                    fill="white", 
                    font=("Arial", 12, "bold"), 
                    tags="digital"
                )

    def create_hours_list(self):
        hours_list = CircularDoublyLinkedList()
        for hour in range(1, 13):
            hours_list.insert_at_end(hour)
        return hours_list

    def get_rgb_color(self):
        colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
        self.rgb_index = (self.rgb_index + 1) % len(colors)
        return colors[self.rgb_index]

    def draw_clock_face(self):
        self.canvas.delete("clock")
        
        # Dibujar círculo principal
        center_x, center_y = 250, 250
        radius = 200
        
        # Círculo exterior con borde RGB
        border_color = self.get_rgb_color()
        self.canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline=border_color, width=8, tags="clock"
        )
        
        # Círculo interior para el fondo del reloj
        self.canvas.create_oval(
            center_x - radius + 20, center_y - radius + 20,
            center_x + radius - 20, center_y + radius - 20,
            fill="#222222", outline="#444", width=2, tags="clock"
        )
        
        # Imagen de Spider-Man
        self.canvas.create_image(
            center_x, center_y,
            image=self.skins[self.current_skin], tags="clock"
        )
        
        # Dibujar números del reloj
        self.draw_clock_numbers(center_x, center_y, radius - 40)
        
        # Actualizar color de botones
        self.update_button_colors()

    def update_button_colors(self):
        if self.current_skin == 0:  # Skin rojo
            color = "#FF3333"
            hover_color = "#CC0000"
        else:  # Skins azul/blanco
            color = "#3399FF"
            hover_color = "#0066CC"
        
        self.date_btn.config(bg=color, activebackground=hover_color)
        self.digital_btn.config(bg=color, activebackground=hover_color)

    def draw_clock_numbers(self, center_x, center_y, radius):
        skin_styles = [
            {"color": "#FF3333", "font": ("Times New Roman", 14, "bold")},
            {"color": "#3399FF", "font": ("Times New Roman", 14, "bold")},
            {"color": "#FFFFFF", "font": ("Times New Roman", 14, "bold")}
        ]
        style = skin_styles[self.current_skin]
        
        for hour in range(1, 13):
            angle = math.radians(90 - hour * 30)
            x = center_x + radius * math.cos(angle)
            y = center_y - radius * math.sin(angle)
            self.canvas.create_text(
                x, y,
                text=str(hour),
                fill=style["color"],
                font=style["font"],
                tags="clock"
            )

    def update_clock(self):
        self.canvas.delete("hands")
        now = time.localtime()
        hours, mins, secs = now.tm_hour % 12 or 12, now.tm_min, now.tm_sec
        
        # Estilo de manecillas
        hand_styles = [
            {"hour": "#FF3333", "min": "#3399FF", "sec": "#FFFFFF"},
            {"hour": "#3399FF", "min": "#FF3333", "sec": "#FFFFFF"},
            {"hour": "#FFFFFF", "min": "#FF3333", "sec": "#3399FF"}
        ]
        style = hand_styles[self.current_skin]
        
        # Dibujar manecillas
        self.draw_hand(250, 250, hours * 30 + mins * 0.5, 60, style["hour"], 8)
        self.draw_hand(250, 250, mins * 6, 90, style["min"], 6)
        self.draw_hand(250, 250, secs * 6, 110, style["sec"], 2)
        
        # Centro del reloj
        self.canvas.create_oval(245, 245, 255, 255, fill="#FFFFFF", tags="hands")
        
        # Actualizar display
        if self.show_date or self.show_digital:
            self.update_clock_display()
        
        self.root.after(1000, self.update_clock)

    def draw_hand(self, x, y, angle, length, color, width):
        angle_rad = math.radians(90 - angle)
        end_x = x + length * math.cos(angle_rad)
        end_y = y - length * math.sin(angle_rad)
        self.canvas.create_line(x, y, end_x, end_y, fill=color, width=width, tags="hands")

    def change_skin(self, direction):
        self.current_skin = (self.current_skin + direction) % len(self.skins)
        self.draw_clock_face()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpiderManSmartWatch(root)
    root.mainloop()