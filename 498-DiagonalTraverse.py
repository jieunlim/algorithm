
# 498. Diagonal Traverse
def findDiagonalOrder(matrix):
    if not matrix: return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    x, y = 0, 0
    for i in range(rows+cols):
        if i%2 == 0:
            # if i < rows: x = i
            # else: x = rows - 1
            x = min(i, rows-1)
            y = i - x
            while x>=0 and y < cols:
                result.append(matrix[x][y])
                x -= 1
                y += 1
        else:
            y = min(i, cols-1)
            x = i - y
            while y>=0 and x < rows:
                result.append(matrix[x][y])
                x += 1
                y -= 1
    return result

matrix=[[1,2], [3,4]]
print(findDiagonalOrder(matrix))
# m+n-1

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
#  i is the diagonal direction order
#  x+y = i
