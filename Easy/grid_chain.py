t = int(input('TESTES:'))
n = int(input('SIZE:'))
#abcdefghijklmnopqrstuvwxyz
def imprimegrid(n):
    print(' ')
    for i in n:
        print(i)
    print(' ')

def grid(n):
    pare = 0
    for i in range(0,len(n)):
        n[i] = ''.join(sorted(n[i]))
    imprimegrid(n)
    for i in range(0,len(n) - 1):
        str  = n[i]
        str1 = n[i+1]
        for j in range(0,len(n)):
            if str[j] > str1[j]:
                pare = 1
                break
        if pare == 1 :
            return 'NO'
    return 'YES'

list = list()
for i in range(0,t):
    for i in range(0,n):
        s = input()
        list.append(s)
    resp = grid(list)
print(resp)
