L = [2,3,5,6,8,9,1]
V = 11

def combinaciones(c):
    if(len(c) == 0):
        return [[]]
    else:
        ultimo = combinaciones(c[:-1])
        return ultimo + [listaC + [c[-1]] for listaC in ultimo]

def losQueSeSuman (L,V):
    return [x for x in combinaciones(L) if sum(x) == V]

print(losQueSeSuman(L, V))
 