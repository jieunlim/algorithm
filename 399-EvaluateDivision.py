# 399. Evaluate Division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def helper(start, end, value):
            r = -1.0
            if visited[start] == 1:
                return r

            if start == end: return value

            visited[start] = 1
            for j, v in graph[start]:
                r = helper(j, end, v * value)
                if r != -1.0: return r

            return r

        if not equations or not values or not queries: return []

        #         build graph from equation/values
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        res = [0 for i in range(len(queries))]
        #         check queries
        visited = defaultdict(int)
        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                res[i] = -1
            elif queries[i][0] == queries[i][1]:
                res[i] = 1
            else:
                visited = defaultdict(int)
                res[i] = helper(queries[i][0], queries[i][1], 1.0)

        return res


    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        from collections import deque
        def helper(start, end):

            dq = deque([(start, 1.0)])
            visited = set()
            while dq:
                node, val = dq.popleft()
                if node == end:
                    return val
                visited.add(node)
                for g, v in graph[node]:
                    if g not in visited: dq.append((g, v * val))

            return -1

        if not equations or not values or not queries: return []

        # build graph from equation/values
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        print(graph)
        res = [0 for i in range(len(queries))]
        # check queries
        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                res[i] = -1
            elif queries[i][0] == queries[i][1]:
                res[i] = 1
            else:
                res[i] = helper(queries[i][0], queries[i][1])

        return res

