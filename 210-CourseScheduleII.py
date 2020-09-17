# 210. Course Schedule II

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        from collections import defaultdict
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            res.append(i)
            return True

        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        res = []
        visited = defaultdict(int)
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

    # online interview 4/22/2020
    def findOrder4(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict = defaultdict(int)
        res = []
        for i in range(len(prerequisites)):
            dict[prerequisites[i][0]] += 1

        print(dict)
        flag = True
        while flag:
            flag = False
            for i in range(numCourses):
                if dict[i] == 0 and i not in res:
                    res.append(i)
                    flag = True
                    for j in range(len(prerequisites)):
                        if prerequisites[j][1] == i:
                            dict[prerequisites[j][0]] -= 1
        return res if len(res) == numCourses else []

    # https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-dfs-bfs-solutions-with-comments.
    # BFS
    def findOrder1(self, numCourses, prerequisites):
        import collections
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        print(f"dic={dic}, neigh={neigh}")
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            print(f"res={res}, node={node}")
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []

    # DFS
    def findOrder2(self, numCourses, prerequisites):
        import collections
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        print(f"dic={dic}, neigh={neigh}")
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []

prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 4
obj = Solution()
print(obj.findOrder(numCourses, prerequisites))