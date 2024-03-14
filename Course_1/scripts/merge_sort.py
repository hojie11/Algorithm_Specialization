def merge_sort(arr, sorted_arr, left, right):
    inv_count = 0 # inversion counting
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, sorted_arr, left, mid)
        inv_count += merge_sort(arr, sorted_arr, mid + 1, right)
        inv_count += merge(arr, sorted_arr, left, mid, right)
    return inv_count


def merge(arr, sorted_arr, left, mid, right):
    i = left # left sub-array index
    j = mid + 1 # right sub-array index
    k = left # sorted_arr index
    inv_count = 0 # inversion counting

    # check index i is in left sub-array and index j is in right sub-array
    while i <= mid and j <= right:
        # the former is smaller than the latter
        # need to not change
        # thus, there is no inversion
        if arr[i] < arr[j]: 
            sorted_arr[k] = arr[i]
            i += 1
        # the latter is bigger than the former
        # notice that left sub-array and right sub-array are sorted in merge sort algorithm
        # therefore, arr[i:] are bigger than arr[j] and
        # inversion has happend arr[i:] times
        elif arr[i] > arr[j]:
            sorted_arr[k] = arr[j]
            inv_count += (mid - i) + 1
            j += 1
        k += 1

    # copy the remaining elements left sub-array
    while i <= mid:
        sorted_arr[k] = arr[i]
        k += 1
        i += 1
    # copy the remaining elements right sub-array
    while j <= right:
        sorted_arr[k] = arr[j]
        k += 1
        j += 1

    # copy all sorted elements to main array
    for idx in range(left, right + 1):
        arr[idx] = sorted_arr[idx]

    return inv_count
    

if __name__ == '__main__':
    # test case
    arr = [5, 3, 8, 9, 1, 7, 0, 2, 6, 4]
    n = len(arr)
    inv_count = merge_sort(arr, [0] * n, 0, n - 1)
    print(arr, inv_count)
    