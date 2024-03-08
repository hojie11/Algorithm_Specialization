import sys
sys.setrecursionlimit(10**9)


class Counter:
    def __init__(self, n=0):
        self.t = n

    def __call__(self, x=0):
        self.t += x


def first(arr, l, r): return l
def last(arr, l, r): return r
def median(arr, l, r):
    mid = len(arr) // 2
    if len(arr) % 2 == 0: mid -= 1
    L, M, R = arr[l], arr[mid], arr[r]
    order = sorted([(L, l), (M, mid), (R, r)])
    return order[1][1]


def partition(arr, l, r, idx, count=None):
    """ 
    [     < p     | p |     > p     ]
            l      idx        j 
    """
    assert l <= idx <= r
    p = arr[idx]
    arr[l], arr[idx] = arr[idx], arr[l]
    idx = l + 1 # move pointer after the first element of array
    for j in range(idx, r + 1):
        if count: count(1)
        if arr[j] < p: # check if there is a num smaller than pivot
            arr[j], arr[idx] = arr[idx], arr[j] # swap
            idx += 1
    idx -= 1
    arr[l], arr[idx] = arr[idx], arr[l] # recover array to the original
    
    assert all(x < p for x in arr[l:idx]) # left
    assert all(x >= p for x in arr[idx+1:r+1]) # right
    return idx


def quick_sort(arr, l=0, r=None, count=None, pivot=None):
    if r is None: r = len(arr) - 1
    if r - l < 1: return
    idx = pivot(arr, l, r) # pivot index
    idx = partition(arr, l, r, idx, count)
    quick_sort(arr, l, idx - 1, count=count, pivot=pivot)
    quick_sort(arr, idx + 1, r, count=count, pivot=pivot)

    return arr


integer_array = []
with open('Algorithm_Specialization/Course_1/quicksort.txt') as f:
    integer_array = list(map(int, f.readlines()))
n = len(integer_array)
print(n)

arr = [1, 5, 4, 2, 3]

for fn in [first, last, median]:
    arr = integer_array[:]
    count = Counter(0)
    quick_sort(arr, count=count, pivot=fn)
    assert arr == sorted(integer_array)
    print(fn.__name__, count.t)