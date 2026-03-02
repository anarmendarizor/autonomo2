import os
import time
from funciones_snake import *


#--------- FUNCIONES GENERALES ----------

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresiona Enter para continuar...")


#---------- JUEGO SNAKE ----------

def jugar_snake():
    serpiente = crear_serpiente()
    comida = crear_comida(serpiente)
    direccion = "d"
    puntos = 0

    while True:
        limpiar_pantalla()
        dibujar_tablero(serpiente, comida)
        print(f"\nPuntaje: {puntos}")
        print("Usa W A S D para moverte")

        mov = input("Movimiento: ").lower()
        if mov in ["w", "a", "s", "d"]:
            direccion = mov

        crecer = False
        x, y = serpiente[0]

        if direccion == "w":
            nueva_cabeza = (x, y - 1)
        elif direccion == "s":
            nueva_cabeza = (x, y + 1)
        elif direccion == "a":
            nueva_cabeza = (x - 1, y)
        elif direccion == "d":
            nueva_cabeza = (x + 1, y)

        if nueva_cabeza == comida:
            puntos += 1
            crecer = True
            comida = crear_comida(serpiente)

        serpiente = mover_serpiente(serpiente, direccion, crecer)

        if colision_pared(serpiente[0]) or colision_cuerpo(serpiente):
            limpiar_pantalla()
            print("GAME OVER")
            print(f"Puntaje final: {puntos}")
            pausar()
            break

        time.sleep(0.3)


# ---------- MENÚ ----------

def mostrar_menu():
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("        SNAKE GAME - MENÚ")
        print("=" * 40)
        print("1. Iniciar Juego")
        print("2. Instrucciones")
        print("3. Créditos")
        print("4. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar_snake()

        elif opcion == "2":
            limpiar_pantalla()
            print("INSTRUCCIONES")
            print("- Usa W A S D para mover la serpiente.")
            print("- Come la comida (X) para crecer.")
            print("- Evita chocar con los bordes.")
            print("- Evita chocar contigo mismo.")
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            print("CRÉDITOS")
            print("Desarrollado por: Anthony Alexander Armendáriz Ortiz")
            print("Proyecto Autónomo 2 - Lógica de Programación")
            pausar()

        elif opcion == "4":
            print("\nSaliendo del juego...")
            time.sleep(1)
            break

        else:
            print("\n⚠ Opción inválida.")
            pausar()


# ---------- PROGRAMA PRINCIPAL ----------

if __name__ == "__main__":
    mostrar_menu()