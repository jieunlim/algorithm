
# 51. N-Queens
# Given an integer n,
# return all distinct solutions to the n-queens puzzle.
# https://leetcode.com/problems/n-queens/

# n*n chessboard
# input - 4
# output:
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# 52. N-Queens II
# return the number of distinct solutions
# https://leetcode.com/problems/n-queens-ii/
# input : 4, output : 2
# n*n 체스보드에서 n개의 퀸을 놓을 수 있는 경우를 찾는 문제
# 퀸은 가로, 세로, 대각선 공격이 가능함.
# 0번째 row에서, 첫번째 퀸을 (0,0)에 놓으면, 0번째 row, column, 대각선 방향은 다른 퀸이 자리할 수 없음.
# 이것을 트리로 그리면 이에 따라, 제약조건에 따라 저절로 prunning이 됨.
# 0번째 row에서 퀸을 (0,0)에 놓고,
# 1번째 row에 놓을 자리를 찾아보면 (1,0)은 column에서 걸림, (1,1)은 대각선에서 걸림, (1,2)와 (1,3)이 가능. 우선 (1,2)에 놓기로 하고,
# 2번째 row로 가면 놓을 수 있는 자리가 없음. 왔던 길 다시 돌아가기.
# 놓았던 1번째 row인 (1,2)를 지우고, (1,3)으로 놓아보고, 다음 2번째 row에 가능한 자리를 찾아봄.
# 이런식으로, prunning & 되돌아가면서 지우고 다시 놓아보는 backtracking을 하는 전형적인 문제임.
# <code description>
# prunning 조건 체크시 (x, y)라고 했을때,
# 같은 row는 x, column은 y로 쉽게 찾을 수 있음.
# 대각선의 경우는,
# 45도 대각선(왼쪽)은 x-y 값이 같고 (즉 (0,0)의 대각선은 (1,1), (2,2)와 같이 x-y값이 모두 0으로 동일)
# 135도 대각선(오른쪽)은 x+y 값이 같음.(즉 (0,3)의 대각선은 (1,2), (2,1), (3,0)과 같이 x+y값이 모두 3으로 동일)
#
# x 값은 queens 매개 변수에 들어가는 y 값의 갯수로 체크하기로 하고 (x=len(queens))
# 첫번째 퀸즈를 (0,0)에 놓았을때 n개 즉 4개의 퀸을 다 놓을 수 없다는 것을 알았으므로,
# 다시 첫번째 퀸즈를 (0,1)에 놓기로 함.
# 이번에 놓은 퀸즈의 위치(0,1) queens=[1],xyDiff=[-1], xySum=[1] 상태는로 recursion함수 호출.
# 다음 row로 가서 x=1이 되고 y는 0번째부터 확인해보면, 1+0=1 이므로 xySum 즉 135도 대각선으로 걸려서 놓을 수 없음.
#                       y 1번째는 queens에 있으므로(같은 row이므로) 안됨
#                       y 2번째는 xyDiff 즉 45도 대각선으로 걸리므로 안됨
#                       y 3번째는 조건에 걸리지 않으므로 놓을 수 있음, 두번째 퀸은 (1,3) 위치에 놓음.
# 결과값인 res에는 [[1, 3, 0, 2], [2, 0, 3, 1]] 과 같이 저장이 되고,
# [1,3,0,2]는 (0,1), (1,3), (2, 0), (3,2)에 퀸이 놓이게 된다는 의미.

class Solution:
    # 51. N-Queens
    # time O(n!), N*(N-2)*(N-4)*...
    # space O(n)
    def solveNQueens(self, n):
        def nQueens(queens, xyDif, xySum):

            x = len(queens)
            # print(f"x={x}, queens={queens}, xyDif={xyDif}, xySum={xySum}")
            if x == n:
                res.append(queens)
                return None

            for y in range(n):
                if y not in queens \
                    and x - y not in xyDif \
                        and x + y not in xySum:
                    nQueens(queens + [y], xyDif + [x-y], xySum + [x+y])
        res = []
        nQueens([], [], [])
        # print(f"res={res}")
        return [["." * i + "Q" + "." * (n - i - 1) for i in qn] for qn in res]

    # 52. N-Queens II
    def totalNQueens(self, n):
        def nQueens(queens, xyDif, xySum):
            x = len(queens)
            if x == n:
                return 1

            cnt = 0
            for y in range(n):
                if y not in queens \
                    and x - y not in xyDif \
                        and x + y not in xySum:
                    cnt += nQueens(queens + [y], xyDif + [x-y], xySum + [x+y])

            return cnt

        cnt = nQueens([], [], [])
        # print(f"cnt = {cnt}")
        return cnt
n = 4
obj = Solution()
print(obj.solveNQueens(n))
# print(obj.totalNQueens(n))

# (51. N-Queens) reference
# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms



print()
print()
# [["." * i + "Q" + "." * (n - i - 1) for i in qn] for qn in res]
n=4
r=[[1, 3, 0, 2], [2, 0, 3, 1]]
tmp=[]
r2=[]
for qn in r:
    for i in qn:
        tmp.append("."*i + "Q" + "."*(n-i-1))
    print(f"tmp={tmp}")
    r2.append(tmp)
    tmp=[]
print(f"r2={r2}")


