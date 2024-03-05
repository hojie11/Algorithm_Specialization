# given n points in the plane, find out the closest pair of points
# 
import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def min(x, y):
    return x if x < y else y


def BruteForce(P, n):
    m_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < m_dist:
                m_dist = dist(P[i], P[j])
    return m_dist


def StripClosest(strip, n, d):
    m_dist = d
    strip = sorted(strip, key=lambda p: p.y) # sort point's array according y coordinates

    # here is trick
    # it looks like o(n^2), but actually o(nlogn)
    # in the worst case, is is going to be o(n^2)
    for i in range(n):
        for j in range(i + 1, n):
            if (strip[j].y - strip[i].y) <= m_dist:
                m_dist = dist(strip[i], strip[j])
            if dist(strip[i], strip[j]) < m_dist:
                break
    return m_dist


def ClosestUtil(P, n):
    if n <= 3:
        return BruteForce(P, n)
    mid = n // 2 # find middle point of list
    mid_point = P[mid]
    # divide the given list int two halves
    # recursively find the smallest distance in both sub-array
    dl = ClosestUtil(P, mid)
    dr = ClosestUtil(P[mid:], n - mid)
    d = min(dl, dr) # get bound of minimum distance 
    strip = []
    for i in range(n):
        if abs(P[i].x - mid_point.x) < d: # gather points closer to the mid point in bound of minimum distance
            strip.append(P[i])
    return min(d, StripClosest(strip, len(strip), d))


def closest(P, n):
    P = sorted(P, key=lambda p: p.x) # sort array according x coordinates
    return ClosestUtil(P, n)


P = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
n = len(P)
print("The smallest distance is", closest(P, n))