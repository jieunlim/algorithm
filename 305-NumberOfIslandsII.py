# 305. Number of Islands II
# start ** 0, 0, visited=set(), 0
#  self.islands=1
# start ** 0, 1, visited={(0, 0)}, 1
# [union] i=0, j=1, x=0, y=0
#   [union] i=0, j=1
#     [find] i=0, j=1, parents={}
#       return
#   [union] x=0, y=0
#     [find] i=0, j=0, parents={}
#       return
#   parents={(0, 1): (0, 0)}, self.islands=1
#  self.islands=1
# start ** 1, 2, visited={(0, 1), (0, 0)}, 1
#  self.islands=2
# start ** 2, 1, visited={(0, 1), (1, 2), (0, 0)}, 2
#  self.islands=3
# start ** 1, 1, visited={(0, 1), (1, 2), (2, 1), (0, 0)}, 3
# [union] i=1, j=1, x=2, y=1
#   [union] i=1, j=1
#     [find] i=1, j=1, parents={(0, 1): (0, 0)}
#       return
#   [union] x=2, y=1
#     [find] i=2, j=1, parents={(0, 1): (0, 0)}
#       return
#   parents={(0, 1): (0, 0), (2, 1): (1, 1)}, self.islands=3
# [union] i=1, j=1, x=0, y=1
#   [union] i=1, j=1
#     [find] i=1, j=1, parents={(0, 1): (0, 0), (2, 1): (1, 1)}
#       return
#   [union] x=0, y=1
#     [find] i=0, j=1, parents={(0, 1): (0, 0), (2, 1): (1, 1)}
#      n=0, m=0
#     [find] i=0, j=0, parents={(0, 1): (0, 0), (2, 1): (1, 1)}
#       return
#   parents={(0, 1): (0, 0), (2, 1): (1, 1), (1, 1): (0, 0)}, self.islands=2
# [union] i=1, j=1, x=1, y=2
#   [union] i=1, j=1
#     [find] i=1, j=1, parents={(0, 1): (0, 0), (2, 1): (1, 1), (1, 1): (0, 0)}
#      n=0, m=0
#     [find] i=0, j=0, parents={(0, 1): (0, 0), (2, 1): (1, 1), (1, 1): (0, 0)}
#       return
#   [union] x=1, y=2
#     [find] i=1, j=2, parents={(0, 1): (0, 0), (2, 1): (1, 1), (1, 1): (0, 0)}
#       return
#   parents={(0, 1): (0, 0), (2, 1): (1, 1), (1, 1): (0, 0), (1, 2): (0, 0)}, self.islands=1
#  self.islands=1

class Solution:
    def numIslands2(self, m: int, n: int, positions):
        self.islands = 0

        def find(i, j):
            print(f"    [find] i={i}, j={j}, parents={parents}")
            if (i, j) not in parents:
                print(f"      return")
                return i, j
            # parents[(i, j)] = find(*parents[(i, j)])
            n, m = parents[(i, j)]
            print(f"     n={n}, m={m}")
            parents[(i, j)] = find(n, m)
            return parents[(i, j)]

        def union(i, j, x, y):
            print(f"[union] i={i}, j={j}, x={x}, y={y}")
            print(f"  [union] i={i}, j={j}")
            p = find(i, j)
            print(f"  [union] x={x}, y={y}")
            q = find(x, y)
            p, q = min(p, q), max(p, q)

            if p != q:
                parents[q] = p
                self.islands -= 1
            print(f"  parents={parents}, self.islands={self.islands}")

        def helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return

            visited.add((i, j))
            self.islands += 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) in visited:
                    union(i, j, x, y)

        if not positions: return []

        res, visited, parents = [], set(), {}
        for i, j in positions:
            print(f"start ** {i}, {j}, visited={visited}, {self.islands}")
            helper(i, j)
            print(f" self.islands={self.islands}")
            res.append(self.islands)

        return res

m = 3
n = 3
# positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
positions = [[0, 0], [0, 1], [1, 2], [2, 1],[1,1]]
obj = Solution()
print(obj.numIslands2(m, n, positions))

class Solution2(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = Union()
        print(f"positions={positions}")
        for p in map(tuple, positions):
            print(f"p={p}")
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.union(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1
        print(f"[add] id={self.id[p]}, sz={self.sz[p]}, count={self.count}")

    def root(self, i):
        print(f"[root] i={i}, self.id={self.id}")
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def union(self, p, q):
        print(f"[union] p={p}, q={q}")
        i, j = self.root(p), self.root(q)
        print(f"  i={i}, j={j}, sz={self.sz}")
        if i == j:
            print(f"  return")
            return

        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1
        print(f"   id={self.id}, sz={self.sz}, count={self.count}")


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1],[1,1]]
obj = Solution2()
# print(obj.numIslands2(m, n, positions))


from typing import List
class Solution3:
    def numIslands2(self, m: int, n: int, positions):
        visited, parent = set(), {}
        self.islands = 0

        def add(i, j):
            print(f"[add] i={i}, j={j}")
            # location is outside the grid
            if not (0 <= i < m and 0 <= j < n) or (i, j) in visited: return

            visited.add((i, j))
            self.islands += 1
            print(f"    visited={visited}, self.islands={self.islands}")

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (x, y) in visited: union(i, j, x, y)

        def find(i, j):
            if (i, j) not in parent: return i, j
            parent[i, j] = find(*parent[i, j])
            return parent[i, j]

        def union(i, j, x, y):
            print(f" union i={i}, y={j}, x={x}, y={y}")
            p, q = find(i, j), find(x, y)
            # dist = lambda x: x[0] ** 2 + x[1] ** 2
            print(f"p={p}, q={q}")
            p, q = min(p, q), max(p, q)
            print(f"p={p}, q={q}")
            if p != q:
                # print('merge components')
                parent[q] = p
                self.islands -= 1
                print(f"parent={parent}, self.islands={self.islands}")

        ans = []
        for i, j in positions:
            add(i, j)
            # print(grid)
            ans.append(self.islands)
            print(f"ans = {ans}")

        return ans
