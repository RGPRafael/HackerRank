def q (n):
    if n == 1:
        return 11
    return q(n-1) * 11

def q1(n):
    if n == 1:
        return 1
    return 11*q1(n-1) + 12


n = int(input())
print(q(n))
print(q1(n))

