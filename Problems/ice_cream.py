### USAR BINARY SEARCH TALVEZ 


def icecreamParlor(m, arr):
    copy_arr = arr.copy()
    copy_arr.sort()
    res = list()

    for i in range(len(copy_arr)) :
            f1 = copy_arr[i]
            f2 = m - f1
            if f2 in copy_arr :
                p  = arr.index(f1)
                s  = arr.index(f2)
                if p == s :
                    if f2 in copy_arr[ p + 1 : ]:
                       s = arr.index(f2, p + 1)
                       print('x')
                       res.append(p + 1)
                       res.append(s + 1)
                       break
                    elif f2 in copy_arr[ : p + 1]:
                       print('x1')
                       s = arr.index(f2, 0, p + 1)
                       res.append(p + 1)
                       res.append(s + 1)
                       break
                    else : continue

                else :
                    res.append(p + 1)
                    res.append(s + 1)
                    break
            else : continue
    return res

t = int(input())

for t_itr in range(t):
    m      = int(input())
    n      = int(input())
    arr    = list(map(int, input().rstrip().split()))
    result = icecreamParlor(m, arr)
    print(result)
