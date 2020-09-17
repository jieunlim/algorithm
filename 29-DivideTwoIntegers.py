
# 29. Divide Two Integers

# Both dividend and divisor will be 32-bit signed integers.
# MAX_INT = 2147483647  # 2**31 - 1
# MIN_INT = -2147483648  # -2**31

# recommended operation
# a = a* -1 => a = -a
# a/2 => a >> 1
# a*2 => a << 1

class Solution:
    # O(N)
    # while dividend < divisor, increasing quotient
    def divide1(dividend, divisor):
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = -dividend

        if divisor < 0:
            negatives += 1
            divisor = -divisor

        quotient = 0
        while dividend - divisor >= 0:
            quotient += 1
            dividend -= divisor

        return -quotient if negatives == 1 else quotient

    # O(logN*logN)
    # check overflow
    # a / b = c,
    # c <= a, the answer c cannot end up bigger than the thing we divided(a)
    # if a and b is within the range(-2^31, 2^31-1). the result a/b will be closer to zero,
    # so it never overflow,
    # except a = -2^31, b = -1 ==> should return 2^31-1 (edge case)

    # a = -2^31, if we change into positive, will be overflow,
    # so we can use negative dividend, negative divisor.

    # The best solution is to work with with negative, instead of positive, numbers.
    # This is allows us to use the largest possible
    # range of numbers, and it covers all the ones we need.

    def divide2(self, dividend: int, divisor: int) -> int:

        INT_MAX = 2 ** 30 + 2 ** 30 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1: return INT_MAX
        # if dividend == INT_MIN and divisor == 1: return INT_MIN

        negative = (dividend < 0) ^ (divisor < 0)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        quotient = 0
        while dividend <= divisor:
            print(f"dividend={dividend}, divisor = {divisor}")
            powerOfTwo, accum = 1, divisor
            while accum >= (INT_MIN >> 1) and dividend <= accum + accum:
                powerOfTwo <<= 1
                accum += accum
                # print(f"accum={accum}, {i}")
            dividend -= accum
            quotient += powerOfTwo
            print(f"dividend={dividend}, quotient={quotient}")

        return -quotient if negative else quotient


    # O(LogN)
    def divide3(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 30 + (2 ** 30 - 1)

        if dividend == INT_MIN and divisor == -1: return INT_MAX
        #if dividend == INT_MIN and divisor == 1: return INT_MIN

        negative = (dividend < 0) ^ (divisor < 0)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor

        quotient, powerOfTwo, accum = 0, 1, divisor
        while accum >= INT_MIN >> 1 and dividend <= accum + accum:
            powerOfTwo <<= 1
            accum += accum
            print(f"powerOfTwo={powerOfTwo}, accum={accum}")

        while dividend <= divisor:
            print(f"dividend={dividend}, divisor = {divisor}")
            if dividend <= accum:
                dividend -= accum
                quotient += powerOfTwo
                print(f"dividend={dividend}, quotient={quotient}, powerOfTwo={powerOfTwo}, accum={accum}")
            accum >>= 1  #O(32)
            powerOfTwo >>= 1
            print(f"accum={accum}, powerOfTwo={powerOfTwo}")

        return -quotient if negative else quotient

# dividend =  -2147483648
# divisor = -1
# dividend = -50
# divisor = 3
# dividend = 10
# divisor = 3
# dividend = -2147483648
# divisor = 2

dividend = 93706
divisor = 157

dividend = 900
divisor = 10

obj = Solution()
print(obj.divide3(dividend, divisor))



'''


    #     31 - 3 (divisor << times) times = 0 , q = 1
    #     28 - 6 times  = 1 , q = 3
    #     22 - 12 times = 2, q = 7
    #     10 - 24 times = 3 -> 2
    #     10 - 12 times = 2 -> 1
    #     10 - 6 times  = 1, q = 9
    #     4  - 6 times  = 0
    #     4  - 3 q      = 10
class Solution11:

    # using positive numbers, but this won't work other than Python
    def divide22(self, dividend: int, divisor: int) -> int:

        INT_MAX = 2 ** 30 + 2 ** 30 - 1
        INT_MIN = -2 ** 31

        if dividend == INT_MIN and divisor == -1: return INT_MAX
        if dividend == INT_MIN and divisor == 1: return INT_MIN

        negative = (dividend < 0) ^ (divisor < 0)
        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor

        quotient = 0
        while dividend >= divisor:
            i, accum = 1, divisor
            while accum < (INT_MAX >> 1) and dividend >= accum + accum:
                i <<= 1
                accum += accum
            dividend -= accum
            quotient += i

        return -quotient if negative else quotient
        
    def divide(self, dividend: int, divisor: int) -> int:

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        q, times = 0, 0

        while dividend >= divisor:
            print(f"dividend={dividend}, divisor={divisor}, times={times}")
            cur = dividend - (divisor << times)
            print(f"  cur={cur}, , divisor << times = {divisor << times}")

            if cur >= 0:
                q += (1 << times)
                times += 1
                dividend = cur
                print(f"   q ={q}, times={times}, dividend={dividend}")
            else:
                times -= 1
                print(f"  times={times}")

        return max(-2 ** 31, min(q * sign, 2 ** 31 - 1))

'''