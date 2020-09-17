# 739. Daily Temperatures

class Solution:
    # time O(n)
    # Space Complexity also would be O(n) as we are using Stack in addition to the list
    # https://leetcode.com/problems/daily-temperatures/discuss/136017/Elegant-Python-Solution-with-Stack
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            print(f"i={i}, t={t}, stack={stack}")
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
                print(f"cur={cur}, ans={ans}")
            stack.append(i)

        return ans

    # Approach #2: Stack
    def dailyTemperatures2(self, T):
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            print(f"i={i}, stack={stack}")
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
                print(f"ans={ans}")
            stack.append(i)
        return ans

    # Time Limit Exceeded
    def dailyTemperatures3(self, T):
        if not T: return
        lenT = len(T)
        res = []
        for i in range(lenT):
            cnt = 0
            for j in range(i+1,lenT):
                print(f"i={i}, j={j}, T[i] {T[i]} < T[j] {T[j]}")
                if T[i] < T[j]:
                    cnt = j-i
                    break
            res.append(cnt)
        return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
obj = Solution()
print(obj.dailyTemperatures3(T))