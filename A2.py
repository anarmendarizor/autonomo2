import os  #sirve para interacturar con el sistema operativo en este caso para limpiar la pantalla de la consola
import time #Pausa el programa durante x tiempo, para que el usuario pueda leer 


def limpiar_pantalla():
    
    #Limpia la pantalla según el sistema operativo.
    
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    
    #Pausa la ejecución hasta que el usuario presione Enter.
    
    input("\nPresiona Enter para continuar...")


# FUNCIONES DEL MENÚ

def mostrar_menu():

    #Muestra el menú principal del juego Snake.
    #Utiliza un ciclo repetitivo para mantenerse activo
   #hasta que el usuario decida salir.


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

   
        #ESTRUCTURA CONDICIONAL
        
        if opcion == "1":
            iniciar_juego_placeholder()

        elif opcion == "2":
            mostrar_instrucciones()

        elif opcion == "3":
            mostrar_creditos()

        elif opcion == "4":
            print("\nSaliendo del juego...")
            time.sleep(1)
            break

        else:
            print("\n⚠ Opción inválida.")
            pausar()



#FUNCIONES PLACEHOLDER


def iniciar_juego_placeholder():
   
    limpiar_pantalla()
    print("Iniciando el juego Snake...")
    print("\n(Aquí se ejecutará el bucle principal del juego)")
    pausar()


def mostrar_instrucciones():
   
    limpiar_pantalla()
    print("INSTRUCCIONES")
    print("- Usa las flechas para mover la serpiente.")
    print("- Come la comida para crecer.")
    print("- Evita chocar con los bordes.")
    print("- Evita chocar contigo mismo.")
    pausar()


def mostrar_creditos():
   
    limpiar_pantalla()
    print("CRÉDITOS")
    print("Desarrollado por: Anthony Alexander Armendáriz Ortiz")
    print("Proyecto Autónomo 2 - Lógica de Programación")
    pausar()



# PROGRAMA PRINCIPAL


if __name__ == "__main__":
    mostrar_menu()
