import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from main import Inventario, Productos, Ventas 
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
        ventana_ing = tk.Toplevel(self.root)
        ventana_ing.title("Gestión de Ingredientes")
        ventana_ing.geometry("400x400")

    # Lista de ingredientes
        texto = tk.Text(ventana_ing, height=10)
        texto.pack(pady=5)

        def mostrar_ingredientes_gui():
            texto.delete(1.0, tk.END)
            if not self.inventario.ingredientes.ingredientes:
                texto.insert(tk.END, "No hay ingredientes cargados.\n")
            else:
                for nombre, datos in self.inventario.ingredientes.ingredientes.items():
                    texto.insert(tk.END, f"{nombre}: {datos['cantidad']} {datos['unidad']} (mínimo: {datos['minimo']})\n")

        mostrar_ingredientes_gui()

    # Campos para agregar
        tk.Label(ventana_ing, text="Nombre:").pack()
        entrada_nombre = tk.Entry(ventana_ing)
        entrada_nombre.pack()

        tk.Label(ventana_ing, text="Cantidad:").pack()
        entrada_cantidad = tk.Entry(ventana_ing)
        entrada_cantidad.pack()

        tk.Label(ventana_ing, text="Unidad (g, kg, ml, l):").pack()
        entrada_unidad = tk.Entry(ventana_ing)
        entrada_unidad.pack()

        tk.Label(ventana_ing, text="Stock mínimo:").pack()
        entrada_minimo = tk.Entry(ventana_ing)
        entrada_minimo.pack()

        def agregar_ingrediente_gui():
            try:
                nombre = entrada_nombre.get().strip().lower()
                cantidad = float(entrada_cantidad.get())
                unidad = entrada_unidad.get().strip().lower()
                minimo = float(entrada_minimo.get())
                self.inventario.ingredientes.agregar_ingredientes(nombre, cantidad, unidad, minimo)
                messagebox.showinfo("Éxito", f"Ingrediente '{nombre}' agregado.")
                mostrar_ingredientes_gui()
            except ValueError:
                messagebox.showerror("Error", "Datos inválidos.")

        tk.Button(ventana_ing, text="Agregar Ingrediente", command=agregar_ingrediente_gui).pack(pady=10)
                   
    def gestionar_productos(self):
        ventana_prod = tk.Toplevel(self.root)
        ventana_prod.title("Gestión de Productos")
        ventana_prod.geometry("500x500")

        texto = tk.Text(ventana_prod, height=10)
        texto.pack(pady=5)

        def mostrar_productos_gui():
            texto.delete(1.0, tk.END)
            if not self.productos.productos:
                texto.insert(tk.END, "No hay productos cargados.\n")
            else:
                for nombre, datos in self.productos.productos.items():
                    texto.insert(tk.END, f"{nombre} - ${datos['precio_unitario']:.2f}\nRinde: {datos['rinde']}\nIngredientes:\n")
                    for ing, cant in datos["ingredientes"].items():
                        texto.insert(tk.END, f"  - {ing}: {cant}\n")
                    texto.insert(tk.END, "\n")

        mostrar_productos_gui()

        # Entradas
        tk.Label(ventana_prod, text="Nombre del producto:").pack()
        entrada_nombre = tk.Entry(ventana_prod)
        entrada_nombre.pack()

        tk.Label(ventana_prod, text="Precio:").pack()
        entrada_precio = tk.Entry(ventana_prod)
        entrada_precio.pack()

        # Ingredientes para el producto  (receta)
        ingredientes_temp = {}

        def agregar_ingrediente_al_producto():
            ing = entrada_ing_nombre.get().strip().lower()
            cant = entrada_ing_cantidad.get().strip()
            try:
                cant = float(cant)
                if ing:
                    ingredientes_temp[ing] = cant
                    messagebox.showinfo("Ingrediente agregado", f"{ing}: {cant}")
                    entrada_ing_nombre.delete(0, tk.END)
                    entrada_ing_cantidad.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Error", "Cantidad inválida.")

        tk.Label(ventana_prod, text="Ingrediente:").pack()
        entrada_ing_nombre = tk.Entry(ventana_prod)
        entrada_ing_nombre.pack()

        tk.Label(ventana_prod, text="Cantidad:").pack()
        entrada_ing_cantidad = tk.Entry(ventana_prod)
        entrada_ing_cantidad.pack()

        tk.Button(ventana_prod, text="Agregar ingrediente al producto", command=agregar_ingrediente_al_producto).pack(pady=5)

        # ingresar el rinde
        tk.Label(ventana_prod, text="¿Cuántas unidades salen con esta receta?").pack()
        entrada_rinde = tk.Entry(ventana_prod)
        entrada_rinde.pack()

        def guardar_producto():
            nombre = entrada_nombre.get().strip().lower()
            try:
                precio = float(entrada_precio.get())
                rinde = int(entrada_rinde.get())  # se usa el rinde ingresado por el usuario
                if nombre and ingredientes_temp and rinde > 0:
                    self.productos.agregar_producto(nombre, ingredientes_temp.copy(), precio, rinde)
                    messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado.")
                    entrada_nombre.delete(0, tk.END)
                    entrada_precio.delete(0, tk.END)
                    entrada_rinde.delete(0, tk.END)
                    ingredientes_temp.clear()
                    mostrar_productos_gui()
                else:
                    messagebox.showerror("Error", "Nombre, ingredientes o rinde vacíos.")
            except ValueError:
                messagebox.showerror("Error", "Precio o rinde inválidos.")

        tk.Button(ventana_prod, text="Guardar producto", command=guardar_producto).pack(pady=10)

        # Botón para editar producto
        def editar_producto():
            nombre = simpledialog.askstring("Editar Producto", "Nombre del producto a editar:")
            if not nombre or nombre.lower() not in self.productos.productos:
                messagebox.showerror("Error", "Producto no encontrado.")
                return

            datos = self.productos.productos[nombre.lower()]

            # Editar ingredientes
            ingredientes = datos.get("ingredientes", {})
            new_ingredientes = {}
            for ingr, cantidad in ingredientes.items():
                nueva_cantidad = simpledialog.askfloat("Editar Ingrediente", f"Cantidad de {ingr} (g/ml):", initialvalue=cantidad)
                if nueva_cantidad:
                    new_ingredientes[ingr] = nueva_cantidad
            datos["ingredientes"] = new_ingredientes

            # Editar rinde
            try:
                nuevo_rinde = int(simpledialog.askstring("Editar Rinde", f"Nuevo rinde para {nombre.title()}:"))
                if nuevo_rinde <= 0:
                    raise ValueError
                datos["rinde"] = nuevo_rinde
            except:
                messagebox.showerror("Error", "Rinde inválido.")
                return

            # Editar precio
            try:
                nuevo_precio = float(simpledialog.askstring("Editar Precio", f"Nuevo precio para {nombre.title()}:"))
                datos["precio_unitario"] = nuevo_precio
            except:
                messagebox.showerror("Error", "Precio inválido.")
                return

            self.productos.guardar_productos()
            messagebox.showinfo("Éxito", "Producto editado con éxito.")
            ventana_prod.destroy()
            self.gestionar_productos()

        tk.Button(ventana_prod, text="Editar Producto", command=editar_producto).pack(pady=10)

        # Botón para eliminar producto
        def eliminar_producto():
            nombre = simpledialog.askstring("Eliminar Producto", "Nombre del producto a eliminar:")
            if not nombre or nombre.lower() not in self.productos.productos:
                messagebox.showerror("Error", "Producto no encontrado.")
                return

            if messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar el producto {nombre.title()}?"):
                del self.productos.productos[nombre.lower()]
                self.productos.guardar_productos()
                messagebox.showinfo("Éxito", f"Producto {nombre.title()} eliminado con éxito.")
                ventana_prod.destroy()
                self.gestionar_productos()

        tk.Button(ventana_prod, text="Eliminar Producto", command=eliminar_producto).pack(pady=10)
        
        
    def registrar_venta(self):
        ventana_venta = tk.Toplevel(self.root)
        ventana_venta.title("Registrar Venta")
        ventana_venta.geometry("400x300")

        tk.Label(ventana_venta, text="Seleccioná un producto:").pack(pady=5)
        productos_nombres = list(self.productos.productos.keys())

        if not productos_nombres:
            messagebox.showerror("Error", "No hay productos cargados.")
            ventana_venta.destroy()
            return

        producto_var = tk.StringVar(ventana_venta)
        producto_var.set(productos_nombres[0])
        menu_productos = tk.OptionMenu(ventana_venta, producto_var, *productos_nombres)
        menu_productos.pack(pady=5)

        tk.Label(ventana_venta, text="Cantidad:").pack(pady=5)
        entrada_cantidad = tk.Entry(ventana_venta)
        entrada_cantidad.pack(pady=5)

        def confirmar_venta():
            producto = producto_var.get()
            try:
                cantidad = int(entrada_cantidad.get())
                if cantidad <= 0:
                    raise ValueError

                # Verificar disponibilidad de ingredientes
                if not self.productos.verificar_disponibilidad(producto, cantidad):
                    messagebox.showerror("Error", f"No hay suficientes ingredientes para preparar {cantidad} unidad(es) de {producto}.")
                    return

                    # Descontar ingredientes
                self.productos.descontar_ingredientes(producto, cantidad)

                # Registrar la venta
                precio_unitario = self.productos.productos[producto]["precio"]
                total = precio_unitario * cantidad
                self.ventas.ventas.append({
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "total": total,
                    "fecha": self.ventas.obtener_fecha()
                })

                messagebox.showinfo("Venta realizada", f"Total: ${total:.2f}")
                ventana_venta.destroy()
            except ValueError:
                messagebox.showerror("Error", "Cantidad inválida.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana_venta, text="Confirmar Venta", command=confirmar_venta).pack(pady=15)

             

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
