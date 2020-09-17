# 581. Shortest Unsorted Continuous Subarray

# find the shortest such subarray and output its length.

class Solution:
    # Sort
    # O(nlgn), O(n)
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
            return 0

        start = 0
        while sorted_nums[start] == nums[start]:
            start += 1
        end = len(nums) - 1

        while sorted_nums[end] == nums[end]:
            end -= 1

        print(f"{nums[start:end+1]}")
        return end + 1 - start

    # Two pointers
    # time O(n), space O(n) for subarray (temp variable)
    def findUnsortedSubarray2(self, nums):

        print(f"nums={nums}")
        if len(nums) < 2: return 0

        l, r = 0, len(nums) - 1
        print(f"l={l}, r={r}")
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1

        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        print(f"l={l}, r={r}")
        if l > r:
            return 0

        temp = nums[l:r + 1]
        tempMin = min(temp)
        tempMax = max(temp)
        print(f"temp={temp}, tempMin={tempMin}, tempMax={tempMax}")

        while l > 0 and tempMin < nums[l - 1]:
            l -= 1

        while r < len(nums) - 1 and tempMax > nums[r + 1]:
            r += 1

        print(f"l={l}, r={r}, r - l + 1={r - l + 1}")
        return r - l + 1

    # space O(1)
    def findUnsortedSubarray3(self, nums):
        def find_min_max(l, r):
            locaMin = float('inf')
            locamMax = float('-inf')
            for i in range(l, r + 1):
                if i == len(nums):
                    break
                locaMin = min(locaMin, nums[i])
                locamMax = max(locamMax, nums[i])

            return locaMin, locamMax

        if len(nums) < 2: return 0
        l, r = 0, len(nums) - 1

        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1

        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        if l > r:
            return 0

        tempMin, tempMax = find_min_max(l, r + 1)

        while l > 0 and tempMin < nums[l - 1]:
            l -= 1

        while r < len(nums) - 1 and tempMax > nums[r + 1]:
            r += 1

        return r - l + 1

nums = [2, 6, 4, 10]
nums=[2, 6, 4, 8, 10, 9, 15]
obj = Solution()
print(obj.findUnsortedSubarray2(nums))