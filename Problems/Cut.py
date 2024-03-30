arr    = list(map(int, input('Sticks: ').split()))
result = list()
while len(arr) != 0:
    arr.sort()
    result.append(len(arr))
    zeros = 0
    for i in arr:
        i = i - arr[0];
        if i == 0: zeros = zeros + 1
    for i in range(0,zeros):
        arr.pop(0)
print(result)
