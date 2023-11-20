#Este script transforma los valores de una matriz 3x3 a 1 o 0 dependiendo de ser pares o impares
matrizUno = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

def elem_matriz(matriz):
    print("Matriz Uno")
    for matUno in matriz:
        print('\t'.join(map(str, matUno)))

    for i in range(0,len(matriz)):
        #print(matriz[i])
        for j in range(0,len(matriz[0])):
            if matriz[i][j] % 2 != 0:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
    print("Matriz Dos")

    for matDos in matriz:
        print('\t'.join(map(str, matDos)))
    return matriz

elem_matriz(matrizUno)
