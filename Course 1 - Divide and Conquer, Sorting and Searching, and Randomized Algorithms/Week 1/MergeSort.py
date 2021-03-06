def merge_sort(arr):
    n = len(arr)
    if (n >= 2):
        A = merge_sort(arr[:int(n/2)])
        B = merge_sort(arr[int(n/2):])
        i = 0
        j = 0
        for k in range(0, n):
            if i < int(n/2) and (j == len(B) or A[i] <= B[j]):
                arr[k] = A[i]
                i = i + 1
            else:
                arr[k] = B[j]
                j = j + 1
    return arr


arr = input()
arr = [(int(num)) for num in arr.split()]

print(merge_sort(arr))