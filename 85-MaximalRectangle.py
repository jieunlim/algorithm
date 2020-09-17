# 85. Maximal Rectangle

# time complexity O(n^2)?

class Solution:


    # same, save space
    # O(column size)
    def maximalRectangle3(self, matrix):
        if not matrix:
            return 0
        m, n, A = len(matrix), len(matrix[0]), 0
        height = [0 for _ in range(n+1)]
        for i in range(m):
            print(f"height={height}")
            for j in range(n):
                height[j] = height[j] + 1 if matrix[i][j] == "1" else 0
                print(f"i={i}, j={j}, height={height}")
            A = max(A, self.largestRectangleArea(height))
            print(f"A={A}")
        return A

    def largestRectangleArea(self, height):
        # height.append(0)
        stack, A = [0], 0
        print(f"** height={height}")
        for i in range(1, len(height)):
            print(f"i=  {i}, height[stack[-1]]={height[stack[-1]]}, height[i]={height[i]}")
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                A = max(A, w * h)
                print(f"    h={h}, w={w}, A={A}")
            stack.append(i)
            print(f"   stack={stack}")
        return A

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
matrix = [
  ["1","0","1","1"],
  ["0","1","1","1"]
]
matrix = [
  ["0","0","1","0"],
  ["1","0","1","1"],
  ["1","1","1","1"]
]
matrix = [
  ["1","0","0","1"],
  ["0","1","1","1"]
]
obj = Solution()
print(obj.maximalRectangle3(matrix))

# 84. Largest Rectangle in Histogram
# 221. Maximal Square




'''

# Solution Approach 3

    # Get the maximum area in a histogram given its heights
    def getRecHistogram(self, heights):
        stack = [-1]

        maxarea = 0
        print(f"heights={heights}")
        for i in range(len(heights)):
            print(f"i={i}, stack[-1]={stack[-1]}")
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
                print(f" 1while   maxarea={maxarea}, stack[-1] ={stack[-1]}")
            stack.append(i)
            print(f"stack={stack}")

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
            print(f" 2while maxarea={maxarea}")
        return maxarea


    def maximalRectangle(self, matrix):

        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones

                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
                print(f"dp={dp}")

            # update maxarea with the maximum area from this row's histogram
            print(f"    i={i}, j={j}, maxarea={maxarea}")
            maxarea = max(maxarea, self.getRecHistogram(dp))
        return maxarea

# https://leetcode.com/problems/maximal-rectangle/discuss/29140/Pyrhon-O(n2)-solution-based-on-Largest-Rectangle-in-Histogram
    def maximalRectangle2(self, matrix):
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]

        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j-1][i] + 1
        print(f"m={m}")
        return max(self.largestRectangleArea2(row) for row in m)

    def largestRectangleArea2(self, height):
        height.append(0)
        stack, size = [], 0
        print(f"*height={height}")
        for i in range(len(height)):
            print(f"i={i}")
            while stack and height[stack[-1]] > height[i]:
                print(f"  while - stack={stack}, height[stack[-1]]={height[stack[-1]]}")
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                size = max(size, h*w)
                print(f"  h={h}, w={w}, size={size}")
            stack.append(i)
            print(f"stack = {stack}")
        print(f"size={size}")
        return size

'''