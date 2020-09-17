# 207. Course Schedule

# finding cycle in a DAG(Directed Acyclic Graph), Topological sort
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.

# https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation

class Solution:
    def canFinish(self, numCourses, prerequisites):
        import collections
        def dfs(i):
            if visited[i] == -1:
                return False

            if visited[i] == 1:
                return True

            visited[i] = -1
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            visited[i] = 1
            return True

        graph = [[] for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        print(f"graph={graph}")
        visited = collections.defaultdict(int)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

numCourses = 2
prerequisites = [[0, 1], [1, 0]]
numCourses = 3
prerequisites = [[0, 1],[1,2]]
obj = Solution()
print(obj.canFinish(numCourses, prerequisites))


class Solution3(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        print(f"numCourses={numCourses}, prerequisites={prerequisites}")
        print(f"graph={graph}, visited={visited}")
        # create graph
        for pair in prerequisites:
            print(f"pair={pair}")
            x, y = pair
            graph[x].append(y)
            print(f"x={x}, y={y}")
        print(f"graph={graph}")

        # visit each node
        for i in range(numCourses):
            print(f"<i={i}>")
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        print(f"[dfs] graph={graph}, visited={visited}, i={i}")
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            print(f"visited[i]={visited[i]} return false")
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            print(f"visited[i]={visited[i]} return true")
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            print(f"j={j}, graph[i]={graph[i]}")
            if not self.dfs(graph, visited, j):
                print(f" return False")
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True

    def canFinish2(self, N, edges):
        pre = defaultdict(list)
        for x, y in edges: pre[x].append(y)

        status = [0] * N

        def canTake(i):
            if status[i] in {1, -1}: return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in pre[i]): return False
            status[i] = 1
            return True

        return all(canTake(i) for i in range(N))


'''

# approach 1 - Backtracking
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict
        print(f"numCourses={numCourses}, prerequisites={prerequisites}")
        courseDict = defaultdict(list)

        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse)
            print(f"nextCourse={nextCourse}, prevCourse={prevCourse}, courseDict={courseDict}")

        path = [False] * numCourses
        print(f"path={path}")
        for currCourse in range(numCourses):
            print(f"currCourse={currCourse}, path={path}, call isCyclic")
            if self.isCyclic(currCourse, courseDict, path):
                return False
        return True


    def isCyclic(self, currCourse, courseDict, path):

        print(f"[isCyclic] currCourse={currCourse}, courseDict={courseDict}, path={path}, path[currCourse]={path[currCourse]}")
        if path[currCourse]:
            # come across a previously visited node, i.e. detect the cycle
            return True

        # before backtracking, mark the node in the path
        path[currCourse] = True
        print(f"path[currCourse]={path[currCourse]}, path={path}")
        # backtracking
        ret = False
        for child in courseDict[currCourse]:
            print(f"child={child}")
            ret = self.isCyclic(child, courseDict, path)
            print(f"ret={ret}, child={child}, currCourse={currCourse}")
            if ret: break

        # after backtracking, remove the node from the path
        path[currCourse] = False
        print(f"path={path}, ret={ret}")
        return ret

# Topological sort
class GNode(object):
    """  data structure represent a vertex in the graph."""
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []

class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        print(f"numCourses={numCourses}, prerequisites={prerequisites}, graph={graph}")
        totalDeps = 0
        for relation in prerequisites:
            print(f"relation={relation}")
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1
            print(f"nextCourse={nextCourse}, prevCourse={prevCourse}, graph={graph}, totalDeps={totalDeps}")

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            print(f"index={index}, node={node}")
            if node.inDegrees == 0:
                nodepCourses.append(index)
                print(f"nodepCourses={nodepCourses}")

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False

'''