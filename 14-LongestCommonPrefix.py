
# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: return ""

        str1 = strs[0]
        for s in strs[1:]:
            common = ''
            length = min(len(str1), len(s))
            for i in range(length):
                if str1[i] == s[i]:
                    common += s[i]
                else:
                    break
            str1 = common

        return str1




def longestCommonPrefix(strs):

    def lcp(c, s1):
        if not s1: return ""
        cLen = min(len(c), len(s1))
        i = 0
        while i < cLen and c:
            print(f"i = {i}, c[i] = {c[i]}, s1[i]={s1[i]} ")
            if c[i] != s1[i]:
                c = c[:i]
                cLen = len(c)
                return c
            i += 1

        return c

    if not strs:
        return ""
    elif len(strs) == 1:
        return strs[0]

    lenS = len(strs)
    wL = min(len(strs[0]), len(strs[1]))
    common = ""
    i = 0
    print(f"i={i}, wL={wL}")
    while i < wL and strs[0][i] == strs[1][i]:
        common += strs[0][i]
        i += 1

    print(f" common = {common}")
    rtn = common
    if lenS > 2 and rtn:
        j = 2
        while j < lenS:
            print(f" common={common}, strs[j]={strs[j]}")
            rtn = lcp(common, strs[j])
            if rtn:
                j += 1
            else:
                return rtn

    return rtn

# https://leetcode.com/problems/longest-common-prefix/discuss/7138/5-line-python-with-zip()-and-len(set())
def longestCommonPrefix2(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    print(f"shortest={shortest}")
    for i, ch in enumerate(shortest):
        print(f"i={i}, ch={ch}")
        for other in strs:
            print(f"other={other}")
            if other[i] != ch:
                return shortest[:i]
    return shortest

# https://leetcode.com/problems/longest-common-prefix/discuss/172553/beat-100-python-submission-short-and-clean
def longestCommonPrefix3(m):
    if not m: return ''
			#since list of string will be sorted and retrieved min max by alphebetic order
    s1 = min(m)
    s2 = max(m)

    print(f"s1={s1}, s2={s2}")
    for i, c in enumerate(s1):
        print(f"i={i}, c={c}")
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1

s=["flower","flow","flight"]
# s=["dog","racecar","car"]
# s=["a"]
# s=["c", "c"]
# s=["abab","aba",""]
s=["baab","bacb","b","cbc"]

# s=["ac","ac","a","a"]
print("rtn:", longestCommonPrefix3(s))

# 758. Bold Words in String
# 564. Find the Closest Palindrome
# 1062. Longest Repeating Substring

# 925. Long Pressed Name
# 736. Parse Lisp Expression
# 591. Tag Validator