class Nodo:
    def __init__(self,data):
        self.data= data
        self.siguiente=None
class listaEnlazadaCircular:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def vacia(self):
        return self.primero==None
    def agregar_inicio(self,data):
        if self.vacia():
            self.primero=self.ultimo=Nodo(data)
        else:
            aux=Nodo(data)
            aux.siguiente=self.primero
            self.primero=aux
            self.ultimo.siguiente=self.primero
            

