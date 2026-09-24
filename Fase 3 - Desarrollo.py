#Stefani Yadira Quiel Gonzalez 5to Perito Contador B  

# ==========================================
# ULTIMO AMANECER EN HIROSHIMA
# ==========================================

class Recurso:#superclase (clase padre)
    def __init__(self, nombre):
        self.nombre = nombre

    def buscar(self):
        print("Akira busca un recurso.")


class Agua(Recurso):#subclase (clase hija)
    def buscar(self):
        print("Akira encontró agua para sobrevivir.")


class Comida(Recurso):#subclase (clase hija)
    def buscar(self):
        print("Akira encontró comida entre los edificios destruidos.")


class Medicina(Recurso):#subclase (clase hija)
    def buscar(self):
        print("Akira encontró medicinas en un hospital abandonado.")


# Polimorfismo:
# Cada clase hija sobrescribe el método buscar().
def explorar(recurso):
    recurso.buscar()


agua = False
comida = False
medicina = False

print("===================================")
print(" ¡BIENVENIDO AL JUEGO DE AKIRA!")
print("===================================")
print("Akira sale del sótano después de la explosión.")
print("Debe encontrar recursos para sobrevivir.\n")

while True:

    print("\nMENÚ")
    print("1. Buscar agua")
    print("2. Buscar comida")
    print("3. Buscar medicinas")
    print("4. Buscar agua, comida y medicinas")
    print("5. Salir")

    try:
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            explorar(Agua("Agua"))
            agua = True

        elif opcion == "2":
            explorar(Comida("Comida"))
            comida = True

        elif opcion == "3":
            explorar(Medicina("Medicina"))
            medicina = True

        elif opcion == "4":
            print("\nAkira explora toda la ciudad:")
            explorar(Agua("Agua"))
            explorar(Comida("Comida"))
            explorar(Medicina("Medicina"))

            agua = True
            comida = True
            medicina = True

        elif opcion == "5":
            print("\nGracias por jugar.")
            break

        else:
            print("Opción no válida.")

        # Condición de victoria
        if agua and comida and medicina:
            print("\n¡FELICIDADES!")
            print("Akira consiguió agua, comida y medicinas.")
            print("Ha sobrevivido y puede continuar su viaje para escapar de Hiroshima.")
            break

    except:
        print("Error: ingresa una opción válida.")
