# 202. Happy number
# time O(logN)
# space O(logN) for visited hashset
#
# O(243*3 + logN + loglogN + logloglogN...) => O(logN)
# given number is n,
# number of digits in a given number n is (logn + 1)
# it eventually gets to 1 / it eventaully gets stuck in a cycle
# it keeps going higher and higher? No, numbers with 4 or more digits will always lose a digit at each step
#  until they are down to 3 digits.
#  So, at worst, the algorithm might cycle around all the numbers under 243 and then go back to cycle or go to 1.
#
# 1. given a number n, what is the next number?
# 2. detect if the number is 1 and in a cycle => use a HashSet
#
# time complexity
#  N == 9999, # of digits are logN,
#  the next number would be 81*logN -> 81*log(81*logN) which means loglogN -> logloglogN...
# [numbers with 4 or more digits]operations will be performed as many as # of digits
# logN + log(logN) + logloglogN...

# [numbers with 3 or less digits] 999 -> next number is 81*3 = 243 ->....
# 3 digits or less numbers will go to 1 or go to cycle, worst case 243 times, 3 digits, so 243*3 is the worst case.

# O(operations of 3 digits or less numbers + operations of 4 or more numbers)
# O(243*3+logn+loglogn+logloglogn...) -> O(logn)

def isHappy( n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            print(f"n={n}, digit={digit}")
            total_sum += digit ** 2
            print(f"total_sum={total_sum}")

        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        print(n, seen)
        seen.add(n)
        n = get_next(n)
        print(n, seen)

    return n == 1

# n=19
# n=7
n=116
print(isHappy(n))
