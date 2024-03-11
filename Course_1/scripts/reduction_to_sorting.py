def partition(arr, l, r):
    p = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]

    return i


def rSelect(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        idx = partition(arr, l, r)

        if idx - l == k - 1:
            return arr[idx]
        if idx - l > k - 1:
            return rSelect(arr, l, idx - 1, k)
        
        return rSelect(arr, idx + 1, r, k - idx + l - 1)
        

arr = [ 10, 4, 5, 8, 6, 11, 26 ] 
n = len(arr) 
k = 3
print("K-th smallest element is ", end = "") 
print(rSelect(arr, 0, n - 1, k)) 