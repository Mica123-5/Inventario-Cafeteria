import json
import os

class Ingredientes:
    def __init__(self, archivo="ingredientes.json"):
        self.archivo = archivo
        self.ingredientes = self.cargar_ingredientes()

    def cargar_ingredientes(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def guardar_ingredientes(self):
        with open(self.archivo, "w") as f:
            json.dump(self.ingredientes, f, indent=4)

    def agregar_ingredientes(self, nombre, cantidad, unidad, minimo):
        unidad = unidad.lower()
        if unidad in ["kg", "kilo", "kilos"]:
            cantidad *= 1000
            minimo *= 1000
            unidad = "g"
        elif unidad in ["l", "litro", "litros"]:
            cantidad *= 1000
            minimo *= 1000
            unidad = "ml"
        elif unidad not in ["g", "ml"]:
            print("Unidad no válida.")
            return

        self.ingredientes[nombre] = {
            "cantidad": cantidad,
            "unidad": unidad,
            "minimo": minimo
        }
        self.guardar_ingredientes()

    def mostrar_ingredientes(self):
        if not self.ingredientes:
            print("No hay ingredientes cargados.")
            return
        for nombre, datos in self.ingredientes.items():
            print(f"{nombre}: {datos['cantidad']} {datos['unidad']} (mínimo: {datos['minimo']})")

    def descontar_ingredientes(self, receta, rinde=1):
        for ingr, cant in receta.items():
            total = cant / rinde
            if ingr not in self.ingredientes:
                print(f"Falta el ingrediente '{ingr}'")
                return False
            if self.ingredientes[ingr]["cantidad"] < total:
                print(f"No hay suficiente '{ingr}'")
                return False
        for ingr, cant in receta.items():
            total = cant / rinde
            self.ingredientes[ingr]["cantidad"] -= total
        self.guardar_ingredientes()
        return True
