import numpy as np


class Vector:
    def __init__(self, vector,q):
        self.vector_entero = vector
        self.vector = np.delete(vector,3)
        self.dis = np.linalg.norm(self.vector-q)
    

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i].dis>nlist[i+1].dis:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist


def main():
    print("-"*20)
    entrada = input("Introduzca los valores de Q (3 valores separados por comas): ")
    entrada = entrada.split(",")
    for i in range(len(entrada)):
        entrada[i] = int(entrada[i])
    q = np.array(entrada)
        
    array = []
    datos = np.load('calificaciones_pelis.npy')

    for i in range(len(datos)):
        v = Vector(datos[i],q)
        array.append(v)

    vectores = bubbleSort(array)
    ganadores = vectores[:3]

    aux = 0
    for i in range(len(ganadores)):
        aux += ganadores[i].vector_entero[-1]
    promedio = aux/3

    print("La prediccion de puntaje de la pelicula 4 para Q es de: ", promedio)


if __name__ == "__main__":
    main()