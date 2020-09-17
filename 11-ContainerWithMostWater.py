
# 11. Container With Most Water
# O(n), O(1)

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


height=[1,3,5,2]
# height =[1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# 42. Trapping Rain Water



# 907. Sum of Subarray Minimums
# 1152. Analyze User Website Visit Pattern
# 1217. Play with Chips
'''
def maxArea2(height):
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        print(f"w={w}, L={L}, R={R}, height[L]={height[L]}, height[R]={height[R]}")
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
        print(f"res={res}, L={L}, R={R}")
    return res
'''