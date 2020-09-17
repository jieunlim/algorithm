# 689. Maximum Sum of 3 Non-Overlapping Subarrays
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        s1, s2, s3 = sum(nums[:k]), sum(nums[k:2 * k]), sum(nums[2 * k:3 * k])
        i1, i2, i3 = [0], [0, k], [0, k, 2 * k]
        m1, m2, m3 = s1, s1 + s2, s1 + s2 + s3

        for j in range(1, len(nums) - 3 * k + 1):
            s1 += nums[j + k - 1] - nums[j - 1]
            s2 += nums[j + 2 * k - 1] - nums[j + k - 1]
            s3 += nums[j + 3 * k - 1] - nums[j + 2 * k - 1]

            if m1 < s1:
                m1 = s1
                i1 = [j]
            if m2 < s2 + m1:
                m2 = s2 + m1
                i2 = i1 + [j + k]
            if m3 < s3 + m2:
                m3 = s3 + m2
                i3 = i2 + [j + 2 * k]
        return i3


#         [1,2,1,2,6,7,5,1], k=2

#         s1=3, s2=3, s3=13
#         m1=3, m2=6, m3=19
#         i1=0  i2=0,2 i3=0,2,4

#         s1=3, s2=8, s3=12
#         m1=3, m2=11, m3=23
#         i1=0  i2=0,3 i3=0,3,5

#         s1=3, s2=13, s3=6
#         m1=3, m2=16, m3=23
#         i1=0  i2=0,4 i3=0,3,5


from typing import List
def maxSumOfThreeSubarrays11(nums: List[int], k: int) -> List[int]:
    w1, w2, w3 = map(sum, [nums[:k], nums[k:2 * k], nums[2 * k:3 * k]])
    max1, max2, max3 = w1, w2 + w1, w3 + w2 + w1
    idx1, idx2, idx3 = [0], [0, k], [0, k, 2 * k]
    print(f"w1={w1}, w2={w2}, w3={w3}")
    print(f"max1={max1}, max2={max2}, max3={max3}")
    print(f"idx1={idx1}, idx2={idx2}, idx3={idx3}")

    for i in range(1, len(nums) - 3 * k + 1):
        w1 += nums[i + k - 1] - nums[i - 1]
        w2 += nums[i + 2 * k - 1] - nums[i + k - 1]
        w3 += nums[i + 3 * k - 1] - nums[i + 2 * k - 1]
        print(f"i={i}, w1={w1}, w2={w2}, w3={w3}")

        if w1 > max1:
            max1, idx1 = w1, [i]
        if max1 + w2 > max2:
            max2, idx2 = max1 + w2, idx1 + [i + k]
        if max2 + w3 > max3:
            max3, idx3 = max2 + w3, idx2 + [i + 2 * k]
    return idx3

nums = [1,2,1,2,6,7,5,1]
k = 2
# nums=[6,7,0,4,1,8,9,2,5,4,9]
# k=2

print(maxSumOfThreeSubarrays11(nums, k))

def maxSumOfThreeSubarrays1(nums, k):
    def helper(i, cnt):
        print(f"memo={memo}")
        if i>=len(nums) or cnt> 3:
            return 0

        if (i, cnt) in memo:
            return memo[(i, cnt)]

        maxVal = 0
        rtn1 = winSums[i] + helper(i+2, cnt+1)
        rtn2 = helper(i+1, cnt)

        memo[(i, cnt)] = max(rtn1, rtn2)
        return memo[(i, cnt)]

    m = 3
    if len(nums) < k * m: return []
    memo = {}
    winSums = [0 for _ in range(len(nums))]
    winSums[0] = sum(nums[:k])
    for i in range(1, len(nums) - k + 1):
        winSums[i] = winSums[i - 1] - nums[i - 1] + nums[i + k - 1]
    print(winSums)
    maxVal=float('-inf')
    for i in range(len(nums) - 1):
        maxVal = max(maxVal, helper(i, 0))
        print(maxVal)
    return maxVal

nums = [1,2,1,2,6,7,5,1]
k = 2
# nums=[6,7,0,4,1,8,9,2,5,4,9]
# k=2


# print(maxSumOfThreeSubarrays1(nums, k))

