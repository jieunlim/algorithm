"""
Demolition Robot
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.
Sample Input :
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]]
Sample Output :
3

"""













def demolition(matrix):
    """
    bfs
    
    """
    m, n = len(matrix), len(matrix[0])
    if m < 1 or n < 1: return -1
    
    
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = collections.deque([(0, 0)])
    visited = set([(0, 0)])
    dist = -1
    while q:
        
        dist += 1
        size = len(q)
        
        for _ in range(size):
            
            i, j = q.popleft()
            
            if matrix[i][j] == 9:
                return dist
            
            for di, dj in neighbors:
                ni, nj = i+di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj))
                    
    return -1

matrix = [
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]
]

print(demolition(matrix))
