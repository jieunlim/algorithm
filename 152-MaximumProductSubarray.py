# 152. Maximum Product Subarray

# 최대합을 구하는 53. Maximum Subarray과 다르게, array input에 negative 값을 고려해주어야 함.
# 즉, 이전 negative 값 중 가장 작은 값이,
# 다음번에 만나는 negative와 곱할 경우 가장 큰 값이 될 수 있으므로
# max값 뿐 아니라, negative 처리를 위해 min 값도 저장하여 처리해야 함.
# x, y를 번거롭게 따로 둔 이유는 min 계산 중 minP 값이 변하면 max값 계산 시 값이 바뀌기 때문인데
# Python 에서는 한 줄로 처리해도 됨. minP, maxP = min(n, minP*n, maxP*n), max(n, minP*n, maxP*n)

class Solution2:

    def maxProduct(self, nums):

        if not nums: return
        elif len(nums) == 1: return nums[0]

        minP = maxP = res = nums[0]

        for n in nums[1:]:
            x = min(n, minP*n, maxP*n)
            y = max(n, minP*n, maxP*n)
            minP, maxP = x, y
            res = max(res, maxP)

        return res

nums = [2,-3,4,-8,0]
nums = [2,3,-2,4]
obj = Solution2()
print(obj.maxProduct(nums))


'''
    public int maxProduct(int[] nums) {
        
        int prod = 1;
        int result = Integer.MIN_VALUE;
        
        for(int i = 0; i < nums.length; i++) {
            prod = prod * nums[i];
            result = Math.max(prod, result);
            if(prod == 0) {
                prod = 1;
            }
        }
        prod = 1;
        
        for(int i = nums.length - 1; i >= 0; i--) {
        
            prod = prod * nums[i];
            result = Math.max(prod, result);
            if(prod == 0) {
                prod = 1;
            }      
        }
        return result;
    }
'''

class Solution:
    def maxProduct(self, nums):

        if not nums:
            return
        elif len(nums) == 1:
            return nums[0]

        curSum = nums[0]
        res = [nums[0]]
        for n in nums[1:]:
            print(f"n={n}, curSum = {curSum}, res={res}")
            if n > curSum * n:
                res = [n]
            else:
                res.append(n)

            curSum = max(curSum, curSum * n)

        return res

    def maxProduct2(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        print(f"nums={nums}")
        for i in range(1, len(nums)):
            print(f"i={i}, max_prod={max_prod}, min_prod={min_prod}, ans ={ans}")
            x = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            y = min(nums[i], max_prod * nums[i], min_prod * nums[i])
            print(f"x={x}, y={y}")
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans

    # https://leetcode.com/problems/maximum-product-subarray/discuss/384555/Python-Solution-(DP)
    def maxProduct3(self, nums):

        min_so_far, max_so_far, max_global = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far, min_so_far = max(min_so_far * nums[i], max_so_far * nums[i], nums[i]), min(min_so_far * nums[i],
                                                                                                   max_so_far * nums[i],
                                                                                                   nums[i])
            max_global = max(max_global, max_so_far)

        return max_global


nums = [2, 3, -2, 4]
nums = [2, -3, 4, -8, 0]
# nums = [-4, -3, -2]
obj = Solution()
print(obj.maxProduct2(nums))

# 238. Product of Array Except Self
# 628. Maximum Product of Three Numbers
# 713. Subarray Product Less Than K