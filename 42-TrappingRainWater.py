# 42. Trapping Rain Water
# time O(N), space O(N)

def trap(height):
    if not height: return 0

    ans, size = 0, len(height)
    leftMax, rightMax = [0 for _ in range(size)], [0 for _ in range(size)]

    leftMax[0] = height[0]
    for i in range(1, size):
        leftMax[i] = max(height[i], leftMax[i-1])

    print(leftMax)
    rightMax[size - 1] = height[size-1]
    for i in range(size-2, -1, -1):
        rightMax[i] = max(height[i], rightMax[i+1])

    print(rightMax)
    for i in range(1, size-1):
        ans += min(leftMax[i]-height[i], rightMax[i]-height[i])
        print(f"i={i}, {leftMax[i]-height[i]}, {rightMax[i]-height[i]}")

    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))



# time O(N), space O(1)

def trap(height):
    if not height or len(height) < 3:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    l_max, r_max = height[left], height[right]

    while left < right:

        l_max, r_max = max(height[left], l_max), max(height[right], r_max)
        print(f" left={left}, right={right}, l_max={l_max}, r_max={r_max}")

        if l_max <= r_max:
            volume += l_max - height[left]
            left += 1
            print(f"    [left] left={left}, right={right} volume={volume}")
        else:
            volume += r_max - height[right]
            right -= 1
            print(f"    [right] left={left}, right={right}  volume={volume}")

    return volume

# height = [0,1,0,2,1,0,1,3,2,1,2,1]  #6
height=[0,4,0,2,0,1]
print(trap(height))

# 11. Container With Most Water


# 238. Product of Array Except Self
# 407. Trapping Rain Water II
# 755. Pour Water



'''
def trap(height):

    leftM = rightM = water = 0
    l, r = 0, len(height)-1
    while l < r:
        leftM, rightM = max(leftM, height[l]), max(rightM, height[r])

        if leftM < rightM:
            water += leftM - height[l]
            l += 1
        else:
            water += rightM - height[r]
            r -= 1

    return water
'''