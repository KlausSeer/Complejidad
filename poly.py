import math 

def polynome(n):
    pol = []
    for i in range(n+1):
        line = input("Ingrese termino de grado %d: "%(i))
        pol.append(line)
    return pol

def p(x, n):
    pol = polynome(n)
    s = 0
    for j in range(n + 1, 0, -1):
        s += ((math.pow(x, j - 1)) * int(pol[j - 1]))
    return s

print("El resultado es: %d"%(p(4,3)))