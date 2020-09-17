# 34. Find First and Last Position of Element in Sorted Array
# sorted array, O(lgN)
# -->
# binary search

class Solution:
    # time O(lgN)
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)

    def searchRange3(self, nums, target):
        def find(flag):
            start, end  = 0, len(nums)-1
            rtn = -1
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    rtn = mid
                    if not flag: end = mid - 1
                    else: start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return rtn

        res=[-1,-1]
        res[0], res[1] = find(0), find(1)
        return res

    def searchRange(self, nums, target):

        def findStart():
            left, right = 0, len(nums)-1
            start = -1

            while left <= right:
                m = left + (right-left)//2

                print(f"m={m}, left={left}, right={right}")
                if nums[m] == target:
                    start = m
                    right = m - 1
                    print(f"start={start}, right={right}")
                elif nums[m] < target:
                    left = m+1
                    print(f"left={left}")
                else:
                    right = m-1
                    print(f"right={right}")
            return start

        def findEnd():
            left, right = 0, len(nums)-1
            end = -1

            while left <= right:
                m = left + (right - left) // 2

                print(f"m={m}")
                if nums[m] == target:
                    end = m
                    left = m + 1
                    print(f"end={end}, left={left}")
                elif nums[m] < target:
                    left = m + 1
                    print(f"left={left}")
                else:
                    right = m - 1
                    print(f"right={right}")
            return end

        res = [-1,-1]
        if not nums: return res
        res[0] = findStart()
        res[1] = findEnd()

        return res


    def searchRange2(self, nums, target):
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                print(f"m={m}, nums[m]={nums[m]} < target={target}")
                if nums[m] < target:
                    l = m + 1
                    print(f"l={l}")
                else:
                    r = m
                    print(f"r={r}")
            print(l if nums[l] == target else -1)
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                # m = (l + r) // 2 + 1
                m = (l + r + 1) // 2
                print(f"m={m}, nums[m]={nums[m]} > target={target}, l={l}, r={r}")
                if nums[m] > target:
                    r = m - 1
                    print(f"r={r}")
                else:
                    l = m
                    print(f"l={l}")
            print(l if nums[l] == target else -1)
            return l if nums[l] == target else -1

        print(f"nums={nums}")
        return [bisect_left(nums, target), bisect_right(nums, target)]

# time O(N) by ms
    def searchRange3(self, nums, target):
        res = [-1, -1]
        start, end = 0, len(nums) - 1

        while start <= end:
            half = (start+end) // 2

            if nums[half] == target:
                for i in range(half, -1, -1):
                    if nums[i] == target:
                        res[0] = i
                    else:
                        break
                for i in range(half, len(nums)):
                    if nums[i] == target:
                        res[1] = i
                    else:
                        break
                break
            elif nums[half] > target:
                end = half - 1
            else:
                start = half + 1
        return res

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8,9,10,10,11,12]
target = 10
# nums = [5,5,5,5,5,5,5,5,5,5,5]
# target = 25
nums=[5,7,7,8,8,10]  # right function test " m = (l + r) // 2 + 1  "
target=8
obj = Solution()
print(obj.searchRange(nums, target))