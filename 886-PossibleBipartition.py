# 886. Possible Bipartition

# O(N+E)
# O(N+E)

import collections
from typing import List
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        # graph =
        # {1:[2,3],
        # 2:[1,4],
        # 3:[1],
        # 4:[2]}

        # for 1-N:
        # colorDict = {1:0,
        #              2:1, 3:1,
        #              4:0, }

        def helper(node, color):
            if node in colorDict:
                return colorDict[node] == color

            colorDict[node] = color
            for nei in graph[node]:
                if not helper(nei, color ^ 1):
                    return False
            return True

        graph = collections.defaultdict(list)
        for n1, n2 in dislikes:
            graph[n1].append(n2)
            graph[n2].append(n1)

        colorDict = {}
        for node in range(1, N + 1):
            if node not in colorDict:
                if not helper(node, 0):
                    return False
        return True

    def possibleBipartition3(self, N: int, dislikes: List[List[int]]) -> bool:
        def helper(node, color=0):
            # print(f"node={node}, color={color}, colorDict={colorDict}")
            if node in colorDict:
                # print(f"return - {colorDict[node] == color}, {colorDict[node]}, {color}" )
                return colorDict[node] == color
            colorDict[node] = color
            for nei in graph[node]:
                # print(f"  for - node={node}, nei={nei}")
                rtn = helper(nei, color ^ 1)
                # print(f"rtn={rtn}, node={node}, nei={nei}, ")
                if not rtn:
                    # print(f"  false - node={node}, nei={nei}")
                    return False
            return True

        if not dislikes: return True
        graph = collections.defaultdict(list)
        for d in dislikes:
            graph[d[0]].append(d[1])
            graph[d[1]].append(d[0])

        # print(graph)
        colorDict = {}
        for n in range(1, N + 1):
            # print(f"start n={n}")
            if n not in colorDict:
                if not helper(n, 0):
                    return False
        return True

# {1:[2,3]
# 2:[1,4]
# 3:[1]
# 4:[2]}
# node = 1, color = 0, colorDict = {1:0, 2:1, 4:0}
#   nei = 2, 3
#     node = 2, color = 1
#        nei = 1, 4
#          node = 1, color = 0
#          node = 4, color = 0
#             nei = 2, color = 1


N = 4
dislikes = [[1,2],[1,3],[2,4]]
obj = Solution()
print(obj.possibleBipartition(N, dislikes))