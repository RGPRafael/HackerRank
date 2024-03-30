import random

def Luck(k,contests):
    important      = list()
    not_important  = list()
    result = 0
    for i in range(len(contests)):
        if contests[i][1] == 1: important.append(contests[i][0])
        else:                   not_important.append(contests[i][0])
    important.sort()
    not_important.sort()
    if len(important) > k:
        win = len(important) - k
        for i in range(len(important)):
            if i < win : result = result - important[i]
            else       : result = result + important[i]
        for i in range(len(not_important)):
            result = result + not_important[i]
    else:
        for i in range(len(important)):     result = result + important[i]
        for i in range(len(not_important)): result = result + not_important[i]

    return result

nk = input().split()
n = int(nk[0])
k = int(nk[1])
contests = []

for i in range(n):
    contests.append(list(map(int, input().rstrip().split())))
print(contests)

result = Luck(k,contests)
print(result)
