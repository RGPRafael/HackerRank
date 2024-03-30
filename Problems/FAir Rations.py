# Complete the fairRations function below.
def fairRations(B):
    s = 0
    bread = 0
    for i in B:
    	s = s + i
    if s % 2 != 0 :
    	return 'NO'
    for i in range(len(B)):
        if B[i] % 2 == 0 : continue
        elif B[i] % 2 != 0 and i == 0:
            B[i]   =  B[i]   + 1
            B[i+1] =  B[i+1] + 1
            bread = bread + 2

        elif B[i] % 2 != 0 and i == len(B) - 1:
               B[i]   =  B[i]   + 1
               B[i-1] =  B[i-1] + 1
               bread = bread + 2

        elif   B[i] % 2 != 0 :
               B[i] = B[i] + 1
               bread = bread + 1
               if  B[i-1] % 2 != 0 :
                   B[i-1] = B[i-1] + 1
                   bread = bread + 1

               elif B[i+1] % 2 != 0 :
                    B[i+1] = B[i+1] + 1
                    bread = bread + 1

               else  :
                    B[i+1] = B[i+1] + 1
                    bread = bread + 1
    return bread

N = int(input())

B = list(map(int, input().rstrip().split()))

result = fairRations(B)
print(result)
