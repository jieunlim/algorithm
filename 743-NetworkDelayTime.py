# 743. Network Delay Time

# PQ O(VlogV+ElogV)
# BFS O(V*E)


from collections import deque, defaultdict

class Solution():
    # BFS
    def networkDelayTime(self, times, N, K):

        from collections import deque, defaultdict
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))

        print(f"graph={graph}")
        while queue:
            time, node = queue.popleft()
            print(f"time={time}, node={node}")
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1

    # Shortest Path Faster Algorithm
    # a generallization of BFS
    # an improvement of the Bellman–Ford algorithm which computes single source shortest paths
    # in a weighted directed graph negative edges
    # O(V*E), almost O(V+E) or O(E)
    def networkDelayTime_spfs(self, times, N, K):
        import collections
        time_arr, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])

        for u, v, w in times:
            graph[u].append((v, w))

        print(f"graph={graph}")
        print(f"q={q}, time_arr={time_arr}")
        while q:
            node_time, node = q.popleft()
            print(f"[pop] node_time={node_time}, node={node}, time_arr[node]={time_arr[node]}")

            if node_time < time_arr[node]:
                time_arr[node] = node_time
                for nei, nei_time in graph[node]:
                    print(f"  [for]nei={nei}, nei_time={nei_time}")
                    q.append((node_time + nei_time, nei))
                    print(f"  [for] q={q}")
                print(f"time_arr={time_arr}")
        mx = max(time_arr)
        print(f"mx={mx}")
        return mx if mx < float("inf") else -1


    # Dijkstra
    # Priority Queue, Heap
    # O(VlogV + ElgV)
    def networkDelayTime_dijkstra(self, times, N, K):
        import collections
        import heapq

        graph, visited, heap = collections.defaultdict(dict), set(), [(0, K)]
        for u, v, w in times:
            graph[u][v] = w

        print(f"graph={graph}, heap={heap}")
        while heap:
            time, node = heapq.heappop(heap)
            print(f"[heappop] time={time}, node={node}")

            if node in visited: continue
            visited, res = visited | {node}, time  # Set union opertator '|', visited.union({u})
            print(f"   visited={visited}, res={res}")

            for neigh in graph[node]:
                print(f"    [for] neigh={neigh}")
                if neigh not in visited: heapq.heappush(heap, (time + graph[node][neigh], neigh))
                print(f"        heap={heap}")
        return res if len(visited) == N else -1


    # Bellman-Ford
    def networkDelayTime_bellman(self, times, N, K):
        dp = [0] + [float('inf')] * N
        dp[K] = 0

        print(f"dp={dp}")
        for _ in range(N):
            for u, v, w in times:
                print(f"u={u}, v={v}, w={w}")
                if dp[u] != float('inf') and dp[u] + w < dp[v]:
                    dp[v] = dp[u] + w
                    print(f"    dp={dp}")

        res = max(dp or [0])
        print(f"dp={dp}, res={res}")
        return -1 if res == float('inf') else res

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

times = [[2,1,10],[2,3,50],[3,4,10],[1,5,20], [1,3,20]]
N = 5
K = 2

# times = [[2, 1, 50], [2, 3, 100], [1, 3, 6], [1, 4, 3], [1, 5, 70], [3, 5, 5], [4, 5, 1]]
# # ,[4,1,10],[4,3,1]]
# N = 5
# K = 2

# times=[[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2



#
# times = [
#         ("A", "B", 70),
#         ("A", "C", 20),
#         ("A", "D", 50),
#         ("B", "C", 10),
#         ("B", "D", 90),
#         ("C", "D", 5),
#     ("C","A",1),
#     ("D","C",2)]
# N=4
# K = "A"
#
# times = [
#         (1, 2, 70),
#         (1, 3, 20),
#         (1, 4, 50),
#         (2, 3, 10),
#         (2, 4, 90),
#         (3, 4, 5),
#     (3, 1, 1),
#     (4, 3, 2)]
# N=4
# K = 1

obj = Solution()

print(obj.networkDelayTime_spfs(times, N, K))
# print(obj.networkDelayTime_dijkstra(times, N, K))
# print(obj.networkDelayTime_bellman(times, N, K))