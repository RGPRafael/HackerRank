
lista1 = list(map(int ,input('LISTA 1 :').split()))
lista2 = list(map(int ,input('LISTA 2 :').split()))

#print(lista1)
#print(lista2)

lista1.sort()
lista2.sort()

#print(lista1)
#print(lista2)

quant = 0
value = lista1[len(lista1) - 1]
for v in range(0,lista2[0]):
    p1 = 0
    p2 = 0
    for j in lista1 : # check if have all factors
        if value % j == 0 : continue
        else :
            p1 = 1
            break

    if p1 == 0: # check if is factor of all
        for k in lista2 :
            if k % value == 0: continue
            else:
                p2 = 1
                break
        if p2 == 0:
            quant = quant + 1
            print(value)
    value = value + 1

print(quant)
