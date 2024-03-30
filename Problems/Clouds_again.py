def jumpingOnClouds(c, k):
    i = 0
    jumps = 0
    t = 0
    n = 0
    while ( i + k ) % len(c) != 0:
        j = ( i + k ) % len(c)
        if c[i] == 1: t = t + 1
        jumps = jumps + 1
        i = j
    if c[i] == 1: t = t + 1
    jumps = jumps + 1
    e = 100 - jumps - 2*t
    return e

nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c, k)
print(result)
