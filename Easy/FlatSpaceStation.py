# É possivel fazer em o(n)?

def flatlandSpaceStations(n, c): #  ainda é O(n²)
    if n == len(c): return 0
    values = list()
    c.sort()
    for i in range(n):
        if i not in c :
            distance = list( map ( lambda num: abs( num - i ), c ) )
            #print(distance)
            values.append(min(distance))
    #print(values)
    return max(values)


nm = input().split()
n = int(nm[0])
m = int(nm[1])
c = list(map(int, input().rstrip().split()))

result = flatlandSpaceStations(n, c)
print(result)
