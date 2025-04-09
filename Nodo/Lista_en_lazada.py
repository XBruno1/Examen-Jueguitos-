class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class NodoConcreto(Nodo):
    def __init__(self, valor):
        super().__init__(valor)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = NodoConcreto(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"{nodo_actual.valor} -> ", end="")
            nodo_actual = nodo_actual.siguiente
        print("None")