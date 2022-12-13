import numpy as np

def columna(cadena, rieles):
    for i in range(0, len(cadena)):
        suma = rieles + 2*(rieles-1)*i
        if suma >= len(cadena):
            return suma, i

def cuadricula(cadena, rieles):
    columnas, i = columna(cadena, rieles)
    cuadrícula = np.zeros((rieles,columnas),dtype=str)
    return cuadrícula, i

def x_extra(cadena, rieles):
    suma, i = columna(cadena, rieles)
    if suma != len(cadena):
        num=suma-len(cadena)
        for j in range(0, num):
            cadena=cadena+"x"
    return cadena

def recorrer_diagonal(cadena, rieles):
    cont=0
    cadenax = x_extra(cadena, rieles)
    a, k =cuadricula(cadena, rieles)
    for j in range(0, k+1):
        for i in range(0, rieles):
            a[i,cont]=cadenax[cont].upper()
            cont+=1
            if cont == len(cadenax):
                return a
        for i in range(rieles-2, 0, -1):
            a[i,cont]=cadenax[cont].upper()
            cont+=1
    else:
        return a

def diagonal_completa(cadena, rieles):
    for j in range(0, len(cadena)):
        a= recorrer_diagonal(cadena, rieles)
    return a

cadena="holque"
rieles=3

print(diagonal_completa(cadena, rieles))

#Recorrer la matriz por filas y almacenar en una lista
def codificada(cadena, rieles):
    a=diagonal_completa(cadena, rieles)
    encriptado=""
    for i in range(0, rieles):
        for j in range(0, len(a[0])):
            if a[i,j] != "":
                encriptado += a[i,j]
    return encriptado

print(codificada(cadena, rieles))
