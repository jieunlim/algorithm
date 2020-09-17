
# 45. Jump Game II
class Solution2:
    def jumpGame(self, nums):
        self.minVal = float('inf')

        def jump(pos):
            print(f"pos={pos}")
            if pos >= len(nums)-1:
                print(f"return  ")
                return 0

            if pos in memo:
                return memo[pos]

            distance = min(len(nums), pos + nums[pos]+1)
            print(f"distance={distance}")
            for j in range(pos+1, distance):
                self.minVal = min(self.minVal, jump(j) + 1)
                print(f"  self.minVal={self.minVal}")

            memo[pos] = self.minVal
            return memo[pos]

        if len(nums) == 1: return 0
        memo = {}
        jump(0)
        return self.minVal

nums = [2,3,1,1,4] #2
nums = [2,3,0,1,4] #2
# nums = [0] #0
# nums = [1] #0
# nums=[1,2] #1
# nums=[2,1]
nums=[1,2,3]
# nums=[1,4,3,7,1,2,6,7,6,10]
# nums=[7,9,5,2,5,7,3,8,8,7,9,3,1,7,6,3,8,7,2,2,5,9]

obj = Solution2()
print(obj.jumpGame(nums))


class Solution:
    # https://youtu.be/vBdo7wtwlXs
    # O(n)
    def jump(self, nums):
        print(f"nums={nums}")
        if len(nums) <= 1: return 0
        # ladder - keep track of largest ladder that you have
        # stairs - keep track of stairs in the current ladder
        ladder = stairs = nums[0]
        jump = 1
        print(f"ladder={ladder}, stairs={stairs}, jump={jump}")
        for i in range(1, len(nums)):
            print(f"*i={i}")
            if i == len(nums) - 1:
                return jump
            if i + nums[i] > ladder:
                ladder = i + nums[i]  # build up the ladder
            stairs -= 1 #use up the stairs
            print(f"stairs={stairs}")
            print(f"i + nums[i]={i + nums[i]}, ladder={ladder}")

            if stairs == 0:
                jump += 1 #no stairs left, now jump
                stairs = ladder - i #get new set of stairs
                print(f"jump={jump}, stairs={stairs}")
            print(f"jump={jump}")
        return jump

    # https://youtu.be/cETfFsSTGJI

    def jumpGame22(self, nums):
        if len(nums) == 1:
            return 0
        next = nums[0]
        curEnd = nums[0]
        cur = 1
        result = 1

        print(f"next = {next}, curEnd = {curEnd}, cur={cur}, result={result}")
        while cur <= next and next < len(nums) - 1:
            print(f"cur={cur}, next={next}")
            if nums[cur] + cur > next:
                next = nums[cur] + cur

            if cur == curEnd:
                curEnd = next
                result += 1

            cur += 1
            print(f"next = {next}, curEnd = {curEnd}, cur={cur}, result={result}")

        return result if curEnd >= len(nums) - 1 else result + 1

    def jump22(self, nums):
        res = 0
        edge = 0
        maxEdge = 0
        for i in range(len(nums)):
            print(f"i={i}, edge={edge}, maxEdge={maxEdge}")
            if i > edge:
                edge = maxEdge
                res += 1
                print(f"   res={res}, edge={edge}")
            maxEdge = max(maxEdge, i + nums[i])
        return res

    def jump11(self, nums):
        n = len(nums)
        if n < 2:
            return 0

            # max position one could reach
        # starting from index <= i
        max_pos = nums[0]
        # max number of steps one could do
        # inside this jump
        max_steps = nums[0]

        jumps = 1
        for i in range(1, n):
            # if to reach this point
            # one needs one more jump
            print(f"i={i}, max_steps={max_steps}")
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
                print(f"jumps={jumps}, max_steps={max_steps}")
            max_pos = max(max_pos, nums[i] + i)
            print(f"max_pos={max_pos}")

        print(f"jumps={jumps}")
        return jumps

    def jump2(self, nums):
        n, start, end, step = len(nums), 0, 0, 0

        while end < n - 1:
            print(f"end = {end}")
            step += 1
            maxend = end + 1
            print(f"step={step}, maxend={maxend}, end={end}")

            for i in range(start, end + 1):
                print(f"i={i}")
                if i + nums[i] >= n - 1:
                    print(f"return step={step}")
                    return step
                maxend = max(maxend, i + nums[i])
                print(f"maxend={maxend}")
            start, end = end + 1, maxend
            print(f"start={start}, end={end}")
        return step

    def jump3(self, nums):
        n = len(nums)
        dp = [0] * n
        lstMin = dp[-1]
        lstMinIdx = n - 1
        print(f"n={n}, dp={dp}, lstMin={lstMin}, lstMinIdx={lstMinIdx}")
        for i in range(n - 2, -1, -1):
            ed = (n - 1 if i + nums[i] >= n - 1 else i + nums[i])
            if lstMinIdx > ed or ed > nums[i + 1] + i + 1:
                lstMin = float("inf")
                for j in range(i + 1, ed + 1):
                    if dp[j] < lstMin:
                        lstMin = dp[j]
                        lstMinIdx = j
            dp[i] = float("inf") if nums[i] == 0 else lstMin + 1

        return dp[0]

nums=[2,3,1,1,4]
# nums=[1,4,3,7,1,2,6,7,6,10]
obj = Solution()
# print(obj.jump(nums))



