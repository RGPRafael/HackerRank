def toys(w):
    c = 0
    w.sort()
    minimum = w[0]
    i = 0
    while i <len(w) :
        j = i
        while j < len(w):
            if  minimum + 4 >= w[j] :
                j = j + 1
                continue
            else:
                minimum = w[j]
                break
        c = c + 1
        i = j
    return c

w = list(map(int,input("WEIGHTS: ").split()))
#print(prices)
containers = toys(w)
print(containers)
