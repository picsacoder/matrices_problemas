import math
def main_diagonal_product(mat):
    l = []
    for i in range(0,len(mat)):
        l.append(mat[i][i])
    
    return math.prod(l)
#source: https://www.codewars.com/kata/551204b7509063d9ba000b45