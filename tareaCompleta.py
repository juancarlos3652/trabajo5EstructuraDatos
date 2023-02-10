class Nodo:
    def __init__(self,data):
        self.data= data
        self.siguiente=None
class ListaCircularSimplementeEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    #Primer ejercicios Agregar ultimo
    def agregarUltimo(self,data):
        if self.vacia():
            self.primero=self.ultimo=Nodo(data)
            self.primero.siguiente=self.primero
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodo(data)
            self.ultimo.siguiente=self.primero
    #Segundo ejercicio Eliminar último
    def eliminarFinal(self):
        if self.vacia():
            print("LISTA VACÍA")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            aux=self.primero
            while aux.siguiente !=self.ultimo:
                aux=aux.siguiente
            aux.siguiente=self.primero
            self.ultimo=aux
    #Tercer ejercicio Lista Vacía
    def vacia(self):
        return self.primero==None    
    #Cuarta ejercicio Agregar Inicio
    def agregarInicio(self,data):
        if self.vacia():
            self.primero=self.ultimo=Nodo(data)
            self.primero.siguiente=self.primero
        else:
            aux=Nodo(data)
            aux.siguiente=self.primero
            self.primero=aux
            self.ultimo.siguiente=self.primero

    #Quinta ejercicio Eliminar Inicio
    def eliminarInicio(self):
        if self.vacia():
            print("LISTA VACÍA")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            self.primero=self.primero.siguiente
            self.ultimo.siguiente= self.primero
    #Sexto ejercicio Mostrar Lista
    def mostrarLista(self):
        aux=self.primero
        while aux:
            print(aux.data)
            aux=aux.siguiente
            if aux==self.primero:
                break
#Menú de opciones:!!-----------------------------------------------------------------------------
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularSimplementeEnlazada()
        while opcion != 7:
            print("--- Lista Simplemente Enlazada ---\n 1. Agregar final\n 2. Eliminar final\n 3. comprobar si la lista está vacía\n 4. Agregar Inicio\n 5. Eliminar Inicio\n 6. Mostrar\n 7. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregarUltimo(dato)
            elif opcion == 2:
                lista.eliminarFinal()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregarInicio(dato)
            elif opcion == 5:
                lista.eliminarInicio()
            elif opcion == 6:
                lista.recorrer()
            elif opcion == 7:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
        

    


