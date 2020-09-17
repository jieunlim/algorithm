# 882. Reachable Nodes In Subdivided Graph
# Dijkstra
# BFS- non weighted, Prim's-find the lowest weight edge to connect all vertices
class Solution(object):

    # Dijkstra (Solution approach 1)
    def reachableNodes(self, edges, M, N):
        import collections, heapq

        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        max_dist = {0: 0}
        used = {}
        ans = 0

        print(f"graph = {graph}")
        print(f"max_dist={max_dist}")
        while pq:
            cur_dist, node = heapq.heappop(pq)
            print(f"[pop] cur_dist={cur_dist}, node={node}")

            if cur_dist > max_dist[node]: continue
            # Each node is only visited once.  We've reached a node in our original graph.
            ans += 1

            for nei in graph[node]:
                print(f" [for] nei={nei}")

                c_move_cnt = min(graph[node][nei], M - cur_dist) #how much further we can walk from this node
                used[node, nei] = c_move_cnt

                print(f"   c_move_cnt={c_move_cnt}, used={used}")

                t_dist_to_nei = cur_dist + graph[node][nei] + 1
                print(f"   t_dist_to_nei={t_dist_to_nei}, max_dist.get(nei, M+1)={max_dist.get(nei, M+1)}, max_dist={max_dist}")

                if t_dist_to_nei < max_dist.get(nei, M+1):
                    heapq.heappush(pq, (t_dist_to_nei, nei))
                    max_dist[nei] = t_dist_to_nei
                    print(f" pq = {pq}, max_dist={max_dist}")

            print(f"......pq={pq}")

        print(f"ans={ans}, max_dist={max_dist}")
        for u, v, w in edges:
            print(f"u={u}, v={v}, w={w}, used.get((u, v), 0)={used.get((u, v), 0)} + used.get((v, u), 0)={used.get((v, u), 0)}")
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
            print(f" ans = {ans}, used={used}")

        return ans

    # BFS
    def reachableNodes_bfs(self, edges, M, N):
        from collections import defaultdict
        m_edges = defaultdict(dict)

        for u, v, t in edges:
            m_edges[u][v] = t
            m_edges[v][u] = t

        cnt = 1
        q = [(0, M)]

        covered = defaultdict(int)
        visited = defaultdict(int)
        visited[0] = M

        print(f"m_edges={m_edges}")
        while q:
            u, m = q.pop(0)
            print(f"[pop] u={u}, m={m}")
            for v in m_edges[u]:
                t = m_edges[u][v]

                print(f"   v={v}, t={t}, visited={visited}")
                if t + 1 <= m:
                    if v not in visited:
                        cnt += 1
                    print(f"{m-t+1}, visited[v] = {visited[v]}")
                    if m - (t + 1) > visited[v]:
                        q.append([v, m - (t + 1)])
                        visited[v] = m - (t + 1)
                        print(f"q = {q}, visited={visited}")

                print(f"covered = {covered}, covered[u, v] {covered[u, v]} + covered[v, u] {covered[u, v]}")
                if (covered[u, v] + covered[v, u] >= t):
                    continue

                cnt += max(0, min(m, t) - covered[u, v]) - \
                       (max(0, covered[v, u] - (t - min(m, t))))
                print(f"cnt = {cnt}")
                covered[u, v] = min(m, t)
        return cnt


    # Prim's - finds a minimum spanning tree for a weighted undirected graph
    def reachableNodes_prims(self, edges, M, N):
        import collections, heapq

        adj = [[] for u in range(N)]
        reached = collections.Counter()
        for u, v, n in edges:
            adj[u].append([v, n])
            adj[v].append([u, n])

        budgets = [-1] * N  # initial budgets[u] must be -1 NOT 0; if 0 were used, this node u may never be visited.
        budgets[0] = M

        heap = []
        heap.append([-M, 0])

        ans = 0
        while heap:
            cur = heapq.heappop(heap)
            budget = -cur[0]
            u = cur[1]
            if budget < budgets[u]: continue  # outdated heap element
            ans += 1
            for v, n in adj[u]:
                reached[u, v] = budget
                if budget - n - 1 > budgets[v]:  # relax edge operation
                    heapq.heappush(heap, [-(budget - n - 1), v])
                    budgets[v] = budget - n - 1

        for u, v, n in edges: ans += min(n, reached[u, v] + reached[v, u])
        return ans

edges = [[0,1,10],[0,2,1],[1,2,2]]
M = 6
N = 3

# edges = [[0,1,5],[0,3,5],[1,2,5], [3,2,1],[0,2,2]]
# M = 6
# N = 4

obj = Solution()
# print(obj.reachableNodes_bfs(edges, M, N))
print(obj.reachableNodes(edges, M, N))
# print(obj.reachableNodes_prims(edges, M, N))


'''
class Solution(object):
    # Dijkstra (Solution approach 1)
    def reachableNodes(self, edges, M, N):
        import collections, heapq

        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq, max_dist, used, ans = [(0, 0)], {0: 0}, {}, 0

        while pq:
            cur_dist, node = heapq.heappop(pq)

            if cur_dist > max_dist[node]: continue
            ans += 1

            for nei in graph[node]:
                c_move_cnt = min(graph[node][nei], M - cur_dist)
                used[node, nei] = c_move_cnt

                t_dist_to_nei = cur_dist + graph[node][nei] + 1

                if t_dist_to_nei < max_dist.get(nei, M + 1):
                    heapq.heappush(pq, (t_dist_to_nei, nei))
                    max_dist[nei] = t_dist_to_nei

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
        return ans

edges = [[0,1,5],[0,3,5],[1,2,5], [3,2,1],[0,2,2]]
M = 6
N = 4

obj = Solution()
print(obj.reachableNodes(edges, M, N))
'''