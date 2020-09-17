# 311. Sparse Matrix Multiplication

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        #         A
        #         2,3,3
        #         (0,0):1
        #         1,0,-1
        #         1,2,3

        #         B
        #         3,3,2
        #         0,0,7
        #         2,2,1

        res = [[0 for i in range(len(B[0]))] for _ in range(len(A))]
        matrixADict, matrixBDict = {}, {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    matrixADict[(i, j)] = A[i][j]
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    matrixBDict[(i, j)] = B[i][j]

        print(matrixADict, matrixBDict)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    a = matrixADict[(i, k)] if (i, k) in matrixADict else 0
                    b = matrixBDict[(k, j)] if (k, j) in matrixBDict else 0
                    res[i][j] += a * b
        return res



class Solution:
    def multiply(self, A, B):

        # [0,0,0]  [1,2]  A.rows * B.cols / A.cols == B.rows
        # [1,1,3]  [3,0]
        #          [3,0]

        rowsA = len(A)
        colsA = len(A[0])
        colsB = len(B[0])

        res = [[0 for _ in range(colsB)] for _ in range(rowsA)]

        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    res[i][j] += A[i][k] * B[k][j]

        return res

class SparseMatrix(object):
    def __init__(self, nrow, ncol, S):
        self.nrow = nrow
        self.ncol = ncol
        self.S = S

    @staticmethod
    def to_sparse(M):
        S = dict()
        for r, row in enumerate(M):
            for c, value in enumerate(row):
                if value: S[(r, c)] = value
        return S

    @classmethod
    def from_dense(cls, M):
        nrow, ncol = len(M), len(M[0])
        S = cls.to_sparse(M)
        return cls(nrow, ncol, S)

    @classmethod
    def from_sparse(cls, nrow, ncol, S):
        return cls(nrow, ncol, S)

    def __matmul__(self, B):
        C = dict()
        for (a_r, a_c), a_val in self.S.items():
            for b_c in range(B.ncol):
                if (a_c, b_c) in B.S:
                    b_val = B.S[(a_c, b_c)]
                    C[(a_r, b_c)] = C.get((a_r, b_c), 0) + a_val * b_val
        return self.from_sparse(self.nrow, B.ncol, C)

    def to_dense(self):
        M = [[0] * self.ncol for _ in range(self.nrow)]
        for (r, c), value in self.S.items():
            M[r][c] = value
        return M


class Solution:
    def multiply(self, A, B):
        A = SparseMatrix.from_dense(A)  # O(n^2)
        B = SparseMatrix.from_dense(B)  # O(n^2)
        C = A @ B  # O(K) with K be the ~ non elements in C
        return C.to_dense()
A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

obj = Solution2()
print(obj.multiply(A, B))


# https://leetcode.com/problems/sparse-matrix-multiplication/discuss/419538/What-the-interviewer-is-expecting-when-this-problem-is-asked-in-an-interview...
# O(mnl) with the definition m, n, l = len(A), len(A[0]), len(B[0]).

# sparse matrix
# dense matrix

class Solution(object):
    # without table
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB: C[i][j] += eleA * eleB

        return C

    # with table
    def multiply2(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n = len(A), len(A[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        l = len(B[0])
        table_A, table_B = {}, {}
        for i, row in enumerate(A):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_A: table_A[i] = {}
                    table_A[i][j] = ele
        for i, row in enumerate(B):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_B: table_B[i] = {}
                    table_B[i][j] = ele
        C = [[0 for j in range(l)] for i in range(m)]
        for i in table_A:
            for k in table_A[i]:
                if k not in table_B: continue
                for j in table_B[k]:
                    C[i][j] += table_A[i][k] * table_B[k][j]
        return C


A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

obj = Solution()
print(obj.multiply(A, B))

