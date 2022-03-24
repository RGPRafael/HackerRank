def jumpingOnClouds(clouds):
    jumps = 0
    i = 0
    while i < len(clouds) - 1 :

        if  i+2 < len(clouds) and clouds[i] == 0 and clouds[i+2] == 0:
            jumps = jumps + 1
            i = i + 2
        elif i+1 < len(clouds) and clouds[i] == 0 and clouds[i+1] == 0:
            jumps = jumps + 1
            i = i + 1

    return jumps

c = list(map(int, input().rstrip().split()))
print( jumpingOnClouds(c) )
