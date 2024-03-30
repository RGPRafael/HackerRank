def saveThePrisoner(n,m,s):
    poisoned = (s + m - 1) % n
    if(poisoned == 0): poisoned = n
    return poisoned





nms = input().split()
n = int(nms[0])
m = int(nms[1])
s = int(nms[2])
result = saveThePrisoner(n, m, s)
print(result)