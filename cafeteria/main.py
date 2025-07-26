from inventario import Inventario
from productos import Productos
from ventas import Ventas


def mostrar_titulo():
    print("""
=========================================
     SISTEMA DE VENTAS - CAFETERÍA  
==========================================
""")

def main():
    inventario = Inventario()
    productos= Productos(inventario=inventario)
    ventas= Ventas()
    mostrar_titulo()
    
    
    while True:
        print ("----------SISTEMA CAFETERIA-------")
        print("1. Gestionar ingredientes")
        print("2. Gestionar productos")
        print("3. Registrar venta de productos")
        print("4.Ver historial de tickets")
        print("5.Salir")

        opcion= input ("Elegi una opcion: ")
        
        if opcion == "1":
            inventario.menu_ingredientes()
        elif opcion == "2":
            productos.menu()
        elif opcion == "3":
            productos_vendidos=[]
            while True:
                productos.mostrar_productos()
                nombre =input("¿Qué producto se vendió?: ").strip().lower()
                receta= productos.obtener_receta(nombre)
            
                if not receta:
                    print("Producto no encontrado.")
                    continue
            
                rinde = productos.productos[nombre].get("rinde", 1)   
                     
                try:
                    cantidad_vendida= int(input("¿Cuántas unidades se vendieron?: "))
                    escala= cantidad_vendida/ rinde
                    if inventario.ingredientes.descontar_ingredientes(receta, rinde=1 /escala):
                        precio= productos.productos[nombre]["precio_unitario"]
                        productos_vendidos.append({
                            "nombre": nombre,
                            "cantidad": cantidad_vendida,
                            "precio": precio
                        })
                    else:
                        print("No hay suficientes ingredientes.")
                except ValueError:
                    print("Cantidad inválida. ") 
                seguir = input("¿Desea agregar otro producto a esta venta? (si/no): ").strip().lower()
                if seguir != "si":
                    break
            if productos_vendidos:
                ventas.registrar_ventas_multiples(productos_vendidos)
        
        elif opcion == "4":
            if ventas.ventas:
                print("\n======== HISTORIAL DE VENTAS ========")
                for i, venta in enumerate(ventas.ventas, 1):
                    print(f"\n--- Venta {i} ---")
                    if "productos" in venta:
                        for prod in venta["productos"]:
                            print(f"Producto: {prod['nombre']}")
                            print(f"Cantidad: {prod['cantidad']}")
                            print(f"Precio unitario: ${prod['precio']:.2f}")
                    else:
                    # Para ventas individuales
                        print(f"Producto: {venta['producto']}")
                        print(f"Cantidad: {venta['cantidad']}")
                        print(f"Precio unitario: ${venta['precio_unitario']:.2f}")
                    print(f"Total: ${venta['total']:.2f}")
                    print(f"Fecha: {venta['fecha']}")
                print("=====================================\n")
            else:
                print("No hay ventas registradas.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
                
                    
if __name__=="__main__":
    main()
    