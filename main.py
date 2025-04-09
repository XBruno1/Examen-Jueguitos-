
from Hanoi.torres_de_Hanoi import TorresDeHanoi
from Nodo.Lista_en_lazada import ListaEnlazada
from Caballo.Lanzador import Lanzador
from Reian.lanzador import NQueens

def ejecutar_torres_de_hanoi():
    print("Ejecutando Torres de Hanoi...")
    discos = 3
    hanoi = TorresDeHanoi(discos)
    print("Estado inicial:")
    print(hanoi)
    hanoi.resolver()
    print("Estado final:")
    print(hanoi)

def ejecutar_lista_enlazada():
    print("Ejecutando Lista Enlazada...")
    lista = ListaEnlazada()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    print("Lista enlazada:")
    lista.mostrar()

def ejecutar_caballos():
    print("Ejecutando simulación de Caballos...")
    Lanzador.ejecutar_simulacion()

def ejecutar_reinas():
    print("Ejecutando simulación de N-Reinas...")
    n = 8  # Cambia el tamaño del tablero aquí
    juego = NQueens(n)
    juego.run_visualization()

def main():
    print("Selecciona una opción:")
    print("1. Torres de Hanoi")
    print("2. Lista Enlazada")
    print("3. Simulación de Caballos")
    print("4. Simulación de N-Reinas")
    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        ejecutar_torres_de_hanoi()
    elif opcion == "2":
        ejecutar_lista_enlazada()
    elif opcion == "3":
        ejecutar_caballos()
    elif opcion == "4":
        ejecutar_reinas()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()