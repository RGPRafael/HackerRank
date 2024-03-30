# Complete the closestNumbers function below.
def closestNumbers1(arr):
    m = None
    arr.sort()
    m = abs(arr[0] - arr[1])
    distance.append([ arr[0], arr[1] ])

    for i in range(1,len(arr)-1):
        dif = abs ( arr[i] - arr[i+1])
        if  m > dif :
            distance.pop() ### QUAL O PROBLEMA ? 
            m = dif
            distance.append([ arr[i], arr[i+1] ])

        elif m == dif : distance.append([ arr[i], arr[i+1] ])
        elif m < dif  : continue

    answer = list()
    for i in distance:
        answer.append(i[0])
        answer.append(i[1])

    answer.sort()
    return answer



def closestNumbers(arr):
    m = None
    arr.sort()
    m = abs(arr[0] - arr[1])
    distance = list()

    distance.append([ arr[0], arr[1] ])

    for i in range(1,len(arr)-1):
        dif = abs ( arr[i] - arr[i+1])
        if  m > dif :
            distance = list()
            m = dif
            distance.append([ arr[i], arr[i+1] ])

        elif m == dif : distance.append([ arr[i], arr[i+1] ])

    answer = list()
    for i in distance:
        answer.append(i[0])
        answer.append(i[1])

    return answer

n      = int(input())
arr    = list(map(int, input().rstrip().split()))
result = closestNumbers(arr)
print(result)
