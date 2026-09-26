
#clase padre (Superclase)
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100

#clase hija (Subclase)
class Soldado(Personaje):
    def atacar(self):
        return 15

#clase hija (Subclase)
class Comandante(Personaje):
    def atacar(self):
        return 25

#Polimorfismo
def combatir(jugador, enemigo):

    while jugador.vida > 0 and enemigo.vida > 0:

        print("\nVida de Akira:", jugador.vida)
        print("Vida del enemigo:", enemigo.vida)

        print("1. Atacar")
        print("2. Esconderse")

        accion = input("Elige una opción: ")

        if accion == "1":
            enemigo.vida -= 25
            print("Akira atacó al enemigo.")

            if enemigo.vida > 0:
                jugador.vida -= enemigo.atacar()

        elif accion == "2":
            print("Akira logró esconderse.")
            return True

    return jugador.vida > 0
#inicio del juego
akira = Personaje("Akira")

print("===================================")
print(" ¡BIENVENIDO AL JUEGO DE AKIRA!")
print("===================================")
print("Akira sale del sótano después de la explosión.")
print("Debe encontrar recursos para sobrevivir.\n")

nivel = 1

while nivel <= 3:

    print("\n====================")
    print("NIVEL", nivel)
    print("====================")

    print("MENÚ")
    print("1. Buscar agua")
    print("2. Buscar comida")
    print("3. Buscar medicinas")
    print("4. Buscar agua, comida y medicinas")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("Akira encuentra agua.")

    elif opcion == "2":
        print("Akira encuentra comida.")

    elif opcion == "3":
        print("Akira encuentra medicinas.")

    elif opcion == "4":
        print("Akira encuentra agua.")
        print("Akira encuentra comida.")
        print("Akira encuentra medicinas.")

    else:
        print("Opción no válida.")
        continue

    print("\n¡Un soldado enemigo aparece!")

    enemigo = Soldado("Soldado")
    enemigo.vida = 50

    if not combatir(akira, enemigo):
        print("\n Akira fue derrotado.")
        print("FIN DEL JUEGO")
        break

    print("Akira sobrevivió y avanza al siguiente nivel.")
    nivel += 1

else:

    print("\n====================")
    print("JEFE FINAL")
    print("====================")

    comandante = Comandante("Comandante")
    comandante.vida = 100

    if combatir(akira, comandante):

        print("\n ¡FELICIDADES!")
        print("Akira derrotó al comandante enemigo.")
        print("Akira escapó de Hiroshima.")
        print("HAS GANADO EL JUEGO")

    else:

        print("\n El comandante derrotó a Akira.")
        print("HAS PERDIDO")
