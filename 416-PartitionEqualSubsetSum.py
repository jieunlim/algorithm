# 416. Partition Equal Subset Sum
# input array 에 1 이 반복되는 경우, BFS 가 효율적이지 않을 수 있으므로,
# backtracking, DP with memoization 으로.
# O(2^n) exponential -> O(n^2) n square
def canPartition(self, nums: List[int]) -> bool:
    def helper(target, idx):
        if target == 0:
            return True

        if idx >= len(nums):
            return False

        if (target, idx) in memo:
            return memo[(target, idx)]

        t = target - nums[idx]
        if t >= 0:
            memo[(target, idx)] = helper(t, idx + 1)
            if memo[(target, idx)]: return True

        memo[(target, idx)] = helper(target, idx + 1)
        return memo[(target, idx)]

    if not nums: return False

    half, remainder = divmod(sum(nums), 2)

    if remainder != 0 or len(nums) < 2:
        return False
    memo = {}
    return helper(half, 0)

def canPartition2(nums):

    def partition(i, target):

        if target == 0: return True
        if i >= len(nums) or target < 0:
            return False
        if (i, target) in memo:
            return memo[(i, target)]

        memo[(i, target)] = partition(i+1, target-nums[i]) or partition(i+1, target)
        return memo[(i, target)]

    if not nums: return True
    half, remainder = divmod(sum(nums), 2)
    if remainder == 1 or len(nums) < 2: return False
    memo = {}

    return partition(0, half)

nums = [1, 5, 11, 5]
nums=[1,2,3,4]
nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
# False

nums = [40,96,95,7,65,34,39,12,86,36,35,69,9,62,64,85,53,43,87,5,44,94,94,87,85,28,3,75,62,84,76,85,56,30,88,95,22,11,46,63,35,18,23,10,45,86,11,98,5,1,76,48,76,23,57,21,10,70,78,65,1,21,53,43,88,49,14,60,21,87,46,63,7,57,93,88,57,72,12,69,56,68,95,46,100,30,7,13,87,65,41,60,3,38,16,96,94,3,3]
# True

nums=[23,13,11,7,6,5,5]
print("canPartition:", canPartition(nums))

# 698. Partition to K Equal Sum Subsets



class Solution:

    # https://github.com/booknara/playground/blob/master/src/main/java/com/booknara/problem/backtracking/PartitionEqualSubsetSum.java
    # Backtracking
    # O(2^n)
    # 48 ms
    def canPartition1(self, nums):
        self.cnt1 = 0
        def helper(start, target):
            # print(f"start={start}, target={target}")
            if target == 0: return True #start could be len(nums) and target == 0, this logic is first than below.
            if start == len(nums) or target < 0: return False
            if (start, target) in memo:
                return memo[(start, target)]

            self.cnt1 += 1
            memo[(start, target)] = helper(start + 1, target - nums[start]) or helper(start + 1, target)
            return memo[(start, target)]

        if not nums: return True
        target, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        memo = {}
        return helper(0, target)

    # DP
    # O(n^2)
    def canPartition2(self, nums):
        def helper(start, target):
            # print(f"start={start}, target={target}")
            if (start, target) in memo:
                return memo[(start, target)]

            if target == 0:
                return True

            for idx, n in enumerate(nums[start:], start+1):
                if target >= n and helper(idx, target - n):
                    return True

            memo[(start, target)] = False
            return memo[(start, target)]

        if not nums: return True
        target, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        memo = {}
        return helper(0, target)

    # DP
    def canPartition3(self, nums):
        def helper(start, target):
            print(f"target={target}, start={start}")
            if start > len(nums) - 1: return False

            if target in nums[start:]: #efficient way
                memo[(start, target)] = True
                return memo[(start, target)]

            if (start, target) in memo:
                return memo[(start, target)]

            for idx, n in enumerate(nums[start:], start + 1):
                print(f"idx={idx}, n={n}")
                if target - n >= 0 and helper(idx, target - n):
                    memo[(start, target)] = True
                    return memo[(start, target)]

            memo[(start, target)] = False
            return memo[(start, target)]

        if not nums: return True
        half, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        memo = {}
        return helper(0, half)


    # TLE
    # BFS는 맞지 않음.
    def canPartition55(self, nums):
        from collections import deque
        if not nums: return True
        target, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        nums = sorted(nums)
        dq = deque([(target, -1)])
        while dq:
            t, start = dq.popleft()
            if t == 0:
                return True

            for i in range(start+1, len(nums)):
                if t < nums[i]: break
                if t == nums[i]: return True
                if t > nums[i]: dq.append((t-nums[i], i))

        return False


