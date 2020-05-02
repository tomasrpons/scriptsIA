import numpy as np


class Vector:
    def __init__(self, vector,q):
        self.vector_entero = vector
        self.vector = np.delete(vector,-1)
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

    cant= int(input('Introduzca la cantidad de usuarios con valores conocidos: '))

    cant_vecinos = int(input('Introduzca la cantidad de vecinos mas cercanos: '))

    vec=[]

    for i in range(cant):

        aux=input('Introduzca las calificaciones para el usuario %i: '%(i+1) ).split(',')

        for j in range(len(aux)):

            aux[j] = int(aux[j])
        vec.append(aux)
    datos=np.array(vec)

    q = input("Introduzca los valores de Q (valores separados por comas): ").split(",")

    for i in range(len(q)):
        q[i] = int(q[i])
        
    array = []

    for i in range(len(datos)):
        v = Vector(datos[i],q)
        array.append(v)

    vectores = bubbleSort(array)
    ganadores = vectores[:cant_vecinos]

    aux = 0
    for i in range(len(ganadores)):
        aux += ganadores[i].vector_entero[-1]
    promedio = aux/cant_vecinos

    print("La prediccion de puntaje de la pelicula  para Q es de: ", promedio)


if __name__ == "__main__":
    main()