# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(idx):
            print(f"idx={idx}, memo={memo}")
            if idx < len(s) and s[idx] == '0':
                return 0

            if idx >= len(s) - 1:
                return 1

            if idx in memo:
                return memo[idx]

            cnt = helper(idx + 1)
            print(f"  idx={idx}, cnt={cnt}, s[idx:idx + 2]={s[idx:idx + 2]}")

            if 1 <= int(s[idx:idx + 2]) <= 26:
                cnt += helper(idx + 2)

            memo[idx] = cnt
            print(f"return idx={idx}, memo={memo}")
            return memo[idx]

        if len(s) == 0: return 0

        memo = {}
        return helper(0)


    def numDecodings2(self, s: str) -> int:
        # Assume there is only 1 way tot decode
        # Algorithm will add on more branching cases
        prev = current = 1
        for i in reversed(range(len(s))):
            letter = s[i]
            temp_prev = current
            if letter == '0':
                current = 0
            elif letter == '1' and i != len(s) - 1:
                current += prev
            elif letter == '2' and i != len(s) - 1 and s[i + 1] in '0123456':
                current += prev
            prev = temp_prev
        return current

s='0'
s='10'
s = '226'
s = '100'
s = '02' #0
s = '190' #0
s = '1901' #0
obj = Solution()
print(obj.numDecodings(s))