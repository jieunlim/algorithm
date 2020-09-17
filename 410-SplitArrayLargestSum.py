
# 410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation

class Solution(object):
    ##     without memoization, Time Limit Exceeded
    def helper(self, nums, m):
        print(f"nums={nums}, m={m}")
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[:j]), self.helper(nums[j:], m - 1)
                print(f"left={left}, right={right}")
                min_result = min(min_result, max(left, right))
                print(f"min_result={min_result}")
            return min_result

    def splitArray(self, nums, m):
        return self.helper(nums, m)


# Memoization
# ## with memoization, 3376ms
from collections import defaultdict
class Solution2(object):
    def helper(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[i:i + j]), self.helper(i + j, nums, m - 1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:
                    break
            return cache[i][m]

    def splitArray(self, nums, m):

        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)


# binary search 36ms
class Solution3(object):
    def is_valid(self, nums, m, mid):
        # assume mid is < max(nums)
        cuts, curr_sum = 0, 0
        print(f"[is_valid] nums={nums}, m={m}, mid={mid}")
        for x in nums:
            curr_sum += x
            print(f"x={x}, curr_sum={curr_sum}")
            if curr_sum > mid:
                cuts, curr_sum = cuts + 1, x
                print(f"cuts={cuts}, curr_sum={curr_sum}")
        subs = cuts + 1
        print(f"subs={subs}")
        return (subs <= m)

    def splitArray(self, nums, m):

        low, high, ans = max(nums), sum(nums), -1
        print(f"low={low}, high={high}, ans={ans}")
        while low <= high:
            mid = (low + high) // 2
            print(f"mid={mid}")
            if self.is_valid(nums, m, mid):  # can you make at-most m sub-arrays with maximum sum atmost mid
                ans, high = mid, mid - 1
                print(f"ans={ans}, high={high}")
            else:
                low = mid + 1
                print(f"low={low}")
        print(f"ans={ans}")
        return ans

nums=[7,2,5,10,8]
# nums=[10,5,17]
m=2
obj = Solution3()
print(obj.splitArray(nums, m))


'''


# https://leetcode.com/problems/split-array-largest-sum/discuss/373306/Python3-BinarySearch-Accepted-and-Well-Documented-Solution
# 410. Split Array Largest Sum
class Solution:
    def splitArray(self, nums, m):
        # First, understand WHAT we are binary searching over
        # we are doing a binary search over the *search space of possible results*
        # What is the search space, aka what are all possible results?
        # For this, we need to know the minimum and maximum possible result
        ## minimum possible result - largest element in array. Since each element needs
        # to be part of some subarray, the smallest we can go is by taking the largest element
        # in a subarray by itself
        ## maximum possible result - sum of all elements in the array since we cannot form
        # a subarray larger than the array itself
        # Compute minResult and maxResult boundaries
        minResult, maxResult = 0, 0
        print(f"nums={nums}, m={m}")
        for num in nums:
            print(f"num={num}")
            maxResult += num
            print(f"minResult={minResult}")
            if num > minResult:
                minResult = num
                print(f"minResult={minResult}")

        # now that we have our minResult and maxResult boundaries, we can begin searching within this space
        # What are we searching for?
        # The smallest value within this space such that we can form m subarrays from nums and none of their sums exceed that value
        finalResult = float('inf')
        while minResult <= maxResult:
            print(f"minResult={minResult}, maxResult={maxResult}")
            # Start by checking if the value in the middle of the search space satisfies this desired outcome
            # If it does, we can discard all values to the right of this in our search space since we have
            # something better than those already. We only need to search values to the left to see if
            # we can find something better
            # If not, we only need to search values higher than mid
            mid = (minResult + maxResult) // 2
            print(f"mid={mid}")
            if self.isPossibility(mid, nums, m):
                finalResult = mid
                maxResult = mid - 1
                print(f"finalResult={finalResult}, maxResult={maxResult}")
            else:
                minResult = mid + 1
                print(f"maxResult={maxResult}")
        print(f" return finalResult={finalResult}")
        return finalResult

    # Checks to see if x is a valid possibility given the constraint of m subarrays
    def isPossibility(self, x, nums, m):
        print(f"[isPossibility]  x={x}, nums={nums}, m={m}")
        numSubarrays = 1
        subarraySum = 0
        for num in nums:
            print(f"num={num}, subarraySum={subarraySum}")
            # Greedily try to add this element to the current subarray as long as the subarray's sum doesn't exceed our upper limit x
            if (num + subarraySum) <= x:
                subarraySum += num
                print(f"    subarraySum={subarraySum}")
            # If sum would be exceeded by adding the current element, we need to start a new subarray and put this element into that
            else:
                numSubarrays += 1
                subarraySum = num
                print(f"    numSubarrays={numSubarrays}, subarraySum={subarraySum}")
        print(f"return {(numSubarrays <= m)}")
        return (numSubarrays <= m)

nums = [7,2,5,10,8]
nums=[10,5,17]
m = 2
obj = Solution()
# print(obj.splitArray(nums, m))
'''