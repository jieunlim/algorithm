class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(i):
            for nei in rooms[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        visited = set()
        visited.add(0)
        dfs(0)

        if len(visited) == len(rooms):
            return True
        else:
            return False

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:

        # BFS
        visited = set([0])
        dq = deque([0])

        while dq:
            room = dq.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dq.append(key)

        if len(visited) == len(rooms):
            return True
        else:
            return False
