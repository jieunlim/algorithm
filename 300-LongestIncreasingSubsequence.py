# 300. Longest Increasing Subsequence

# https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step
class Solution:
# O(n*m) solution. m is the sub[]'s length
    def lengthOfLIS(self, nums):
        sub = []
        print(f"nums={nums}")
        for val in nums:
            pos, sub_len = 0, len(sub)
            print(f"val = {val}, pos={pos}, sub_len={sub_len}")
            while (pos <= sub_len):  # update the element to the correct position of the sub.
                print(f"  pos={pos}, sub_len={sub_len}")
                if pos == sub_len:
                    sub.append(val)
                    print(f"  pos == sub_len, sub={sub}")
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    print(f"  val <= sub[pos], sub={sub}")
                    break
                else:
                    pos += 1
                    print(f"  pos={pos}")

        print(f"len(sub)={len(sub)}, sub={sub}")
        return len(sub)

# O(nlogn) solution with binary search
    def lengthOfLIS2(self, nums):
        def binarySearch(sub, val):
            lo, hi = 0, len(sub) - 1
            print(f"sub={sub}, val={val}, lo={lo}, hi={hi}")
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                print(f"lo={lo}, hi={hi}, mid={mid}, sub[mid]={sub[mid]}")
                if sub[mid] < val:
                    lo = mid + 1
                    print(f"lo={lo}")
                elif val < sub[mid]:
                    hi = mid - 1
                    print(f"hi={hi}")
                else:
                    print(f"return mid {mid}")
                    return mid
            print(f"return lo ={lo}")
            return lo

        sub = []
        for val in nums:
            print(f"val={val}")
            pos = binarySearch(sub, val)
            print(f"pos={pos}")
            if pos == len(sub):
                sub.append(val)
                print(f"1.sub={sub}")
            else:
                sub[pos] = val
                print(f"2.sub={sub}")
        return len(sub)

nums = [10,9,2,5,3,7,101,18]
# nums = [3,2,5,6]
obj = Solution()
print(obj.lengthOfLIS2(nums))