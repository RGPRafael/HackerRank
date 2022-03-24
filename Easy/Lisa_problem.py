### NOT FINISHED

def workbook(n,k,arr):
	special_problems = 0
	page = 1
	for i in range(len(arr)):
		problems_in_chapter = arr[i]
		page_in_chapter = 1
		for j in range(1,problems_in_chapter + 1):
	return special_problems     


nk  = input().split()
n   = int(nk[0])
k   = int(nk[1])
arr = list(map(int, input().rstrip().split()))
result = workbook(n, k, arr) 
print (result)

