# 240. Search a 2D Matrix II

class Solution:
    # Approach 4: Search Space Reduction
    # start at the bottom-left of the matrix
    # O(n+m), O(1)
    def searchMatrix(self, matrix, target):

        if not matrix: return False

        row, col, width = len(matrix) - 1, 0, len(matrix[0])
        while row >= 0 and col < width:
            # print(f"row={row}, col={col}, matrix[row][col]={matrix[row][col]}")
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1
            else:
                col = col + 1
        return False

    # Approach 2: Binary Search
    # O(lg(n!))
    def searchMatrix2(self, matrix, target):
        def bSearch(start, vertical):
            lo = start
            hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

            while hi >= lo:
                mid = (lo + hi) // 2
                if vertical:  # searching a column
                    if matrix[start][mid] < target:
                        lo = mid + 1
                    elif matrix[start][mid] > target:
                        hi = mid - 1
                    else:
                        return True
                else:  # searching a row
                    if matrix[mid][start] < target:
                        lo = mid + 1
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                    else:
                        return True

            return False

        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vFound = bSearch(i, True)
            hFound = bSearch(i, False)

            if vFound or hFound:
                return True

        return False

    # Approach 3: Divide and Conquer
    # O(nlgn), O(lgn)
    def searchMatrix3(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 20, 22],
  [10, 13, 14, 22, 24],
  [18, 21, 23, 26, 30]
]
target = 5
# matrix=[]
# target=0
target = 20

obj = Solution()
print(obj.searchMatrix(matrix, target))