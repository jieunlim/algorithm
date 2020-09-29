# 139. Word Break

# O(2^n) -> O(n^2)
# O(n)
# https://leetcode.com/problems/word-break/discuss/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below

# cat sand og
#          F
#     sando, sandog
#     F
# cats and
#      ando
#      andog
#      F
# catsa
# catsan
def wordBreak(s, wordDict):

    def helper(idx):
        print(f"idx={idx}, memo={memo}")
        if idx == len(s):
            return True

        if idx in memo:
            return memo[idx]

        for j in range(idx, len(s)):
            subStr = s[idx:j+1]
            print(f"subStr={subStr}")
            if subStr in wordDict:
                if helper(j+1):
                    memo[idx] = True
                    return memo[idx]

        memo[idx] = False
        print(f"return False, idx={idx}, memo={memo}")
        return memo[idx]

    wordDict = set(wordDict)
    memo = {}
    return helper(0)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))


def wordBreak(s, wordDict):

    def helper(start):
        print(f"start={start}, memo={memo}")
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        for i in range(start, len(s)):
            print(s[:i+1])
            if s[start:i+1] in wordDict:
                if helper(i+1):
                    memo[start] = True
                    print(f"i={i}")
                    return memo[start]

        memo[start] = False
        return memo[start]

    memo = {}
    return helper(0)

s= 'catsdog'
wordDict = ['cats', 'dog']
# print(wordBreak(s, wordDict))
# start = 3, helper(4)

class Solution(object):
    # 140. Word Break II
    def wordBreak2(self, s, wordDict):

        def helper(start):
            print(f"start={start}, memo={memo}")
            if start in memo:
                return memo[start]
            res = []
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    print(f"   i={i}, start={start}, s[start:i+1]={s[start:i+1]}")
                    if i+1 == len(s):
                        res.append(s[start:i+1])
                    else:
                        rtn = helper(i+1)
                        print(f"     s[start:i+1]={s[start:i+1]}, start={start}, i={i}, rtn={rtn}")
                        for each in rtn:
                            print(f"     each={each}")
                            res.append(' '.join([s[start:i+1], each]))
                            print(f"     res={res}")

            memo[start] = res
            print(f"return {memo[start]}, start={start}, memo={memo}")
            return memo[start]

        memo = {}
        return helper(0)

s= 'catsanddog'
wordDict = ['cats', 'cat','sand', 'and', 'dog']
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
obj = Solution()
# print(obj.wordBreak2(s, wordDict))

# a = ['A','B']
# print(" ".join(a))

# pine apple pen apple
#                  * apple
#              *pen apple
#        *apple pen apple/applepen apple
#   *pine apple pen apple/pine applepen apple/pileapple pen apple




class Solution:
# time O(n**2)
# space O(n)
# DP
# catsanddog - true flag at the end of each word
# FFTTFFTFFT
    def wordBreak(self, s, wordDict):
        word_bool = [False] * len(s)

        for i in range(len(s)):
            for j in range(i, len(s)):
                print(f"i={i}, j={j}. word_bool[i-1]={word_bool[i-1]}, s[i:j+1]={s[i:j+1]}")
                if (i == 0 or word_bool[i - 1]) and s[i:j + 1] in wordDict:
                    word_bool[j] = True
                    print(f"word_bool={word_bool}")

        # print(word_bool)
        return word_bool[-1]



