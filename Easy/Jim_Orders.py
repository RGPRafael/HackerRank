def order(a):
    return a[0]

def jimOrders(orders):
    temp = list()
    custumers = list()
    custumer = 1
    for i in orders :
        time_delivered = i[0] + i[1]
        temp.append([time_delivered, custumer])
        custumer = custumer + 1
    temp.sort(key = order)

    for i in temp :
        custumers.append(i[1])

    return custumers

n = int(input())
orders = []
for _ in range(n):
    orders.append(list(map(int, input().rstrip().split())))
result = jimOrders(orders)
print(result)
