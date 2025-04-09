class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def __repr__(self):
        return f"Nodo(valor={self.valor})"