def candies(arr):
    cand = [None] * len(arr)
    for i in range(len(arr)):
        if i == 0 : cand[i] = 1
        elif i == len(arr) - 1 and arr[i-1] < arr[i] : cand[i] = cand[i-1] + 1
        elif i == len(arr) - 1 and arr[i-1] >= arr[i] : cand[i] = 1
        elif arr[i] <= arr[i+1] :
            if arr[i-1] < arr[i] : cand[i] = cand[i-1] + 1
            else : cand[i] = 1
        else :
            if arr[i-1] < arr[i] : cand[i] = cand[i-1] + 1
            else : cand[i] = 2
    return sum(cand)


n   = int(input())
arr = list(map(int, input().rstrip().split()))
c = candies(arr)
print(c)
