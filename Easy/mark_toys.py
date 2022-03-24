def buy(prices,k):
    toys = 0
    prices.sort()
    for i in prices :
        if i <= k :
            k = k - i
            toys = toys + 1
    return toys



k = int(input("BUDGET: "))
prices = list(map(int,input().split()))
#print(prices)
result = buy(prices,k)
print(result)
