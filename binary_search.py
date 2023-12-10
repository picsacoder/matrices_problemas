import time
time_start = time.time()

def binary_search(l:list,n_toFind:int):
    l.sort()
    i_izq = 0
    i_rgt = len(l) - 1 

    while i_izq <= i_rgt:
        middle = (i_izq+i_rgt) // 2
        if l[middle] == n_toFind:
            return 'Found {mid} in {time} seconds'.format(mid=middle,time=time.time() - time_start)
        elif l[middle] > n_toFind:
            i_rgt = middle - 1    
            
        else:
            i_izq = middle + 1 
            
    return -1


listD = []
for i in range(0,100):
    listD.append(i)

print(binary_search(listD,54))
