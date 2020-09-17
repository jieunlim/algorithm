# 934. Shortest Bridge

# 1.DSF to mark the first island + collect edge points of the first island
# 2.DSF to mark the second island + collect edge points of the second island
# 3.Calculate the min distance between every pair of the points between the two islands.


# https://leetcode.com/problems/shortest-bridge/discuss/189440/Python-concise-DFS-and-BFS-in-1-solution
# Idea is straightforward.
# We get root of first island from "first" function
# We dfs root and add indexes to bfs
# We bfs and expand the first island in other words
# Finally return step number when facing other island
# Note: This can also be done with referenced array if you don't want to modify A.

class Solution:
    def shortestBridge(self, A):
        n = len(A)
        # get one point from any island
        def getFirst():
            for i, row in enumerate(A):
                for j, point in enumerate(row):
                    if point == 1:
                        return (i, j)

        islandA = []
        boundaries = []
        # DFS first to find the boundary of first island
        stack = [getFirst()]
        print(f"stack={stack}")

        while len(stack) > 0:
            i, j = stack.pop()
            print(f"i={i}, j={j}, stack={stack}")
            # label it
            A[i][j] = -1
            # islandA.append((i, j))
            # isBound = False
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 0:
                        boundaries.append((i, j))
                        # boundaries.append((x, y))
                    elif A[x][y] == 1:
                        stack.append((x, y))

        print(f"boundaries={boundaries}, stack={stack}")
        # all the points on island A is stored in islandA now
        # BFS to expend it
        step = 0
        print(f"step={step}, boundaries={boundaries}, A={A}")
        while boundaries:
            new = []
            for i, j in boundaries:
                print(f"i={i}, j={j}")
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    print(f"  x={x}, y={y}")
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
                        print(f"  A={A}, new={new}")
            step += 1
            boundaries = new
            print(f"step={step}, boundaries={boundaries}, A={A}")

    def shortestBridge2(self, A):
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                print(f"x={x}, y={y}")
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)

        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        print(f"i={i}, j={j}")
                        return i, j

        n, step, bfs = len(A), 0, []
        dfs(*first())
        print(f"bfs={bfs}")
        while bfs:
            new = []
            for i, j in bfs:
                print(f"i={i}, j={j}, new={new}")
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    print(f" x={x}, y={y}")
                    if 0 <= x < n and 0 <= y < n:
                        print(f"  A[x][y]={A[x][y]}")
                        if A[x][y] == 1:
                            print(f"    step={step}")
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
                            print(f"    new={new}")
            step += 1
            bfs = new
            print(f"*step={step}, bfs={bfs}")

A = [[0, 1, 0],
     [0, 0, 0],
     [0, 0, 1]]
# A=[[0,0],[0,0]]
obj = Solution()
print(obj.shortestBridge2(A))

