# 125. Valid Palindrome
#
# Palindrome problems
# 125,9, 680,234
# 647, 5, 539, 1177
# 564, 336, 214

# 647. Palindromic Substrings
# 5. Longest Palindromic Substring
# 516. Longest Palindromic Subsequence
# 1143. Longest Common Subsequence


# O(n), O(1)
def isPalindrome(s):
    i, j = 0, len(s)-1
    s = s.lower()

    while i <= j:
        # print(f"i={i}, j={j}, s[i]={s[i]}, s[j]={s[j]} ")
        # if not s[i].isalpha():
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
            # continue
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1

    return True

s = "A man, a plan, a canal: Panama"
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = "0P"

print(isPalindrome(s))