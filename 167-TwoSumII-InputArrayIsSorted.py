# 167. Two Sum II - Input array is sorted

# two pointer
# time O(n)
# space O(1)
def twoSumII(numbers, target):

    i, j = 0, len(numbers)-1

    while i < j:
        total = numbers[i] + numbers[j]

        if total == target:
            return [i+1, j+1]
        elif total < target:
            i += 1
        else:
            j -= 1
    return -1

    # i, j = 0, len(numbers)-1
    # numbers = list(enumerate(numbers, start=1))
    #
    # while i < j:
    #     s = numbers[i][1] + numbers[j][1]
    #
    #     if s == target:
    #         return [numbers[i][0], numbers[j][0]]
    #     elif s < target:
    #         i += 1
    #     else:
    #         j -= 1
    #
    # return -1

# hash
# time O(n)
# space O(n)
def twoSumII2(numbers, target):
    dict ={}
    for i, x in enumerate(nums, start = 1):
        y = target - x
        if y in dict:
            return [dict[y], i]
        dict[x] = i
    return -1

# binary search
def twoSumII3(numbers, target):
    for i in range(len(numbers)):
        l, r = i + 1, len(numbers) - 1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == tmp:
                return [i + 1, mid + 1]
            elif numbers[mid] < tmp:
                l = mid + 1
            else:
                r = mid - 1
nums = [2,7,11,15]
target = 9
print(twoSumII(nums, target))
