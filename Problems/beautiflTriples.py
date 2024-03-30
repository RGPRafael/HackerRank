def beautifulTriplets(d, arr):
    b = 0
    for i in range(0 , len(arr)-2):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] == d:

                for k in range(j + 1 , len(arr)):
                        if arr[k] - arr[j] == d:
                            b = b + 1
    return b

def beautifulTriplets_1(d, arr):
    b = 0
    flag = 0
    for i in range(0 , len(arr)):
        for j in range(i + 1, len(arr)):
            if   arr[j] - arr[i] == d:
                    flag = 1
            elif arr[j] - arr[i] == (2*d) and flag == 1:
                    b = b + 1
        flag = 0
    return b

def beautifulTriplets_2(d, arr):
    b = 0
    for i in range(0 , len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            b+=1

    return b

d = int(input())
arr = list(map(int, input().rstrip().split()))
result = beautifulTriplets(d, arr)
print("R0:", result)
result = beautifulTriplets_1(d, arr)
print("R1:", result)
result = beautifulTriplets_2(d, arr)
print("R2:", result)
