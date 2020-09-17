# 785. Is Graph Bipartite?
#     Time    O(V+E)
#     Space   O(V+E)

# [[1,3], [0,2], [1,3], [0,2]]
# 0----1
# |    |
# |    |
# 3----2
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colorDict = {}
        for node in range(len(graph)):
            if node not in colorDict:  # 0,1,2,3
                stack = [node]
                colorDict[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in colorDict:
                            stack.append(nei)
                            colorDict[nei] = colorDict[node] ^ 1
                        elif colorDict[nei] == colorDict[node]:
                            return False
        return True

    def isBipartite(self, graph):
        def dfs(pos):
            print(f"pos={pos}, graph[pos]={graph[pos]}, color = {color}")
            for nei in graph[pos]:
                print(f" nei={nei}")
                if nei in color:
                    print(f" ncolor[nei]={color[nei]}, color[pos]={color[pos]}")
                    if color[nei] == color[pos]:
                        return False
                else:
                    color[nei] = 1 - color[pos]
                    print(f" else - color[nei]={color[nei]}")
                    if not dfs(nei):
                        return False
            return True

        color = {}
        for i in range(len(graph)):
            if i not in color:
                print(f"*i={i}")
                color[i] = 0
                if not dfs(i):
                    return False
        return True


graph = [[1,3], [0,2], [1,3], [0,2]]
obj = Solution()
print(obj.isBipartite(graph))