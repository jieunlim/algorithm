# 128. Longest Consecutive Sequence
# O(nlogn) mergesort
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums: return 0
        sortedNums = self.mergeSort(nums)

        cnt, maxCnt = 0, 0
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] + 1 == sortedNums[i + 1]:
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            elif sortedNums[i] != sortedNums[i + 1]:
                cnt = 0
        return maxCnt + 1

    def mergeSort(self, nums) -> List:
        if not nums:
            return []

        if len(nums) < 2:
            return nums

        mid = len(nums) // 2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right) -> List:
        if not left or not right:
            return left or right

        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1
        print(res)
        return res

    # O(n)
    def longestConsecutive2(self, nums):
        if not nums: return 0

        numsSet = set(nums)

        maxVal = 0
        for i in range(len(nums)):
            if nums[i] in numsSet:
                cnt = 1
                curNum = nums[i]
                numsSet.remove(curNum)
                while curNum + 1 in numsSet:
                    cnt += 1
                    curNum += 1
                    numsSet.remove(curNum)


                curNum = nums[i]
                while curNum - 1 in numsSet:
                    cnt += 1
                    curNum -= 1
                    numsSet.remove(curNum)

                maxVal = max(maxVal, cnt)

        return maxVal

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        print(f"num_set={num_set}")
        for num in num_set:
            print(f"num={num}")
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                print(f"current_num={current_num}, current_streak={current_streak}")

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    print(f"   current_num={current_num}, current_streak={current_streak}")

                longest_streak = max(longest_streak, current_streak)
                print(f"longest_streak={longest_streak}")

        return longest_streak

    def longestConsecutive2(self, num):
        num = set(num)
        maxLen = 0
        while num:
            print(f"num={num}")
            n = num.pop()
            i = n + 1
            l1 = 0
            l2 = 0

            print(f"n={n}, i={i}")
            while i in num:
                num.remove(i)
                i += 1
                l1 += 1
                print(f"  i={i}, l1={l1}")
            i = n - 1
            while i in num:
                num.remove(i)
                i -= 1
                l2 += 1
                print(f"  i={i}, l2={l2}")
            maxLen = max(maxLen, l1 + l2 + 1)
        return maxLen
obj = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(obj.longestConsecutive(nums))
print()
print(obj.longestConsecutive2(nums))
