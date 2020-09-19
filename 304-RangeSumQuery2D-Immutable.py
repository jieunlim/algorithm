# 304. Range Sum Query 2D - Immutable

class NumMatrix:
    def __init__(self, matrix):

        if not matrix: return
        self.matrix = matrix
        self.matrixSum = [[ 0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
        self.initMatrix()

    def initMatrix(self):
        rows = len(self.matrixSum)
        cols = len(self.matrixSum[0])
        for i in range(rows):
            for j in range(cols):
                a = self.matrixSum[i-1][j] if i > 0 else 0
                b = self.matrixSum[i][j-1] if j > 0 else 0
                c = self.matrixSum[i-1][j-1] if i > 0 and j > 0 else 0
                self.matrixSum[i][j] = a + b - c + self.matrix[i][j]
        # print(self.matrixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        a = self.matrixSum[row1 - 1][col2] if row1 > 0 else 0
        b = self.matrixSum[row2][col1 - 1] if col1 > 0 else 0
        c = self.matrixSum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.matrixSum[row2][col2] - a - b + c

# matrix [[]]
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))



