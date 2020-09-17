# 249. Group Shifted Strings
# https://www.youtube.com/watch?v=vUd-7qS6BPQ

from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        def getOffset(s):
            res = []
            for ch in s:
                res += [(ord(ch) - ord(s[0]))%26 ]
                print(ch, res, s)
            return tuple(res)

        groupDict = defaultdict(list)
        for s in strings:
            groupDict[getOffset(s)].append(s)

        return groupDict.values()
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
obj = Solution()
print(obj.groupStrings(strings))