# 3. Longest Substring Without Repeating Characters

# time O(N), space(O(min(m, n)))
# The size of the Set is upper bounded by the size of the string n
# and the size of the charset/alphabet m

# Hash table, sliding window

def longestSubstringWO(s):

    start = maxL = 0
    dict = {}

    for i in range(len(s)):

        if s[i] in dict and start <= dict[s[i]]:
            start = dict[s[i]] + 1
            # start += 1
        else:
            maxL = max(maxL, i - start + 1)
        dict[s[i]] = i

        print(f"i={i}, s[i]={s[i]}, start={start}, maxL={maxL}, dict={dict}")

    return maxL

s = "abcabcbb"
# s="pwwkew"
# s="pwwwwkew"
# s="tmmzuxta" #and start <= dict[s[i]]
# 't' repeated twice, but if start=2, first 't' is the way before the start, so no need to be considered
# s="aabaab!bb"
print(longestSubstringWO(s))

# 159. Longest Substring with At Most Two Distinct Characters
# 340. Longest Substring with At Most K Distinct Characters
# 992. Subarrays with K Different Integers
'''
def lengthOfLongestSubstring( s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        print(f"i={i}, s[{i}]={s[i]}, usedChar={usedChar}, start={start}")
        if s[i] in usedChar and start <= usedChar[s[i]]:
            print(f"usedChar[s[i]]={usedChar[s[i]]}")
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i
        print(f"start={start}, maxLength={maxLength}, usedChar[s[i]]={usedChar[s[i]]}")
    return maxLength
'''