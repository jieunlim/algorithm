# 953. Verifying an Alien Dictionary

# time complexity O(C) - C is the total content of words
# space complexity O(1)

class Solution:

    def isAlienSorted2(self, words, order):
        hashDict = {}
        for i, ch in enumerate(order):
            hashDict[ch] = i

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if hashDict[w1[j]] > hashDict[w2[j]]:
                        return False
                    break
        return True

    def isAlienSorted(self, words, order):
        ind = {}

        for i, c in enumerate(order):
            ind[c] = i

        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for c1, c2 in zip(w1, w2):
                if ind[c1] < ind[c2]:
                    break
                elif ind[c1] > ind[c2]:
                    return False
        return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
#
# words = ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
obj = Solution()
print(obj.isAlienSorted(words, order))