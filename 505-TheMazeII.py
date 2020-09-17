
# 505. The Maze II

# https://leetcode.com/problems/the-maze-ii/discuss/150536/Python-simple-and-elegant-PriorityQueue-solution-beats-97
# time O(mn*lg(mn)) - m*n matrix, lg(mn) for heapifying, removing O(1)
# space O(mn) for queue size

# Priority Queue solution
import heapq
class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        print(f"m={m}, n={n}, q={q}, stopped={stopped}")
        while q:
            dist, x, y = heapq.heappop(q)
            print(f"dist={dist}, x={x}, y={y}")
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                print(f"i={i}, j={j}, newX={newX}, newY={newY}, d={d}")
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    print(f"  [while] newX={newX}, newY={newY}, d={d}")
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
                    print(f"  [if] stopped={stopped}, dist={dist}, d={d}")
            print(f" q={q}")
        return -1


    def shortestDistance_bfs(self, maze, start, destination):

        import collections

        print(f"maze={maze}, start={start}, destination={destination}")
        print(maze[start[1]], maze[destination[0]][destination[1]])

        if maze[start[0]][start[1]] or maze[destination[0]][destination[1]]:
            return -1

        queue = collections.deque([tuple(start + [-1])])  # Store distance to start as -1.
        print(f"queue={queue}")
        while queue:
            i, j, distance = queue.popleft()
            print(f"i={i}, j={j}, distance={distance}")

            for x, y in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                row, col, d = i, j, distance
                print(f"(x,y)={x,y}, row={row}, col={col}, d={d}")
                # Let the ball keep rolling in whatever direction it's going until it hits a stopping point.
                while 0 <= row + y < len(maze) and 0 <= col + x < len(maze[0]) and not maze[row + y][col + x] == 1:
                    row += y
                    col += x
                    d -= 1
                    print(f"  [while] row={row}, col={col}, d={d}")
                # We are at a stopping point for the ball. If the stopping point has never been added to the queue,
                # or if it represents a new shortest distance, update the cell value to -distance and add cell to the queue.
                if maze[row][col] == 0 or (maze[row][col] < 0 and abs(d) < abs(maze[row][col])):
                    maze[row][col] = d
                    if [row, col] != destination:
                        queue.append((row, col, d))
                    print(f"    [if] maze={maze}, queue={queue}")
        if maze[destination[0]][destination[1]] == 0:
            return -1
        return -maze[destination[0]][
            destination[1]] - 1  # Distance to start was stored as -1 so we need to subtract 1 before returning.

maze = [[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]]
start=[0,4]
destination=[4,4]
obj = Solution()
print(obj.shortestDistance(maze, start, destination))
# print(obj.shortestDistance_bfs(maze, start, destination))


