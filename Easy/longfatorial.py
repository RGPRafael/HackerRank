import math
n = int(input('n: '))
emput = n
fat = 1
# naive version
while(n != 1 ):
    fat = n * fat
    n = n - 1
print(fat)

fat = 1
for i in range(1,emput+1):
    fat = i * fat
print(fat)

print(math.factorial(emput))
