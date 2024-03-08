from time import time


# find closest number to k in given 1d list
def nearest(l, v):
    return l[min(range(len(l)), key=lambda i: abs(l[i] - v))]


# faster method
# using sort and abs functions
def nearest2(l, v):
    l.sort()
    closest_num = l[0]
    for num in l:
        if (num - v) < abs(closest_num - v):
            closest_num = num
        if num > v:
            break
    return closest_num

l = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
k = 9
start = time()
print(nearest(l, k))
print(time() - start)

start = time()
print(nearest2(l, k))
print(time() - start)