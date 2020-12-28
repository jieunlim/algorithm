# O(m + nlogn)-m is number of edges and n is number of nodes.  O(E+nlgn)

import collections
import heapq
class Solution:
    def findCheapestPrice(self, n, edges , src, dst, K):
        import heapq, collections

        pq = [(0, src, K+1)]
        graph = collections.defaultdict(dict)

        for s, d, c in edges:
            graph[s][d] = c

        while pq:
            cost, src, stops = heapq.heappop(pq)

            if src == dst: return cost

            if stops > 0:
                for neighbor in graph[src]:
                # for n in graph[src].keys():
                    heapq.heappush(pq,
                                   (cost + graph[src][neighbor],
                                    neighbor,
                                    stops-1))

        return -1

 # Dijkstra
    def findCheapestPrice_D(self, n, flights, src, dst, K):
        import collections
        import heapq

        pq, g = [(0, src, K + 1)], collections.defaultdict(dict)
        # visited = set()
        print(f"pq={pq} g={g}")

        for s, d, c in flights:
            g[s][d] = c
        print(f"g={g}")

        while pq:
            cost, src, k = heapq.heappop(pq)
            print(f" [while] src={src}, k={k}, cost={cost}")

            # if src in visited: continue
            # visited = visited | {src}

            if src == dst:
                return cost
            if k:
                for v2 in g[src]:
                    print(f"  [for] dst={v2}")
                    heapq.heappush(pq, (cost + g[src][v2], v2, k - 1))
                    print(f"      pq={pq}")
        return -1

    def findCheapestPrice3(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        pq = []

        for u, v, w in flights: graph[u].append((w, v))

        heapq.heappush(pq, (0, K + 1, src))
        while pq:
            price, stops, city = heapq.heappop(pq)

            if city is dst: return price
            if stops > 0:
                for price_to_nei, nei in graph[city]:
                    heapq.heappush(pq, (price + price_to_nei, stops - 1, nei))
        return -1


    def findCheapestPrice_test(self, n, flights, src, dst, K):
		# Build the graph:
        from collections import defaultdict
        d = defaultdict(list)
        for u, v, w in flights:
            d[u].append((w,v)) # directed

        # Apply Dijkstra:
        from heapq import heappop, heappush
        h = [(0, -1, src)] # cost, k, node
        weights = {} # instead of pre-processing the weights dict with placeholder values of inf and 0, we do it on the fly
        while h:
            cost, k, node = heappop(h)
            if cost > weights.get((k, node), float('inf')) or \
            k > K:
                continue # don't even bother to add to heap
            if node == dst:
                return cost
            for edgeCost, nei in d[node]:
                newCost = edgeCost + cost
                if weights.get((k+1, nei), float('inf')) > newCost:
                    weights[(k+1, nei)] = newCost
                    heappush(h, (newCost, k+1, nei))
        return -1 # all nodes visited but no dst found, so return -1
# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]

# n = 4
# edges = [[0,1,100],[0,2,500],[0,3,40],[1,2,50],[3,2,200]]
# src=0
# dst=1
# k=1

# n=4
# edges = [
#         ("A", "B", 70),
#         ("A", "C", 20),
#         ("A", "D", 50),
#         ("B", "C", 10),
#         ("B", "D", 90),
#         ("C", "D", 5),
#     ("C","A",1),
#     ("D","C",2)]
# src = "A"
# dst = "D"
# k = 2

edges=[[0,1,10],[0,2,50],[1,2,10],[2,3,10],[1,3,40]]
n=4
src=0
dst=3
k=1

n=5
edges=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src=2
dst=1
k=1
# result: -1

n=5
edges=[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
src=0
dst=4
k=1
# result:5
obj = Solution()
# print(obj.findCheapestPrice(n, edges, src, dst, k))
print(obj.findCheapestPrice_D(n, edges, src, dst, k))
# print(obj.findCheapestPrice3(n, edges, src, dst, k))
# print(obj.findCheapestPrice_test(n, edges, src, dst, k))