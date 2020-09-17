# 323. Number of Connected Components in an Undirected Graph
# https://youtu.be/ibjEGG7ylHk


from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(e):
            while root[e] != e:
                root[e], e = root[root[e]], root[e]
            return e

        def union(e0, e1, cnt):
            if e0 != e1:
                root[e1] = e0
                cnt -= 1
            return cnt

        if n <= 0: return 0
        root = [i for i in range(n)]
        cnt = n
        for edge in edges:
            e0 = find(edge[0])
            e1 = find(edge[1])
            cnt = union(e0, e1, cnt)

        return cnt

edges = [[0, 1], [1, 2], [3, 4]]
# edges = [[0, 1], [1, 2], [2, 3], [1,3], [3, 4]]
n = 5

obj = Solution()
print(obj.countComponents(n, edges))

def countComponents1(n, edges):
    def dfs(n, g, visited):
        if visited[n]:
            return
        visited[n] = 1
        for x in g[n]:
            dfs(x, g, visited)

    visited = [0] * n
    g = {x: [] for x in xrange(n)}
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    ret = 0
    for i in xrange(n):
        if not visited[i]:
            dfs(i, g, visited)
            ret += 1

    return ret

def countComponents2(n, edges):
    g = {x: [] for x in xrange(n)}
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    ret = 0
    for i in xrange(n):
        queue = [i]
        ret += 1 if i in g else 0
        for j in queue:
            if j in g:
                queue += g[j]
                del g[j]

    return ret

def countComponents3(n, edges):
    def find(x):
        print(f"[find] x = {x}")
        if parent[x] != x:
            parent[x] = find(parent[x])
        print(f"parent = {parent}")
        return parent[x]

    def union(xy):
        print(f"[union] xy = {xy}")
        x, y = map(find, xy)
        print(f" x={x}, y={y}")
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    parent, rank = range(n), [0] * n
    print(f"edges={edges}")
    # map(union, edges)
    for i in edges:
        union(i)
    print(f"2")

    return len({find(x) for x in parent})

def countComponents(n, edges):
    arr = [i for i in range(n)]
    print(f"arr={arr}")
    for x in edges:
        print(f"x={x}, n={n}")
        t1 = x[0]
        print(f"t1={t1}")
        while arr[t1]!=t1:
            arr[t1],t1 = arr[arr[t1]],arr[t1]
            print(f"arr[t1]={arr[t1]}, t1={t1}")

        t2 = x[1]
        print(f"t2={t2}")
        while arr[t2]!=t2:
            arr[t2],t2 = arr[arr[t2]],arr[t2]
            print(f"arr[t2]={arr[t2]}, t2={t2}")

        # Union
        if t1!=t2:
            arr[t2] = t1
            n-=1
            print(f"n={n}")
        print(f"arr={arr}")
    return n
