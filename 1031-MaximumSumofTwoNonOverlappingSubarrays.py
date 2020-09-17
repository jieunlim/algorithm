# 1031. Maximum Sum of Two Non-Overlapping Subarrays

# O(N)
# O(1)

# 689. Maximum Sum of 3 Non-Overlapping Subarrays
def maxSumTwoNoOverlap(A, L, M):

    def helper(L, M):

        maxLeft, maxSum = 0, 0
        for i in range(len(A)-L-M+1):
            maxLeft = max(maxLeft, sum(A[i:L+i]))
            rightSum = sum(A[L+i:L+M+i])
            maxSum = max(maxSum, maxLeft + rightSum)

        return maxSum

    if len(A) < L+M:
        return

    return max(helper(L, M), helper(M, L))

A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
L = 1
M = 2

A=[2,1,5,6,0,9,5,0,3,8]
L=4
M=3
print(maxSumTwoNoOverlap(A, L, M))

# 0, 11 - 11
# 6, 7 - 13
# 6, 4
# 6, 7
# 6, 6
# 6, 10 - 16
# 6, 13 - 19
#
# 6, 5 - 11
# 11, 2 - 13
# 11, 5 - 16
# 11, 1
# 11, 9 - 20
# 11, 4 - 15


def maxSumTwoNoOverlap2(  A, L, M):
    for i in range(1, len(A)):
        A[i] += A[i - 1]
    print(f"A={A}")
    res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
    for i in range(L + M, len(A)):
        Lmax = max(Lmax, A[i - M] - A[i - L - M])
        Mmax = max(Mmax, A[i - L] - A[i - L - M])
        res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
    return res

from typing import List
def maxSumTwoNoOverlap(A: List[int], L: int, M: int) -> int:

    def maxSum(L: int, M: int) -> int:
        sumL = sumM = 0
        for i in range(0, L + M):
            if i < L:
                sumL += A[i]
            else:
                sumM += A[i]

        print(f"sumL={sumL}, sumM={sumM}")
        maxL, ans = sumL, sumL + sumM
        for i in range(L + M, len(A)):
            sumL += A[i - M] - A[i - L - M]
            maxL = max(maxL, sumL)
            sumM += A[i] - A[i - M]
            print(f"maxL={maxL}, sumM={sumM}")
            ans = max(ans, maxL + sumM)
        return ans

    return max(maxSum(L, M), maxSum(M, L))

A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2

A = [1,5,6,0,9,3]
L = 1
M = 3
print(maxSumTwoNoOverlap(A, L, M))

def maxSumTwoNoOverlap(A: List[int], L: int, M: int) -> int:
    lenA = len(A)
    maxLeftL = [0 for _ in range(lenA)]
    maxLeftM = [0 for _ in range(lenA)]
    maxRightL = [0 for _ in range(lenA)]
    maxRightM = [0 for _ in range(lenA)]

    curL, curM, mL, mM = 0, 0, 0, 0
    for i in range(lenA):
        curL += A[i]
        curM += A[i]
        if i >= L: curL -= A[i-L]
        if i >= M: curM -= A[i-M]
        if i >= L-1 and mL < curL: mL = curL
        if i >= M-1 and mM < curM: mM = curM
        maxLeftL[i] = mL
        maxLeftM[i] = mM

    curL, curM, mL, mM = 0, 0, 0, 0
    for i in range(lenA):
        curL += A[lenA - 1 - i]
        curM += A[lenA - 1 - i]
        if i >= L: curL -= A[lenA - 1 - i + L]
        if i >= M: curM -= A[lenA - 1 - i + M]
        if i >= L - 1 and mL < curL: mL = curL
        if i >= M - 1 and mM < curM: mM = curM
        maxRightL[lenA - 1 - i] = mL
        maxRightM[lenA - 1 - i] = mM

    result = 0
    for i in range(lenA-1):
        result = max(result, maxLeftL[i] + maxRightM[i+1])
        result = max(result, maxLeftM[i] + maxRightL[i+1])

    return result

# 689. Maximum Sum of 3 Non-Overlapping Subarrays