# 670. Maximum Swap

# https://youtu.be/pDyh9VOMWgI

#  l  r
#  ^  ^
# 72636 -> 76632
# left: first one smallest from left to right

class Solution(object):
    # O(N)
    # O(N)

    # Greedy
    def maximumSwap(self, num: int) -> int:

        # [2,7,3,6]
        numList = [int(s) for s in str(num)]

        numDict = {}
        for idx, n in enumerate(numList):
            numDict[n] = idx

        for idx, n in enumerate(numList):
            for d in range(9, n, -1):
                if d in numDict and numDict[d] > idx:
                    numList[idx], numList[numDict[d]] = numList[numDict[d]], numList[idx]
                    return int("".join([str(x) for x in numList]))
        return num


    def maximumSwap(self, num: int) -> int:

        num = [int(x) for x in str(num)]
        maxIdx = len(num) - 1
        x = y = 0
        for i in range(len(num)-1, -1, -1):
            if num[i] > num[maxIdx]:
                maxIdx = i
            elif num[i] < num[maxIdx]:
                x = i
                y = maxIdx
        num[x], num[y] = num[y], num[x]
        return int(''.join([str(x) for x in num]))

    # O(n^2)
    # Brute force
    def maximumSwap2(self, num):
        A = list(str(num))
        ans = A[:]
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                A[i], A[j] = A[j], A[i]
                if A > ans: ans = A[:]
                A[i], A[j] = A[j], A[i]

        return int("".join(ans))

num = 2736
# num = 9973
obj = Solution()
print(obj.maximumSwap(num))

#         A = list(str(num))

#         last = {int(x): i for i, x in enumerate(A)}
#         print(f"last={last}")
#         for i, x in enumerate(A):
#             for d in range(9, int(x), -1):
#                 print(f"i={i}, x={x}, d={d}, last.get(d, 0)={last.get(d, 0)}")
#                 if last.get(d, 0) > i:
#                     A[i], A[last[d]] = A[last[d]], A[i]
#                     print(f"A={A}")
#                     return int("".join(A))
#         return num

#         numList = list(str(num))
#         numDict = collections.defaultdict(int)
#         for i in range(len(numList)):
#             numDict[int(numList[i])] = i
#         print(numList, numDict)

#         for i, n in enumerate(numList):
#             for digit in range(9, int(n), -1):
#                 print(f"i={i},n={n}, {numDict.get(digit, 0)} ")
#                 if numDict.get(digit, 0) > i:
#                     numList[i], numList[numDict[digit]] = numList[numDict[digit]], numList[i]
#                     print(f"return, {numDict.get(digit, 0)} ")
#                     return int("".join(numList))
#         return num