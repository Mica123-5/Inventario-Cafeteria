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
        print("3. Salir")

        opcion= input ("Elegi una opcion: ")
        
        if opcion == "1":
            inventario.menu()
        elif opcion == "2":
            productos.menu()
        elif opcion =="3":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
if __name__=="__main__":
    main()