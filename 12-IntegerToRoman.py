
# 12. Integer to Roman

class Solution:
    def intToRoman1(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res, i = "", 0
        while num:
            print(f"num={num}, res={res}, i={i}, values[i]={values[i]}, numerals[i]={numerals[i]}")
            res += (num // values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res

    def intToRoman2(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        # for i, v in enumerate(values):
        #     res += (num // v) * numerals[i]
        #     num %= v
        # return res
        for n, v in zip(numerals, values):
            res += (num // v) * n
            num %= v
        return res

    # dictionaries are ordered from Python 3.6
    def intToRoman3(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'}

        res = ""

        for i in d:
            res += (num // i) * d[i]
            num %= i
            print(f"res={res}, num={num}, i={i}")

        return res

num = 13
obj = Solution()
print(obj.intToRoman3(num))