def camelcase(s):
    cont = 1
    for i in s :
        if i.isupper():
           cont += 1
    return cont

s = input()
result = camelcase(s)
print(result)
