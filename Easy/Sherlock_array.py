def balancedSums(arr):

    if len(arr) == 1: return 'YES'
    for i in range(len(arr)):
        esq = 0
        dir = 0
        for j in range(0,i):
            esq = esq + arr[j]
        for k in range(i+1, len(arr)):
            dir = dir + arr[k]
        if esq == dir : return 'YES'
    return 'NO'

def balancedSums1(arr):
    esq = 0
    dir = 0
    if len(arr) == 1: return 'YES'
    middle = int(len(arr)/2)
    for k in range(len(arr)):
            dir = dir + arr[k]
    for i in range(len(arr)):
        esq = esq + arr[i]
        if esq == dir : return 'YES'
        else          : dir = dir - arr[i]
    return 'NO'


T = int(input().strip())

for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        print(result)
        result = balancedSums1(arr)
        print(result)
