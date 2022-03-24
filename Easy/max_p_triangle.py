def maximumPerTringle(sticks):
    possibles_tringles = list()
    sticks.sort()
    for i in range(len(sticks)-2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            possibles_tringles.append([ sticks[i], sticks[i+1], sticks[i+2] ])

    quant_tringle = len(possibles_tringles)
    if quant_tringle > 1:
        if possibles_tringles[quant_tringle -1 ][2] > possibles_tringles[quant_tringle -2 ][2]:
            triangle = possibles_tringles[quant_tringle -1 ]

        elif possibles_tringles[quant_tringle -1 ][0] > possibles_tringles[quant_tringle -2 ][0]:
            triangle = possibles_tringles[quant_tringle -1 ]

        else : triangle = possibles_tringles[quant_tringle -1 ]

    elif quant_tringle == 1:
        triangle = possibles_tringles[0]

    else : triangle = -1
    return triangle

n = int(input())
sticks = list(map(int, input().rstrip().split()))
array = maximumPerTringle(sticks)
print(array)
