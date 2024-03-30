def pickingNumbers(a):
    # Write your code here
    a.sort()
    size = 1
    count = 1
    for i in range(0,len(a)) :
        for j in range(i+1, len(a)):
            if abs(a[i] - a[j]) <= 1:
                count = count + 1
            else:
                break
        if( size == 1): 
            size = count
        if( count >= size):
            size = count
        count = 1        
                
    return size

l = [ 1, 2, 2, 3, 1, 2]
l1 = [4, 6, 5, 3, 3, 1]
l2 = list()
for i in range(0,100):
    l2.append(66)
#print(l2)
result = pickingNumbers(l2)
print(result)