import json
import os

class Productos:
    def __init__(self, archivo="productos.json"):
        self.archivo = archivo
        self.productos = self.cargar_productos()

    def cargar_productos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def guardar_productos(self):
        with open(self.archivo, "w") as f:
            json.dump(self.productos, f, indent=4)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos cargados.")
        else:
            print("Productos disponibles:")
            for nombre in self.productos:
                print(f"- {nombre}")

    def obtener_receta(self, nombre_producto):
        producto = self.productos.get(nombre_producto)
        if producto and "ingredientes" in producto:
            return producto["ingredientes"]
        return {}

    def agregar_producto(self, nombre, ingredientes_necesarios, precio_unitario, rinde):
        self.productos[nombre] = {
            "ingredientes": ingredientes_necesarios,
            "precio_unitario": precio_unitario,
            "rinde": rinde
        }
        self.guardar_productos()
        print("Producto agregado con éxito.")

    def menu(self):
        while True:
            print("========MENU CONFITERIA========")
            print("1. Ver productos")
            print("2. Agregar producto")
            print("3. Volver al menú principal")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                self.mostrar_productos()

            elif opcion == "2":
                nombre = input("Nombre del producto: ").strip().lower()
                ingredientes = {}
                print("Agregá los ingredientes que usa (uno por uno, escribí 'fin' para terminar): ")
                while True:
                    ingr = input("Ingrediente: ").strip().lower()
                    if ingr == "fin":
                        break
                    try:
                        cantidad = float(input(f"Cantidad de {ingr} (en gramos/ml): "))
                        ingredientes[ingr] = cantidad
                    except ValueError:
                        print("Cantidad inválida. Intentalo de nuevo.")

                try:
                    rinde = int(input("¿Cuántas unidades salen con esta receta?: "))
                    if rinde <= 0:
                        print("El rinde debe ser mayor que cero.")
                        continue
                    precio_unitario = float(input("Precio de venta por unidad: "))
                    self.agregar_producto(nombre, ingredientes, precio_unitario, rinde)
                except ValueError:
                    print("Valor inválido. Intentalo de nuevo.")

            elif opcion == "3":
                break

            else:
                print("Opción no válida.")
