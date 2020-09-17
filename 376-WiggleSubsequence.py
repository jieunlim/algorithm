
# 376. Wiggle Subsequence

class Solution:
    # https://leetcode.com/problems/wiggle-subsequence/discuss/162996/python-O(n)-time-O(1)-space-easy-to-understand-16-ms-solution-beats-100
    def wiggleMaxLength(self, nums):

        if not nums:
            return 0

        length = 1
        up = None  # current is increasing or not
        for i in range(1, len(nums)):
            # print(f"i={i}")
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False

        return length

    # https://leetcode.com/problems/wiggle-subsequence/discuss/506582/easily-understood-Python-soln-16ms
    def wiggleMaxLength2(self, nums):

        n=len(nums)
        if n<2:
            return(n)
        diff=[]

        print(f"nums={nums}")
        for i in range(1,n):
            print(f"i={i}, diff={diff}")

            if nums[i]>nums[i-1]:
                diff.append(1)
            elif nums[i]<nums[i-1]:
                diff.append(-1)
            else:
                diff.append(0)

        count=n
        prev=0
        for j in range(n-1):
            print(f"j={j}, diff={diff}")
            if diff[j]==0:
                count-=1
                print(f"  count={count}")
            else:
                if diff[j]==prev:
                    count-=1
                prev=diff[j]
                print(f"  count={count}, prev={prev}")

        return(count)

    # O(nlogn) sort, space O(1)
    def wiggleSort33(self, nums):

        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]


nums=[1,7,4,9,2,5]
obj = Solution()
print(obj.wiggleMaxLength(nums))


# 280. Wiggle Sort
# 324. Wiggle Sort II