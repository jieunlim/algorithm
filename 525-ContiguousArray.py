
# 525. Contiguous Array

def findMaxLength(nums):
    dict = {0:-1}
    maxVal = 0
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            sum -= 1
        elif nums[i] == 1:
            sum += 1

        if sum in dict:
            print(dict[sum])
            maxVal = max(maxVal, i - dict[sum])
        else:
            dict[sum] = i
    return maxVal

# dict = {-1:0, 0:1, 1:2,
nums = [0,1,1,0]
nums = [1,1,1,1,1,1,1,1]
# -1,0,1,0

print(findMaxLength(nums))
