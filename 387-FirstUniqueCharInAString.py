# 387. First Unique Character in a String
# linear search with Hashmap
# time O(N), N is a number of characters in the string
# space O(N)
from collections import Counter
def firstUniqChar(s):
    # build hash map : character and how often it appears
    cnter = Counter(s)
    print(cnter)

    # find the index
    for i in range(len(s)):
        if cnter[s[i]] == 1:
            return i
    return -1

# s = "leetcode"
s = "loveleetcode"
print(firstUniqChar(s))


