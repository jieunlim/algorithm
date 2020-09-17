# 560. Subarray Sum Equals K
# the total number of continuous subarrays whose sum equals to k

# hashmap
# O(n), O(n)
class Solution:
    def subarraySum(self, nums, k):
        from collections import defaultdict
        sum = res = 0
        dict = defaultdict(int)
        dict[0] = 1

        for n in nums:
            sum += n
            print(f"n={n}, sum= {sum}, dict={dict}, sum - k={sum - k}")
            if sum - k in dict:
                res += dict[sum-k]
                print(f"res={res}, dict={dict}")
            dict[sum] += 1

        print(f"res={res}")
        return res
nums=[2,3,1,2,2,1,3]
k=6

nums=[0,0,0,0,0,0,0,0,0,0]
k=0
obj = Solution()
print(obj.subarraySum(nums, k))


# O(N^2)
def subarraySum2(nums, k):
    cnt = 0
    for start in range(len(nums)):
        sum = 0
        for end in range(start, len(nums)):
            sum += nums[end]
            if sum == k:
                cnt += 1

    return cnt
