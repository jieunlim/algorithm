
# 13. Roman to Integer

# the maximum number possible number can be 3999,
# which in roman numerals is MMMCMXCIX. As such the time complexity is O(1)
# https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution
class Solution:
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            print(f"roman[s[i]]={roman[s[i]]}, roman[s[i+1]]={roman[s[i+1]]}")
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
                print(f"* z={z}")
            else:
                z += roman[s[i]]
                print(f"** z={z}")

        print(f"roman[s[-1]]={roman[s[-1]]}")
        return z + roman[s[-1]]

    def romanToInt2(self, s):

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        sum = 0

        for i in s[::-1]:
            curr = roman[i]
            print(f"i={i}, prev={prev}, curr={curr}")
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            print(f"sum={sum}")
            prev = curr
        return sum

s="IV"
s="MDIC"
obj = Solution()
print(obj.romanToInt2(s))