import json
import os 
from datetime import datetime


class Ventas:
    def __init__(self, archivo="ventas.json"):
        self.archivo = archivo
        self.ventas = self.cargar_ventas()
    
    def cargar_ventas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r")as f:
                return json.load(f)
        return[]
    
    def guardar_ventas(self):
        with open(self.archivo, "w") as f:
            json.dump(self.ventas, f, indent=4)
            
    def registrar_venta(self, producto, cantidad, precio_unitario):
        total = round(precio_unitario * cantidad,2)
        fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        venta= {
            "producto":producto,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "total": total,
            "fecha": fecha
        }
        
        self.ventas.append(venta)
        self.guardar_ventas()
        self.generar_ticket(venta)
        

    def registrar_ventas_multiples(self, lista_productos):
        total = 0
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#GENERAR TICKET

        print("\n======== TICKET DE VENTA CAFETERÍA ========")
        for item in lista_productos:
            nombre = item["nombre"]
            cantidad = item["cantidad"]
            precio = item["precio"]
            subtotal = precio * cantidad
            total += subtotal

            print(f"\nProducto: { nombre}")
            print(f"Precio unitario: ${precio:.2f}")
            print(f"Cantidad: {cantidad}")
            print(f"Subtotal: ${subtotal:.2f}")
        print(f"\nTotal: ${total:.2f}")
        print(f"Fecha: {fecha}")
        print("==================================\n")


        venta = {
            "productos": lista_productos,
            "total": total,
            "fecha": fecha
            }
        self.ventas.append(venta)
        self.guardar_ventas()

    def generar_ticket(self, venta):
        print("\n======== TICKET DE VENTA CAFETERÍA ========")
        print(f"\nProducto: {venta['producto']}")
        print(f"Precio unitario: ${venta['precio_unitario']:.2f}")
        print(f"Cantidad: {venta['cantidad']}")
        print(f"Total: ${venta['total']:.2f}")
        print(f"Fecha: {venta['fecha']}")
        print("==================================\n")