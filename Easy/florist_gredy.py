def getMinimumCost(k,c):
    custo_total = 0
    c.sort()
    flowers = 0
    j = len(c) - 1
    while j >= 0  :
        i = 0
        while( i < k and j >= 0 ):
            preco = (flowers + 1)*c[j]
            custo_total = custo_total + preco
            i = i + 1
            j = j - 1
        flowers = flowers + 1
    return custo_total




nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
minimumCost = getMinimumCost(k, c)
print(minimumCost)
