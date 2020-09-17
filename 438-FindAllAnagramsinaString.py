# 438. Find All Anagrams in a String

# O(S)
# space O(1) because pCount and sCount contain not more than 26 elements
from collections import Counter
def findAllAnagrams(s, p):
    pLength = len(p)
    sLength = len(s)

    if pLength > sLength:
        return []

    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:pLength-1])

    for i in range(pLength - 1, sLength):
        sCounter[s[i]] += 1
        if sCounter == pCounter:
            res.append(i - pLength + 1)

        sCounter[s[i-pLength+1]] -= 1
        if sCounter[s[i-pLength+1]] == 0:
            del sCounter[s[i-pLength+1]]
    return res




class Solution:
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter
    def findAnagrams2(self, s, p):
        from collections import Counter

        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        print(f"pCounter={pCounter}, sCounter={sCounter}")
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            print(f"i={i}, pCounter={pCounter},  sCounter={sCounter}")
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
                print(f"res={res}")
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            print(f" i - len(p) + 1={i - len(p) + 1}, sCounter={sCounter}")

            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
                print(f"del sCounter...{sCounter}")
        print(f"return res = {res}")
        return res

    # https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92017/Python-O(n)-sliding-window-with-a-lot-of-comments.-Accepted-solution
    def findAnagrams(self, s, p):
        hash = {}  # hash stores the list of characters we need to cross-off. Initially has all of p in it
        for c in p:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        count = len(p)  # number of characters still to be crossed-off

        print(f"hash={hash}, count={count}")
        # initialize
        result = []
        left = 0  # the current candidate is s[left:right+1]
        right = 0
        while right < len(s):
            # for every iteration, check if current character is a desired char. if so, cross it off. otherwise, move on to the next character

            print(f"right={right}, s={s}, hash={hash}")
            if s[right] in hash:
                hash[s[right]] -= 1
                if hash[s[right]] >= 0:  # If we have a negative hash value(meaning more than enough of that particular character), it means we are not getting any closer to the solution, so, count should not change
                    count -= 1

            print(f"hash={hash}, count={count}")

            # print 'left=', left, 'right=', right, 'count=', count, 'hash=', hash, 'cur_window=', s[left:right+1]
            # if all items are crossed-off, add to result list
            if count == 0:
                result.append(left)

            print(f"result={result}")
            # Move window only if the minimum size is met.
            if right == left + len(p) - 1:
                if s[left] in hash:  # If the char we are getting rid of is already in the hash, increment the hash (add to the items that we need to cross-off)
                    if hash[s[left]] >= 0:  # If the hash (number of items we need to cross-off) is negative(i.e we have had double chars in out current window), do not increment the required count
                        count += 1
                    hash[s[left]] += 1
                left += 1
            right += 1
            print(f"left={left}, right={right}")
        print(f"result={result}")
        return result

s = 'abab'
p = 'ab'
s='cbaebabacd'
p='abc'
obj = Solution()
print(obj.findAnagrams2(s,p))


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
#  the similar questions are:
#
# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
