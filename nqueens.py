#n de reinas y nxn del tablero
n = 6
tablero = []

#creando el tablero
for i in range(0,n):
    tablero.append([])
    for j in range(0,n):

        tablero[i].append([0])

        
print(tablero[1][1][0])
    
for tableroUno in tablero:
    print('\t'.join(map(str, tableroUno)))
