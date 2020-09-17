# 1514. Path with Maximum Probability

from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        import heapq
        from collections import defaultdict
        dic = defaultdict(list)
        for i, e in enumerate(edges):
            dic[e[0]].append((e[1], succProb[i]))
            dic[e[1]].append((e[0], succProb[i]))

        #         dic={0:[(1, 0.5),(2, 0.3)], 1:[(2, 0.5)]}
        visited = set()
        pq = []
        for t, w in dic[start]:
            heapq.heappush(pq, (-w, t))
            # (-0.5, 1) (-0.3, 2)

        while pq:
            w, t = heapq.heappop(pq)
            visited.add(t)
            if t == end:
                return -w

            for t1, w1 in dic[t]:
                if t1 not in visited:
                    heapq.heappush(pq, (w * w1, t1))

        return 0

# O(VlogV + ElogV)
# O(V+E)

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
# Output: 0.25000
obj = Solution()
print(obj.maxProbability(n, edges, succProb, start, end))