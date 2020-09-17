# 42. Trapping Rain Water

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

# 11. Container With Most Water
def maxArea(height):
    l, r = 0, len(height)-1
    volume = 0

    while l < r:
        if height[l] < height[r]:
            volume = max((r-l)*height[l], volume)
            print(f"{l}, {r}, {height[l]}, l - volume={volume}")
            l += 1
        else:
            volume = max((r-l)*height[r], volume)
            print(f"r - volume={volume}")
            r -= 1

    return volume

height=[0,4,0,2,0,1]
print(trap(height))