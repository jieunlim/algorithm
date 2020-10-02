# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# return an array output
# the product of all the elements of nums except self
# Note: Please solve it without division and in O(n)
class Solution:
# O(N), O(N)
# 왼쪽에서 0번째는 1로 주고, 오른쪽으로 향하면서, i(self)를 제외한 왼쪽편의 곱을 left[i]에 저장.
# 오른쪽에서 len(nums)-1번째를 1로 주고, 왼쪽으로 향하면서 , i(self)를 제외한 오른쪽 편의 곱을 right[i]에 저장.
# left[i]와 right[i]를 곱하면 self를 제외한 결과값
# 하지만 이 경우, O(N) space complexity
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [0] * length
        right = [0] * length
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        if not nums: return []

        nums = [1] + nums + [1]
        left= [ 1 for _ in range(len(nums)) ]
        right= [ 1 for _ in range(len(nums)) ]

        for i in range(1, len(left)-1):
            left[i] = nums[i-1]*left[i-1]

        for i in range(len(left)-2, 0, -1):
            right[i] = nums[i+1]*right[i+1]

        for i in range(1, len(left)):
            left[i] *= right[i]

        return left[1:len(nums)-1]

# Follow up: Could you solve it with constant space complexity
# O(N), O(1)
# 같은 원리로 처리하고, res라는 결과변수를 이용하여 space complexity를 O(1)로 줄임
    def productExceptSelf2(self, nums):
        length = len(nums)
        p = 1
        res = []
        for i in range(length):
            res.append(p)
            p = p * nums[i]
        p = 1
        for i in range(length-1, -1, -1):
            res[i] = res[i] * p
            p = p * nums[i]
        return res
nums = [1, 2, 3, 4]
obj = Solution()
print(obj.productExceptSelf(nums))
nums = [1, 2, 3, 4]
print(obj.productExceptSelf2(nums))







'''

# 238. Product of Array Except Self
class Solution:
    # O(N), O(N)
    def productExceptSelf(self, nums):

        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1

        print(f"L={L}, R={R}, answer={answer}")
        for i in range(1, length):
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
            print(f"i={i}, L[i]={L[i]}, L={L}")

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            print(f"R i={i}")
            R[i] = nums[i + 1] * R[i + 1]
            print(f"i={i}, R[i]={R[i]}, R={R}")

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
            print(f"i={i}, answer={answer}")

        return answer

    # https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space
    # O(N), O(1)
    def productExceptSelf2(self, nums):
        p = 1
        n = len(nums)
        output = []
        print(f"p={p}, n={n}, output={output}")

        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
            print(f"i={i}, output={output}, p={p}")

        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
            print(f"  i={i}, output={output}, p={p}")
        return output

nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf2(nums))

# 42. Trapping Rain Water
# 152. Maximum Product Subarray
# 265. Paint House II

'''