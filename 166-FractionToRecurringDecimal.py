
# 166. Fraction to Recurring Decimal
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not denominator: return
        if numerator == 0: return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        num = abs(numerator)
        den = abs(denominator)

        quotient, remainder = divmod(num, den)
        res.append(str(quotient))

        if remainder:
            res.append(".")
            dic = {}
            while remainder:
                if remainder in dic:
                    res.insert(dic[remainder], "(")
                    res.append(")")
                    break
                dic[remainder] = len(res)
                q, remainder = divmod(remainder * 10, den)
                res.append(str(q))
        return "".join(res)