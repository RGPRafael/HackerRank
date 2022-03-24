# localizacao e alcance de antena
n = list(map(int, input('HOUSES: ').split()))
k = int(input('K:'))

n.sort()
#print(n)
antenas = 0
i  = 0
while i < len(n):  ## find the minimum number of radios
    alcance =  n[i] + k
    while( i < len(n) and n[i] <= alcance): i = i + 1
    i = i - 1
    #print(n[i])
    antenas = antenas + 1
    alcance =  n[i] + k
    while( i < len(n) and n[i] <= alcance): i = i + 1
print(antenas)
