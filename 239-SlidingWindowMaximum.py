# 239. Sliding Window Maximum

from collections import deque
class Solution:
    # time O(Nk)
    # space O(N-k+1)
    def maxSlidingWindow1(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            print(f"i={i}, dq={dq}")
            if dq and dq[0] < i - k + 1:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            # if i > k - 2:
            if i+1 >= k:
                res.append(nums[dq[0]])
        return res

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
obj = Solution()
print(obj.maxSlidingWindow(nums, k))


'''
    def maxSlidingWindow2(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        from collections import deque
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        print(nums)

        def clean_deque(i):
            print(f"clean - deq={deq}, i={i}")
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            print(f"deq={deq}")
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
            print(f"deq={deq}, output={output}")
        return output

    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            print(f"i={i}")
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            print(f"  left={left}")
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
                print(f"  (j + 1) % k ={(j + 1) % k }")
            else:
                right[j] = max(right[j + 1], nums[j])
            print(f"  right={right}")

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
            print(f"output={output}, left[{i + k - 1}]={left[i + k - 1]}, right[{i}]={right[i]}")

        return output
'''
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# obj = Solution()
# print(obj.maxSlidingWindow(nums, k))