def maxSumOfThreeSubarrays(nums, k):
    m = 3
    if len(nums) < k * m: return []
    winSums = [0 for _ in range(len(nums))]
    winSums[0] = sum(nums[:k])
    for i in range(1, len(nums) - k + 1):
        winSums[i] = winSums[i - 1] - nums[i - 1] + nums[i + k - 1]
    print(winSums)

    maxSum = [0 for _ in range(m + 1)]
    maxIdx = [[] for _ in range(m + 1)]

    for s in range(len(nums) - k * m + 1):
        for i in range(1, m + 1):
            idx = s + (i - 1) * k
            wSum = winSums[idx]
            if wSum + maxSum[i - 1] > maxSum[i]:
                maxSum[i] = wSum + maxSum[i - 1]
                maxIdx[i] = maxIdx[i - 1] + [idx]
                print(maxSum, maxIdx)

    print(maxSum[-1])
    return maxIdx[m]

nums = [1,2,1,2,6,7,5,1]
k = 2

print()
print(maxSumOfThreeSubarrays(nums, k))


from collections import defaultdict
def maxSumOfThreeSubarrays2(nums, k):
    m = 3
    if len(nums) < k * m: return []

    winDict = defaultdict(lambda: [0, []])
    winSums = [sum(nums[:k])]
    for i in range(1, len(nums) - k+1):
        winSums.append(winSums[i - 1] - nums[i - 1] + nums[i + k -1])

    print(winSums)
    for s in range(len(nums) - m * k + 1):
        for i in range(1, m + 1):

            sIdx = s + (i - 1) * k
            wSum = winSums[sIdx]

            if wSum + winDict[i - 1][0] > winDict[i][0]:
                winDict[i][0] = wSum + winDict[i - 1][0]
                winDict[i][1] = winDict[i - 1][1] + [sIdx]
    return winDict[m][1]


# winSum = [3,3,3,8,13,12,6]
# s = 0, winDict = {0:[0, []], 1:[3, [0], 2:[3+3, [1, 3]], 3:[13+6,[0, 3, 5]]}

# s = 0, 1, 2
#   i = 1, 2, 3
# s= 0, winDict = {0:[0, []], 1:[3, [0]], 2:[3+3, [0, 2]], 3:[16, [0, 2, 4]]}
# s= 1, winDict = {0:[0, []], 1:[3, [0]], 2:[3+8, [0, 3]], 3:[23, [0, 3, 5]]}

nums = [1,2,1,2,6,7,5,10]
k = 2
# nums=[4,3,2,1]
# k = 1
nums=[6,7,0,4,1,8,9,2,5,4,9]
k=2

# print(maxSumOfThreeSubarrays(nums, k))

# 1031. Maximum Sum of Two Non-Overlapping Subarrays




# https://youtu.be/r_uJ9Vlqaqs
from typing import List
from collections import defaultdict
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        m = 3
        windowSums = [sum(nums[:k])]

        for i in range(1, len(nums)-k+1):
            windowSums.append(windowSums[-1] - nums[i-1] + nums[i+k-1])

        print(f"windowSums={windowSums}")

        # maxSums = defaultdict(lambda: [0, []])
        maxSums = defaultdict(lambda: [0, []])
        for s in range(len(nums)-k*m + 1):
            print(f"s={s}")
            for i in range(1, m+1):
                l = s + (i-1)*k
                print(f"  s={s}, i={i}, l={l}, k={k}")
                wSum = windowSums[l]
                print(f"  wSum={wSum}, maxSums[i-1][0]={maxSums[i-1][0]}, {maxSums[i][0]}")
                if wSum + maxSums[i-1][0] > maxSums[i][0]:
                    maxSums[i][0] = wSum + maxSums[i-1][0]
                    maxSums[i][1] = maxSums[i-1][1] + [l]
                    print(f"  maxSums[i][0]={maxSums[i][0]}, maxSums[i][1]={maxSums[i][1]}")
                print(f"maxSums={maxSums}")

        return maxSums[m][1]

nums=[1,2,1,2,6,7,5,1]
k=2
# obj = Solution()
# print(obj.maxSumOfThreeSubarrays(nums, k))

# 1031. Maximum Sum of Two Non-Overlapping Subarrays

# https://github.com/ryancheunggit/leetcode/blob/master/code/689_solution.py
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#              [6]
# max, loc = 13, 4
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#  [3] [3]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 3+3,[0,2]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#    [3] [8]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 11=3+8>6,[0,3]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#      [3] [13]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 16=3+13>11,[0,4]
# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#        [8] [12]
# max_of_1, loc_of_1 = 8, [3]
# max_of_2, loc_of_2 = 20=12+8>16,[3,5]

# --------------------------
#  0 1 2 3 4 5 6 7
# [1,2,1,2,6,7,5,1], 2
#    [3] [8] [12]
# max_of_1, loc_of_1 = 3, [0]
# max_of_2, loc_of_2 = 11,[0,3]
# max_of_3, loc_of_3 = 23,[0,3,5]

