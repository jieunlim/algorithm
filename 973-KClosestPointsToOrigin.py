
# 973. K Closest Points to Origin
# O(nlogn)
# O(n)

import heapq
def kClosest(points, K):
    res = []
    heap = []

    for i, point in enumerate(points):
        heapq.heappush(heap, (point[0]**2+point[1]**2, i))

    for _ in range(K):
        res.append(points[heapq.heappop(heap)[1]])

    return res

def kClosest(points, K):
    import heapq
    pq = []
    for i, p in enumerate(points):
        pq.append((p[0]*p[0] + p[1]*p[1], p))
    heapq.heapify(pq)

    return [ heapq.heappop(pq)[1] for _ in range(K)]

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(kClosest(points, K))