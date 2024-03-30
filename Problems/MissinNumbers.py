#USAR CASHING KKKK


def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()
    brr_index   = 0
    arr_index   = 0
    resul_index = 0
    result = list()
    while( arr_index < len(arr) and  brr_index < len(brr)  ):
        if arr[arr_index] != brr[brr_index]  : result.append(brr[brr_index] )
        else                                 : arr_index = arr_index + 1
        brr_index = brr_index + 1

    for i in range(brr_index,len(brr)):
        result.append(brr[i])

    return result


def missingNumbers1(arr, brr):
    arr.sort()
    brr.sort()
    count = 1
    result = list()
    arr_index = 0
    brr_index = 0
    while( arr_index < len(arr)):
        freq_a = 1
        freq_b = 1
        i = arr_index
        j = brr_index
        while(i + 1 < len(arr) and arr[i] == arr[i+1] ):
            freq_a = freq_a + 1
            i = i + 1
        while(j + 1 < len(brr) and brr[j] == brr[j+1] ):
            freq_b = freq_b + 1
            j = j + 1
        if freq_a == freq_b and arr[arr_index] == brr[brr_index] :
            arr_index = i + 1
            brr_index = j + 1

        elif freq_a != freq_b and arr[arr_index] == brr[brr_index]:
            result.append(brr[brr_index])
            arr_index = i + 1
            brr_index = j + 1

        elif freq_a != freq_b and arr[arr_index] == brr[brr_index]:

    return result

n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))
result = missingNumbers(arr, brr)
print(result)
result = missingNumbers1(arr, brr)
print(result)
