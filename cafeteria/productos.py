import json
import os

class Productos:
    def __init__ (self, archivo ="productos.json"):
        self.archivo = archivo
        self.productos = self.cargar_productos()
        
    def cargar_productos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load (f)
        return {}
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos cargados.")
        else:
            print ("Productos disponibles: ")
            for nombre in self.productos:
                print(f"- {nombre}")
    def obtener_receta(self, nombre_producto):
        return self.productos.get(nombre_producto, {}.get("ingredientes", {}))


class Confiteria:
    def __init__(self):
        self.productos = {}
        
    def cargar_productos (self, archivo= "productos.json"):
        if os.path.exists(archivo):  
            with open (archivo, "r") as f:
                self.productos = json.load(f)
        else:
            self.productos ={}  
            
    def guardar_productos (self, archivo="productos.json"):
        with open(archivo, "w") as f:
            json.dump(self.productos, f, indent=4)
    def agregar_productos(self, nombre, ingedientes_necesarios, precio):
        self.productos[nombre]={
            "ingedientes": ingedientes_necesarios,
            "precio": precio
        }
        self.guardar_productos()
    def mostrar_productos(self):
        if not self.preductos:
            print("No hay productos cargados.")
            return
        
        for nombre, datos in self.productos.items():
            print (f"Producto: {nombre}")
            print (f"Precio: ${datos['precio']}")
            print ("Ingredientes: ")
            for ingrediente, cantidad in datos["ingredientes"].items():
                print (f"   -{ingrediente}: {cantidad}")
            print()
            
    def menu(self):
        while True:
            print("========MENU CONFITERIA========")
            print("1. Ver productos")
            print("2. Agregar productos")
            print("3. Volver al menu principal")
            
            opcion= input("Elegi una opcion: ")
            
            if opcion== "1":
                self.mostrar_productos()
            elif opcion == "2":
                nombre= input("Nombre del producto: ")
                ingredientes = {}
                print ("Agrega los ingredientes que usa (de a uno, escribi 'fin para terminar): ")
                while True:
                    ingr= input("Ingrediente: ")
                    if ingr.lower()== "fin":
                        break
                    try: 
                        cantidad = int(input(f"Cantidad de {ingr}: "))
                        ingredientes[ingr]= cantidad
                    except ValueError:
                        print("Cantidad invalida.")
                try:
                    precio= int(input("Precio de venta del producto: "))
                except ValueError:
                    print("Precio invalido.")
                    continue 
                self.agregar_productos(nombre, ingredientes, precio)
                print("Producto agregado.")
            elif opcion== "3":
                break
            else:
                print("Opcion no valida.")