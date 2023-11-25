def get_matrix(n):
    l = []
    for i in range(0,n):
        l.append([])
        while len(l[i]) < n:
            l[i].append(0)
        l[i][i] = 1
        
    
    return l
#source: https://www.codewars.com/kata/5a34da5dee1aae516d00004a