
# 278. First Bad Version
# binary search
# n = 5
# 1 2 3 4 5
#     T    right = mid
#     F    left = mid + 1
#  O(logN), O(1)

def firstBadVersion( n):
    """
    :type n: int
    :rtype: int
    """
    start, end = 0, n
    while start < end:
        mid = start + (end - start) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1

    return start
    # 1,2,3,4
    # F F T T


def firstBadVersion(n):

    left, right = 1, n

    while left < right:
        mid = left + (right-left)//2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return right