# O(2^n) -> O(n^2) with memoization
# https://leetcode.com/problems/word-break/discuss/169383/The-Time-Complexity-of-The-Brute-Force-Method-Should-Be-O(2n)-and-Prove-It-Below

    def wordBreak1(self, s, wordDict):
        def wB(start):
            print(f"*start={start}, memo={memo}")
            if start == lenS:
                return True
            if start in memo:
                return memo[start]

            for i in range(start,lenS):
                print(f"    i={i}")
                if s[start:i+1] in wordDict:
                    print(f"    s[start:i+1]={s[start:i+1]}")
                    if wB(i+1):
                        memo[start] = True
                        print(f"    return {memo[start]}, memo={memo}")
                        return memo[start]
            memo[start] = False
            print(f"    return(BBB) {memo[start]}, memo={memo}")
            return memo[start]

        memo = {}
        wordDict = set(wordDict)
        lenS = len(s)
        print(f"s={s}, wordDict={wordDict}")
        return wB(0)

    def wordBreak2(self, s, wordDict):
        def wB(start):

            w = s[start:end]
            print(f"start={start}, w={w}, memo={memo}")
            if w in memo:
                print(f" return memo[w]={memo[w]}")
                return memo[w]

            for i in range(start, end):
                print(f"i={i}, {s[start:i+1]}, memo={memo}")
                if s[start:i+1] in wordDict:
                    memo[s[start:i+1]] = True
                    if i == end-1:
                        print(f"return True, i={i}, end={end}")
                        return True
                    if wB(i+1):
                        return True
            memo[w] = False
            return memo[w]

        memo = {}
        end = len(s)
        return wB(0)

    def wordBreak3(self, s, wordDict):

        def wordB(start, end):
            print(f"start={start}, end={end}, memo={memo}")
            w = s[start:end]
            print(f"w={w}")
            if w in memo:
                print(f"return memo {memo[w]}")
                return memo[w]
            # if w in wordDict:
            #     memo[w] = True
            #     return True

            for i in range(start, end):
                print(f"i={i}, [start:i + 1]={s[start:i + 1]}")
                if s[start:i + 1] in wordDict:
                    memo[s[start:i + 1]] = True

                    if i == end-1:
                        print(f" i=end-1, i={i}, end={end}, return True")
                        return True
                    elif wordB(i + 1, end):
                        print(f" after wordB {i+1}, {s[i+1:end]} return True")
                        return True

            memo[s[start:end + 1]] = False
            print(f"memo[s[start:end + 1]]={memo[s[start:end + 1]]}, memo = {memo}")
            return False

        memo = {}
        wordDict = set(wordDict)
        return wordB(0, len(s))

    # def wordBreak2(self, s, wordDict):
    #
    #     def wBreak_re(start, end):
    #         print(f"start={start}, end={end}, s[start:end]={s[start:end]}, memo={memo}")
    #
    #         if s[start:end] in memo:
    #             return memo[s[start:end]]
    #         elif s[start:end] in wordDict:
    #             memo[s[start:end]] = True
    #             print(f"(return True) memo={memo}")
    #             return True
    #
    #         for i in range(start, end-1):
    #             print(f"i={i}, s[start:i + 1]={s[start:i + 1]}, wordDict={wordDict}, memo={memo}")
    #             # if s[start:i + 1] in wordDict and wBreak_re(i + 1, end):
    #             if s[start:i + 1] in wordDict:
    #                 memo[s[start:i + 1]] = True
    #                 if wBreak_re(i + 1, end):
    #                     return True
    #         memo[s[start:end]] = False
    #         return False
    #
    #     wordDict = set(wordDict)
    #     memo = {}
    #     return wBreak_re(0, len(s))


# s = "letitgo"
# wordDict = ["let", "go", "itt"]

# s="leetcode"
# wordDict = {"leet", "code"}

# s = "applepenapple"
# wordDict = ["apple", "pen"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

obj = Solution()
# print(obj.wordBreak1(s, wordDict))



'''
# Soltion 1
        def wB(start):

            if start == lenS:
                return True
            if start in memo:
                return memo[start]

            for i in range(start,lenS):
                if s[start:i+1] in wordDict:
                    if wB(i+1):
                        memo[start] = True
                        return memo[start]
            memo[start] = False
            return memo[start]

        memo = {}
        wordDict = set(wordDict)
        lenS = len(s)
        return wB(0)
# End of Soltion 1
    
    
# # solution 2
#         def wB(start):

#             w = s[start:end]
#             if w in memo:
#                 return memo[w]

#             for i in range(start, end):
#                 if s[start:i+1] in wordDict:
#                     memo[s[start:i+1]] = True
#                     if i == end-1:
#                         return True
#                     if wB(i+1):
#                         return True
#             memo[w] = False
#             return memo[w]

#         memo = {}
#         end = len(s)
#         return wB(0)
# end of solution 2

#         word_bool = [False] * len(s)

#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if (i == 0 or word_bool[i-1]) and s[i:j+1] in wordDict:
#                     word_bool[j] = True

#         # print(word_bool)
#         return word_bool[-1]
    

#         def wordB(start, end):
#             w = s[start:end + 1]
#             if w in memo:
#                 return memo[w]
#             if w in wordDict:
#                 memo[w] = True
#                 return True

#             for i in range(start, end):
#                 if s[start:i + 1] in wordDict:
#                     memo[s[start:i + 1]] = True
#                     if wordB(i + 1, end):
#                         return True

#             memo[s[start:end + 1]] = False
#             return False


#         memo = {}
#         wordDict = set(wordDict)
#         return wordB(0, len(s) - 1)



    
#         def wordB(start, end):
#             w = s[start:end]
#             # print(f"w={w}")
#             if w in memo:
#                 return memo[w]
#             # if w in wordDict:
#             #     memo[w] = True
#             #     return True

#             for i in range(start, end):
#                 if s[start:i + 1] in wordDict:
#                     memo[s[start:i + 1]] = True

#                     if i == end-1: return True
#                     elif wordB(i + 1, end):
#                         return True

#             memo[s[start:end + 1]] = False
#             return False

#         memo = {}
#         wordDict = set(wordDict)
#         return wordB(0, len(s))
'''