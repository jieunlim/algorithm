# 215. Kth Largest Element in an Array

# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
# 347. Top K Frequent Elements

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        for i, n in enumerate(nums):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        for _ in range(k):
            res = heapq.heappop(nums)

        return -res

    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums: return -1
        pq = []
        for n in nums:
            pq.append(-n)
        heapq.heapify(pq)

        for i in range(k):
            rtn = heapq.heappop(pq)

        return -rtn



    # O(nlgn) time
    def findKthLargest1(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]


    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        print(f"nums={nums}")
        for i in range(k):
            for j in range(len(nums) - i - 1):
                print(f"i={i}, j={j}. nums[j]={nums[j]}, nums[j + 1]={nums[j + 1]}, nums={nums}")
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(f"nums={nums}")
        return nums[len(nums) - k]


    # O(nk) time, selection sort idea
    def findKthLargest3(self, nums, k):
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]


    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)


    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k - 1]


    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums) + 1 - k)


    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]


    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

nums=[3,2,1,5,6,4]
k=2
obj = Solution()
print(obj.findKthLargest2(nums, k))


# 347. Top K Frequent Elements