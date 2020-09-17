# 1192. Critical Connections in a Network

class Solution:
    def criticalConnections(self, n, connections):

        def helper(rank, cur, prev):
            # print(f"rank={rank}, cur={cur}, prev={prev}")
            rankArr[cur] = rank
            for nei in graph[cur]:
                if nei == prev: continue
                if rankArr[nei] == 0:
                    helper(rank +1, nei, cur)

                rankArr[cur] = min(rankArr[cur], rankArr[nei])
                # print(f"rankArr={rankArr}, cur={cur}, nei={nei}")
                if rankArr[nei] > rank:
                    result.append([cur, nei])

        if n < 1 or not connections: return []
        result, rankArr = [], [0 for i in range(n)]

        graph = [[] for _ in range(n)]
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        # print(graph)
        helper(1, 0, -1)
        return result

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
n = 6
connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]

obj = Solution()
print(obj.criticalConnections(n, connections))

class Solution2:
    def criticalConnections(self, n: int, connections) :
        graph = [[] for _ in range(n)]  ## vertex i ==> [its neighbors]

        currentRank = 0  ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level
        lowestRank = [i for i in range(n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i
        visited = [False for _ in range(n)]  ## common DFS/BFS method to mark whether this node is seen before

        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        res = []
        prevVertex = -1  ## This -1 a dummy. Does not really matter in the beginning.
        ## It will be used in the following DFS because we need to know where the current DFS level comes from.
        ## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.

        print(f"graph={graph}")

        currentVertex = 0  ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res

    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        print(f"[DFS] res={res}, lowestRank={lowestRank}, visited={visited}")
        print(f"      currentRank = {currentRank}, prevVertex={prevVertex}, currentVertex={currentVertex}")
        visited[currentVertex] = True
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            print(f"  nextVertex={nextVertex}")
            if nextVertex == prevVertex:
                print(f"    continue")
                continue  ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
            # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
            # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            print(f" currentVertex={currentVertex}, nextVertex={nextVertex}, lowestRank={lowestRank}")
            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            print(f"  lowestRank[currentVertex] = {lowestRank[currentVertex]}, ")
            # take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1:  ####### if all the neighbors lowest rank is higher than mine + 1,
                # then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
n=6
connections=[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]

obj = Solution2()
# print(obj.criticalConnections(n, connections))


import collections
class Solution3:
    # Cycle 아닌 것 찾기!
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me

    def criticalConnections(self, n, connections):
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            print(f"dfs rank={rank}, curr={curr}, prev={prev}, low={low}, result={result}")
            for neighbor in edges[curr]:
                print(f" for  neighbor={neighbor}, prev={prev}")
                if neighbor == prev:
                    print(f"  neighbor == prev, continue")
                    continue
                if not low[neighbor]:
                    print(f" [not low] low[neighbor]={low[neighbor]}, curr={curr}")
                    result += dfs(rank + 1, neighbor, curr)
                    print(f" result={result}")
                low[curr] = min(low[curr], low[neighbor])
                print(f" low={low}, rank={rank}, curr={curr}, neighbor={neighbor}")
                if low[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
                    print(f" result={result}")
            print(f"result={result},curr={curr}, prev={prev}")
            return result

        low, edges = [0] * n, collections.defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        print(f"edges={edges}")

        return dfs(1, 0, -1)

    # https: // leetcode.com / problems / critical - connections - in -a - network / discuss / 465923 / Simple - Intuitive - Explanation - Beats - 99 - in -theory -as-well -as-compute - PYTHON
    def criticalConnections2(self, n, connections):

        graph = [[] for _ in range(n)]  ## vertex i ==> [its neighbors]

        currentRank = 0  ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level

        lowestRank = [i for i in
                      range(n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i

        visited = [False for _ in range(n)]  ## common DFS/BFS method to mark whether this node is seen before

        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        res = []
        prevVertex = -1  ## This -1 a dummy. Does not really matter in the beginning.
        ## It will be used in the following DFS because we need to know where the current DFS level comes from.
        ## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.

        currentVertex = 0  ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res


    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
        visited[currentVertex] = True
        lowestRank[currentVertex] = currentRank

        print(f"_DFS res={res}, graph={graph}, lowestRank={lowestRank}")
        print(f" visited={visited}, currentRank={currentRank}, prevVertex={prevVertex}, currentVertex={currentVertex}")

        print(f"graph[currentVertex]={graph[currentVertex]}")
        for nextVertex in graph[currentVertex]:
            print(f" nextVertex={nextVertex}, prevVertex={prevVertex}")
            if nextVertex == prevVertex:
                continue  ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                print(f" visited[nextVertex]={visited[nextVertex]}, visited={visited}")
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
            # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
            # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            print(f" lowestRank={lowestRank}")
            # take the min of the current vertex's and next vertex's ranking
            if lowestRank[nextVertex] >= currentRank + 1:  ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])
                print(f" res={res}")


n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
obj = Solution()
# print(obj.criticalConnections(n, connections))