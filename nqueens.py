#n de reinas y nxn del tablero
n = 6
tablero = []

#creando el tablero
for i in range(0,n):
    tablero.append([])
    for j in range(0,n):

        tablero[i].append(0)


print(tablero[0][1])
xd = 0
while xd < n:
    xd += 1
    print(xd)

    
#for tableroUno in tablero:
#    print('\t'.join(map(str, tableroUno)))
