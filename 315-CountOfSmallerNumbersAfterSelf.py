
# 315. Count of Smaller Numbers After Self


#Time limit exceeded
def cnt_smaller_number_after_self(nums):

    cnt_arr = [0 for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                cnt_arr[i] += 1
    return cnt_arr


nums = [5,2,6,1]
# print(cnt_smaller_number_after_self(nums))

def countSmaller(nums):
    def countSmaller_re(e_nums):
        half = len(e_nums)//2
        if half:
            left = countSmaller_re(e_nums[:half])
            right = countSmaller_re(e_nums[half:])

            for i in range(len(e_nums)-1, -1, -1):
                if not right or left and left[-1][1] > right[-1][1]: #no data in right or...
                    smaller_arr[left[-1][0]] += len(right)
                    e_nums[i] = left.pop()
                else:
                    e_nums[i] = right.pop()
        return e_nums

    smaller_arr = [0] * len(nums)
    countSmaller_re(list(enumerate(nums)))
    return smaller_arr

# nums = [5,2,6,1]
print(countSmaller(nums))

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
# Time O(NlgN), Space O(N)
# Mergesort, Divide and conquer
# Add up len(right) to count arrary(return value) whenever left > right
# remember original index

def countSmaller2(nums):
    def sort(enum):
        half = len(enum)// 2
        print(f"half={half}, enum={enum}")
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            print(f"left={left}, right={right}")

            for i in range(len(enum))[::-1]:
            # for i in range(len(e_nums) - 1, -1, -1):
                print(f"i={i}, left={left}, right={right}, enum={enum}")
                if not right or left and left[-1][1] > right[-1][1]:
                    if left and right:
                        print(f"i={i}, left[-1][1]={left[-1][1]}, right[-1][1]={right[-1][1]}")
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                    print(f"smaller={smaller}, enum[{i}]={enum[i]}")
                else:
                    enum[i] = right.pop()
            print(f"enum is = {enum}")
        return enum

    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

nums = [5,2,6,1]
nums=[4,5,2,1]
print(countSmaller2(nums))
