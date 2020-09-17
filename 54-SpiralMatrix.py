# 54. Spiral Matrix

class Solution:
    # https://leetcode.com/problems/spiral-matrix/discuss/20821/An-iterative-Python-solution

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix and matrix[0]:
            if matrix[0]:
                result += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix and matrix[-1]:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result

    def spiralOrder(self, matrix):
        result = []

        while matrix and matrix[0]:
            print(f"matrix[0]={matrix[0]}")

            if matrix[0]:
                print(f"1 matrix[0]={matrix[0]}")
                result += matrix.pop(0)
            print(f"result={result}, matrix={matrix}")

            if matrix and matrix[0]:
                print(f"2 matrix[0]={matrix[0]}")
                for row in matrix:
                    print(f"  row={row}")
                    result.append(row.pop())
            print(f"result={result}, matrix={matrix}")

            if matrix and matrix[-1]:
                print(f"3 matrix[-1]={matrix[-1]}")
                result += matrix.pop()[::-1]
            print(f"result={result}, matrix={matrix}")

            if matrix and matrix[0]:
                print(f"4 matrix[0]={matrix[0]}")
                for row in matrix[::-1]:
                    print(f"row={row}, matrix[::-1]={matrix[::-1]}")
                    result.append(row.pop(0))
            print(f"result={result}, matrix={matrix}")

        return result

    def spiralOrder2(self, matrix):
        nrow = len(matrix)
        if nrow == 0: return []
        ncol = len(matrix[0])
        if ncol == 0: return []

        r_start, r_end = 0, nrow - 1
        c_start, c_end = 0, ncol - 1
        output = []
        # dir_idx = 0 # right

        print(f"r_start={r_start}, r_end={r_end}, c_start={c_start}, c_end={c_end}")
        while (r_start <= r_end) and (c_start <= c_end):

            output = output + matrix[r_start][c_start:c_end + 1]
            r_start += 1

            print(f"output={output}, r_start={r_start}")
            if (r_start > r_end): break

            for r in range(r_start, r_end + 1):
                output.append(matrix[r][c_end])
                print(f"r={r}, output={output}")
            c_end -= 1

            print(f"c_end={c_end}")
            if (c_start > c_end): break

            output = output + [x for x in reversed(matrix[r_end][c_start:c_end + 1])]
            r_end -= 1

            print(f"r_end={r_end}, output={output}")
            if (r_start > r_end): break

            for r in range(r_end, r_start - 1, -1):
                output.append(matrix[r][c_start])
                print(f"r={r}, output={output}")
            c_start += 1

        print(f"c_start={c_start}, output={output}")
        return output

    def spiralOrder3(self, matrix):
        nrow = len(matrix)
        if nrow == 0: return []
        ncol = len(matrix[0])
        if ncol == 0: return []

        r_start, r_end = 0, nrow - 1
        c_start, c_end = 0, ncol - 1
        output = []
        dir_idx = 0  # right

        while len(output) < (ncol * nrow):
            if dir_idx == 0:  # Right
                output = output + matrix[r_start][c_start:c_end + 1]
                r_start += 1
                dir_idx = 1  # Down
            elif dir_idx == 1:  # Down
                for r in range(r_start, r_end + 1):
                    output.append(matrix[r][c_end])
                c_end -= 1
                dir_idx = 2  # Left
            elif dir_idx == 2:  # Left
                output = output + [x for x in reversed(matrix[r_end][c_start:c_end + 1])]
                r_end -= 1
                dir_idx = 3  # Up
            else:  # Up
                for r in range(r_end, r_start - 1, -1):
                    output.append(matrix[r][c_start])
                c_start += 1
                dir_idx = 0  # Right

        return output


# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
obj = Solution()
print(obj.spiralOrder(matrix))