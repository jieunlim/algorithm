# 9. Palindrome Number
# Follow up: Coud you solve it without converting the integer to a string?

# find the largest power of 10 which is smaller then x first.
# Then check if left most digit is equal to right most digit and so on.
# https://leetcode.com/problems/palindrome-number/discuss/5156/Two-python-solution-with-O(1)-space

def isPalindrome3(  x):
    if x < 0:
        return False
    b = 1
    while x / b >= 10:
        b *= 10

    print(f"b={b}")
    while b >= 10:
        print(f"x / b = {x}//{b}, {x//b}, {x%10}")
        if x // b != x % 10:
            return False
        x, b = (x % b) // 10, b // 100
        print(f" x={x}, b={b}")
    return True


#  reverse the number first and see if it is equal to the original number.
def isPalindrome2(x):

    if x < 0:
        return False

    p, res = x, 0

    while p:
        res = res*10 + p%10
        p //= 10
        # print(f"res={res}, p={p}")

    return x == res


def isPalindrome(x):
    if x < 0:
        return False

    s = str(x)
    i, j = 0, len(s)-1

    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False

    return True
x=-10
x=101
x=12321
print(isPalindrome3(x))