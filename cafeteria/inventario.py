import json
import os
from datetime import datetime

class Inventario:
    def __init__(self):
        self.ingredientes= {}
        
    def cargar_ingredientes (self, archivo= "ingredientes.json"):
        if os.path.exists(archivo):
            with open(archivo, "r")as f:
                self.ingredientes = json.load(f)
        else:
            self.ingredientes = {}
    
    def guardar_ingredientes (self, archivo= "ingredientes.json"):
        with open (archivo, "w") as f:
            json.dump(self.ingredientes , f, indent=4)  #json.dump función que escribe datos en formato JSON dentro de un archivo.
                                                       #indent=4 4 espacis de sangria
    def agregar_ingredientes (self, nombre, cantidad, unidad, minimo, precio):
        self.ingredientes[nombre]= {
            "cantidad": cantidad,
            "unidad": unidad,
            "minimo":minimo,
            "precio": precio
        }
        self.guardar_ingredientes()
        
    def mostrar_ingredientes (self):
        if not self.ingredientes:
            print("No hay ingredientes cargados.")
        for nombre, datos in self.ingredientes.items():
            print (f"{nombre}:{datos['cantidad']} {datos['unidad']} (minimo: {datos['minimo']})")
            
    def descontar_ingredientes(self, receta):
        for ingrediente, cantidad_necesaria in receta.items():
            if ingrediente not in self.ingredientes:
                print(f"Ingrediente '{ingrediente}' no está en el inventario.")
                return False
            if self.ingredientes[ingrediente]["cantidad"] < cantidad_necesaria:
                print(f"No hay suficiente '{ingrediente}' (faltan {cantidad_necesaria - self.ingredientes[ingrediente]['cantidad']} {self.ingredientes[ingrediente]['unidad']})")
                return False
    
    # Si hay stock suficiente, lo descontamos
        for ingrediente, cantidad_necesaria in receta.items():
            self.ingredientes[ingrediente]["cantidad"] -= cantidad_necesaria
        self.guardar_igredientes()
        return True
       
    def menu(self):
        while True:
            print ( "========MENU CAFETERIA========")
            print ("1. Ver ingredientes")
            print("2. Agregar ingredientes")
            print ("3. Registrar venta de producto")
            print ("4. Salir ")
            
            opcion= input("Elegi un opcion: ")
            if opcion == "1":
                self.mostrar_ingredientes()
            elif opcion =="2":
                nombre = input("Nombre del ingrediente: ")
                entrada_cantidad= input("Cantidad disponible (ej. 300 o 300 gr): ")
                try: 
                    partes= entrada_cantidad.strip().split()
                    if len(partes) ==2:
                        cantidad =float(partes[0])
                        unidad = partes[1]
                    elif len(partes)==1 :
                        cantidad= float(partes[0])
                        unidad = input("Unidad (g/ml/etc): ")
                    else:
                        print("Formato no reconocido. Ingresa por ejemplo: 300 o 300 ml ")
                        return
                except ValueError:
                    print("La cantidad debe ser un numero. Intentalo de nuevo.")
                    return   
                
                minimo = int(input("Stock minimo : "))
                precio = int(input("Precio por unidad: "))
                self.agregar_ingredientes(nombre,cantidad,unidad,minimo,precio)
            
            elif opcion == "4":
                from productos import Productos
                productos = Productos()
                productos.mostrar_productos()
                elegido = input("¿Qué producto se vendió?: ").lower()
                receta = productos.obtener_receta(elegido)
                if receta:
                    exito = self.descontar_ingredientes(receta)
                if exito:
                    print(f"Venta de '{elegido}' registrada con éxito.")
                else:
                    print("Producto no encontrado.")

            elif opcion =="4":
                print("Saliendo del sistema.")
                break
            else:
                print("Opcion invalida.")
