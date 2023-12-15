def matrix_mult(a, b):
  r = []
  
  for i in range(0,len(a)): #len(a) = 2, rows
    r.append([])
    for j in range(0,len(b[0])): 
      r[i].append(0)
      for k in range(0,len(b)):
        r[i][j] += a[i][k] * b[k][j]
  return r

matrix_mult([[1,2],[3,2]],[[3,2],[1,1]])

