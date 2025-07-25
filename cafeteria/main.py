from inventario import Inventario
from productos import Productos
def main():
    inventario = Inventario()
    productos= Productos()
    
    inventario.cargar_ingredientes()
    productos.cargar_productos()
    
    while True:
        print ("========SISTEMA CAFETERIA========")
        print("1. Gestionar ingredientes")
        print("2. Gestionar productos")
        print("3. Registrar venta de productos")
        print("4.Salir")

        opcion= input ("Elegi una opcion: ")
        
        if opcion == "1":
            inventario.menu()
        elif opcion == "2":
            productos.menu()
        elif opcion == "3":
            productos.mostrar_productos()
            nombre =input("¿Qué producto se vendió?: ").strip().lower()
            receta= productos.obtener_receta(nombre)
            if not receta:
                print("Producto no encontrado o sin stock")
                continue
            rinde= productos.productos[nombre].get("rinde",1)
            if rinde <= 0:
                print("El rinde no es valido.")
                continue
            exito= inventario.descontar_ingredientes(receta, rinde)
            if exito:
                print("Venta registrada y stock actualizado.")
            else:
                print("No se pudo realizar la ventana (ingredientes insuficientes).")
                
        elif opcion =="4":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
if __name__=="__main__":
    main()