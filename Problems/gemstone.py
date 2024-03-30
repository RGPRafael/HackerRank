def gemstones(arr):
    gem = set(arr[0])
    r = gem
    for i in arr[1:] :
        amostra = set(i)
        r = r.intersection(amostra)
    return len(r)



n = int(input())
arr = []

for _ in range(n):
    arr_item = input()
    arr.append(arr_item)

result = gemstones(arr)
print(result)
