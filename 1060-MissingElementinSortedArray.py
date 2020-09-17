# 1060. Missing Element in Sorted Array

class Solution:

    def missingElement(self, nums, k):

        misCnt = []
        for i, n in enumerate(nums):
            misCnt.append(nums[i] - nums[0] - i)
        # misCnt = [0, 2, 3, 3]

        if k > misCnt[-1]:
            return nums[-1] - misCnt[-1] + k

        missing, idx = 0, 0
        for i, cnt in enumerate(misCnt):
            if cnt >= k: break
            missing = cnt
            idx = i
        return nums[idx] - misCnt[idx] + k

    def missingElement2(self, nums, k):

        misCnt = []
        for i, n in enumerate(nums):
            misCnt.append(nums[i] - nums[0] - i)
        # misCnt = [0, 2, 3, 3]
        print(misCnt)

        start, end = 0, len(nums)  #### for the bigger number of the last value, not len(nums)-1
        while start < end:
            mid = start + (end - start) // 2
            if misCnt[mid] < k:
                start = mid + 1
            else:
                end = mid

        return nums[start - 1] - misCnt[start - 1] + k

    def missingElement33(self, nums, k):
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
        print(f"missing={missing}")

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        idx = 1
        # find idx such that
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is greater than nums[idx - 1]
        # and less than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)

    def missingElement22(self, nums, k):
        def getMissingNumber(idx):
            return nums[idx] - nums[0] - idx

        start, end = 0, len(nums)
        while start < end:
            mid = start + (end-start)//2
            print(f"start={start}, end={end}, mid={mid}")
            rtn = getMissingNumber(mid)
            print(f"rtn={rtn}")
            if rtn < k:
                start = mid+1
            else:
                end = mid
            print(f"start={start}, end={end}")
        return nums[start-1] + k - getMissingNumber(start - 1)

    def missingElement3(self, nums, k):

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] - nums[0] - mid < k:  # count the number of missing from the begining to mid point
                l = mid
            else:
                r = mid - 1

        return nums[0] + k + l
A = [4,7,9,10]
K = 1
A=[1,2,4]
K=3
obj = Solution()
print(obj.missingElement(A, K))