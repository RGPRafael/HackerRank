def happyLadybugs(b):   #B_RRBR
    cont = 1
    if '_' in b :
        c = b.replace('_','') #BRRBR
        for i in c :
            count = b.count( i )
            if count != 1: continue
            else         : return 'NO'
        return 'YES'

    else:
        for i in b :
            count = b.count( i )
            if count != 1:
                 x = b.index(i)
                 y = b.index(i,x+1)
                 if ( y - x ) != 1 : return 'NO'
                 continue
            else : return 'NO'

    return 'YES'

g = int(input())

for g_itr in range(g):
    n = int(input())
    b = input()
    result = happyLadybugs(b)
    print(result)