# nums = [1, 5, 11, 5] #T
# nums = [1, 2, 3, 5]
# nums = [1,2,5]
# nums = [2,2,3,5]
# nums = [1,2,3,4,5,6,7] #true
nums=[1,2,3,4]
nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
# False, (canPartition1-9901 canPartition2-156948) after memo(4950 4852)

nums = [40,96,95,7,65,34,39,12,86,36,35,69,9,62,64,85,53,43,87,5,44,94,94,87,85,28,3,75,62,84,76,85,56,30,88,95,22,11,46,63,35,18,23,10,45,86,11,98,5,1,76,48,76,23,57,21,10,70,78,65,1,21,53,43,88,49,14,60,21,87,46,63,7,57,93,88,57,72,12,69,56,68,95,46,100,30,7,13,87,65,41,60,3,38,16,96,94,3,3]
# True (144 54), (98 53)

# nums=[1,1,1,1,1,1,1,1,100]
# nums=[2,2,3,5]
obj = Solution()
print(obj.canPartition1(nums))
print()
print(obj.canPartition2(nums))
# print(obj.cnt1, obj.cnt2)


# 39. Combination Sum
# 279. Perfect Squares
'''

    # 184 ms
    def canPartition3(self, nums):
        def helper(start, target):
            # print(f"target={target}, start={start}")
            if start > len(nums) - 1: return False
            if target in nums[start:]:
                memo[(start, target)] = True
                return memo[(start, target)]

            if (start, target) in memo:
                return memo[(start, target)]

            for idx, n in enumerate(nums[start:], start+1):
                if target - n >= 0 and helper(idx, target - n):
                    memo[(start, target)] = True
                    return memo[(start, target)]

            memo[(start, target)] = False
            return memo[(start, target)]

        if not nums: return True
        half, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        memo = {}
        return helper(0, half)

    # 328 ms
    def canPartition4(self, nums):

        def helper(start, target):
            # print(f"target={target}, start={start}")
            if start > len(nums) - 1: return False
            if target in nums[start:]: return True
            if (start, target) in memo:
                return memo[(start, target)]

            for idx, n in enumerate(nums[start:], start + 1):
                # print(f"   target={target}, n={n}, idx={idx}")
                if n > target:
                    break
                if helper(idx, target - n):
                    return True

            memo[(start, target)] = False
            return memo[(start, target)]

        if not nums: return True
        half, remainder = divmod(sum(nums), 2)
        if remainder == 1 or len(nums) < 2: return False

        nums = sorted(nums)
        memo = {}
        return helper(0, half)


'''


# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90618/7-Lines-59ms-Recursive-Python-Solution

class Solution(object):
    def canPartition(self, nums):
        nums.sort(reverse=True)
        def helper(start, target):         # Here path is not needed
            if target < 0: return
            elif target == 0: return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]): return True
            return False

        return False if sum(nums)%2 else helper(0, sum(nums)/2)


    def canPartition(self, nums):
        cache = {}
        def helper(start, target):         # Here path is not needed
            if (start, target) in cache:
                return cache[(start, target)]
            if target < 0:
                return
            elif target == 0:
                return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            cache[(start, target)] = False
            return False
        return False if sum(nums)%2 else helper(0, sum(nums)/2)