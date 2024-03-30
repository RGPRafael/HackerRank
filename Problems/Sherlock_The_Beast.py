def decentNumber(n):
    it = 0
    ints = [1] * n
    full_of_ones = int("".join(map(str,ints)))
    possible = 5 * full_of_ones
    low = 3 * full_of_ones
    digits_five = n
    digits_three = 0

    while it <= n :
        if   digits_five % 3 == 0  and digits_three == 0     : break
        elif digits_five % 3 == 0  and digits_three % 5 == 0 : break
        elif digits_five == 0      and digits_three % 5 == 0 : break
        possible = possible - (2 * 10**it)
        digits_five  = digits_five  - 1
        digits_three = digits_three + 1
        it = it + 1

    if possible >= low : print(possible)
    else: print(-1)
    #print(digits_five,digits_three)

t = int(input().strip())
for t_itr in range(t):
    n = int(input().strip())
    decentNumber(n)
