# 84. Largest Rectangle in Histogram

def largestRectangleArea(heights):
    stack = []
    result = 0
    for i in range(len(heights)):
        stack.append(i)
        for s in range(len(stack)-2, -1, -1):
            if heights[stack[s]] >= heights[i]:
                stack.remove(stack[s])
            else:
                break
        print(f"i={i}, stack={stack}")
        for j in range(len(stack)-1, -1, -1):
            print(f"j={j}")
            h = heights[stack[j]]
            length = i+1
            if j>0: length = i - stack[j-1]
            result = max(result, h*length)
            print(f"  h={h}, len={len}, result={result}")
    return result

heights=[2,1,4,3]
print(largestRectangleArea(heights))
