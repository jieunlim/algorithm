# 344. Reverse String

def reverse_string(s):
    s.reverse()

# time: O(N)
# space: O(N)
def reverse_string1(s):

    def rs(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            rs(left+1, right-1)
    rs(0, len(str)-1)

# time: O(N)
# space: O(1)
def reverse_string2(s):

    left, right = 0, len(str)-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left, right = left+1, right-1

str = ["h","e","l","l","o"]
reverse_string(str)
print("1:", str)
str = ["h","e","l","l","o"]
reverse_string1(str)
print("2:", str)
str = ["h","e","l","l","o"]
reverse_string2(str)
print("3:", str)


'''
# 344. Reverse String
def reverseString(s):

    # iteration
    i, j = 0, len(s)-1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s

def reverseString2(s):

    def rStr(i, j):

        if i >= j:
            return
        s[i], s[j] = s[j], s[i]

        rStr(i+1, j-1)

    rStr(0, len(s)-1)


s=["h","e","l","l","o"]
reverseString2(s)
print(s)

'''