# max_of_i = max(max_of_i, max_of_{i-1}+sum_current_subarray_i)

# class Solution:
#     def maxSumOfThreeSubarrays(self, nums: List[int], k: int, m=3) -> List[int]:
#         # Space and Time O(n)
#         window_sums = [sum(nums[:k])]
#         for i in range(1, len(nums) - k + 1):
#             window_sums.append(window_sums[-1] - nums[i - 1] + nums[i + k - 1])
#
#         # Space O(m^2)
#         max_sums = collections.defaultdict(lambda: [0, []])
#
#         # Time O(m*n)
#         for s in range(len(nums) - k * m + 1):  # O(n)
#             for i in range(1, m + 1):  # O(m)
#                 l = s + (i - 1) * k
#                 window_sum = window_sums[l]
#                 if window_sum + max_sums[i - 1][0] > max_sums[i][0]:
#                     max_sums[i][0] = window_sum + max_sums[i - 1][0]
#                     max_sums[i][1] = max_sums[i - 1][1] + [l]
#         return max_sums[m][1]

'''
    def maxSumOfThreeSubarrays(self, nums, k):
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k * 2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k * 2])
        seqThreeSum = sum(nums[k * 2:k * 3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1

        print(f"bestSeq={bestSeq}, bestTwoSeq={bestTwoSeq}, bestThreeSeq={bestThreeSeq}")
        print(f"seqSum={seqSum}, seqTwoSum={seqTwoSum}, seqThreeSum={seqThreeSum}")
        print(f"bestSeqSum={bestSeqSum}, bestTwoSum={bestTwoSum}, bestThreeSum={bestThreeSum}")
        print(f"seqIndex={seqIndex}, twoSeqIndex={twoSeqIndex}, threeSeqIndex={threeSeqIndex}")

        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq

    def maxSumOfThreeSubarrays2(self, nums, k):
        w1, w2, w3 = sum(nums[:k]), sum(nums[k:2 * k]), sum(nums[2 * k:3 * k])
        mw1, mw2, mw3 = w1, w1 + w2, w1 + w2 + w3
        mw1index, mw2index, mw3index = [0], [0, k], [0, k, 2 * k]  # mw1,mw2,mw3's index.
        for i in range(1, len(nums) - 3 * k + 1):  # last index for w1 window will be n-3k
            w1 += nums[i - 1 + k] - nums[i - 1]
            w2 += nums[i - 1 + 2 * k] - nums[i - 1 + k]
            w3 += nums[i - 1 + 3 * k] - nums[i - 1 + 2 * k]
            if w1 > mw1:
                mw1, mw1index = w1, [i]
            if mw1 + w2 > mw2:
                mw2, mw2index = mw1 + w2, mw1index + [i + k]
            if mw2 + w3 > mw3:
                mw3, mw3index = mw2 + w3, mw2index + [i + 2 * k]
        return mw3index

    def maxSumOfThreeSubarrays3(self, nums: List[int], k: int) -> List[int]:
        W = []  # array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            print(f"i={i}, x={x}, cur_sum={curr_sum}, W={W}")
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                W.append(curr_sum)

        print(f"cur_sum={curr_sum}, W={W}")

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans is None or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, l
        return ans

    def maxSumOfThreeSubarrays4(self, nums, k):
        subsum = sum(nums[:k])
        take1 = [(0, ()) for _ in range(len(nums))]
        take2 = [(0, ()) for _ in range(len(nums))]
        take3 = [(0, ()) for _ in range(len(nums))]

        for i in range(k - 1, len(nums)):
            print(f"i={i}, subsum={subsum}, i-k={i-k}, {nums[i - k]}, {nums[i]}")
            subsum = subsum - nums[i - k] + nums[i]
            print(f"    subsum={subsum}")

            # update take 1
            if subsum > take1[i - 1][0]:
                take1[i] = (subsum, (i - k + 1,))
            else:
                take1[i] = take1[i - 1]
            print(f"take1={take1}")

            # update take 2
            if subsum + take1[i - k][0] > take2[i - 1][0]:
                newval = subsum + take1[i - k][0]
                newidx = take1[i - k][1] + (i - k + 1,)
                take2[i] = (newval, newidx)
            else:
                take2[i] = take2[i - 1]
            print(f"take2={take2}")

            # update take 3
            if subsum + take2[i - k][0] > take3[i - 1][0]:
                newval = subsum + take2[i - k][0]
                newidx = take2[i - k][1] + (i - k + 1,)
                take3[i] = (newval, newidx)
            else:
                take3[i] = take3[i - 1]
            print(f"take3={take3}")

        return take3[-1][1]
'''