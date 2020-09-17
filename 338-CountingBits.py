# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/discuss/79557/How-we-handle-this-question-on-interview-Thinking-process-%2B-DP-solution

class Solution(object):
    def countBits(self, num):
        res = [0 for _ in range(num + 1)]
        for i in range(1, num+1):
            res[i] = res[i // 2] + (i % 2)
        return res

    def countBits2(self, num):
        res = [0,]
        for i in range(1, num+1):
            bits = i
            bitCnt = 0
            while bits:
                bitCnt += bits&1
                bits = bits >> 1
            res.append(bitCnt)
        return res

    # https://leetcode.com/problems/counting-bits/discuss/79538/Simple-Python-Solution
    # Code works by constantly extending a list with itself but with the values incremented by 1
    def countBits3(self, num):
        res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res]
            print(f"len(res)={len(res)}, num={num}, res={res}")
        return res[:num + 1]

obj = Solution()
n = 16
print(obj.countBits3(n))

# 0-5 [0, 1,1,2,  1] [ 2,2,3,1,2 ] [2, 3,2,3,3][4,1
# 0-0,
# 1-1,
# 2-10,
# 3-11,
# 4-100,

# 5-101,
# 6-110
# 7-111
# 8-1000
# 9-1001

# 10-1010
# 11-1011
# 12-1100
# 13-1101
# 14-1110
# 15-1111
# 16-10000


# 1011 \
# &0001 = 0001
# &0010
# &0100
# &1000
#
# 1011&0001
# 101&0001
#
# 1011 >> 1


# 191. Number of 1 Bits

