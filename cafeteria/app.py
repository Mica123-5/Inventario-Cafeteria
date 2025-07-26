import tkinter as tk
from tkinter import messagebox
from main import Inventario, Productos, Ventas  # asegurate que los módulos estén bien estructurados

class CafeteriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cafetería")
        self.root.geometry("400x400")

        self.inventario = Inventario()
        self.productos = Productos(self.inventario)
        self.ventas = Ventas()

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="📋 Sistema de Cafetería", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="1. Gestionar ingredientes", width=30, command=self.gestionar_ingredientes).pack(pady=5)
        tk.Button(self.root, text="2. Gestionar productos", width=30, command=self.gestionar_productos).pack(pady=5)
        tk.Button(self.root, text="3. Registrar venta", width=30, command=self.registrar_venta).pack(pady=5)
        tk.Button(self.root, text="4. Ver historial de tickets", width=30, command=self.ver_historial).pack(pady=5)
        tk.Button(self.root, text="5. Salir", width=30, command=self.root.quit).pack(pady=20)

    def gestionar_ingredientes(self):
        messagebox.showinfo("Info", "Esta opción aún se maneja por consola.")
        self.inventario.menu_ingredientes()

    def gestionar_productos(self):
        messagebox.showinfo("Info", "Esta opción aún se maneja por consola.")
        self.productos.menu()

    def registrar_venta(self):
        messagebox.showinfo("Info", "Registrar ventas se hace por consola en esta versión.")
             # Podemos mejorar esto después

    def ver_historial(self):
        if self.ventas.ventas:
            ventas_texto = ""
            for i, venta in enumerate(self.ventas.ventas, 1):
                ventas_texto += f"Venta {i}:\n"
                if "productos" in venta:
                    for prod in venta["productos"]:
                        ventas_texto += f"- {prod['nombre']} x{prod['cantidad']} - ${prod['precio']:.2f}\n"
                else:
                    ventas_texto += f"- {venta['producto']} x{venta['cantidad']} - ${venta['precio_unitario']:.2f}\n"
                ventas_texto += f"Total: ${venta['total']:.2f} - Fecha: {venta['fecha']}\n\n"
            messagebox.showinfo("Historial de Ventas", ventas_texto)
        else:
            messagebox.showinfo("Historial de Ventas", "No hay ventas registradas.")

# Ejecutar interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = CafeteriaApp(root)
    root.mainloop()
