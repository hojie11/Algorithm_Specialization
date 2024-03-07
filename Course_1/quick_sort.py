import time
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [range(0, 100000000)]
random.shuffle(arr)

start = time.perf_counter()
arr = quick_sort(arr)
end = time.perf_counter()
print(f"quick_sort,  time: {end - start:.10f}")

start = time.perf_counter()
arr = bubble_sort(arr)
end = time.perf_counter()
print(f"bubble_sort, time: {end - start:.10f}")
#quick_sort,  time: 0.0000005000
#bubble_sort, time: 0.0000012500