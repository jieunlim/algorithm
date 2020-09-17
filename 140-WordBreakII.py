# 140. Word Break II

# https://youtu.be/B6LDeV1ZHa4

# time complexity O(2^(n-1))
# space complexity O(n*2^(n-1))
# https://zhang-xiao-mu.blog/2019/01/14/word-break-i-ii/


# In the worst case the runtime of this algorithm is O(2^n).
# Consider the input "aaaaaa", with wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"].
# Every possible partition is a valid sentence, and there are 2^n-1 such partitions.
# It should be clear that the algorithm cannot do better than this since it generates all valid sentences.
# The cost of iterating over cached results will be exponential, as every possible partition will be cached,
# resulting in the same runtime as regular backtracking.
# Likewise, the space complexity will also be O(2^n) for the same reason - every partition is stored in memory.
#
# Where this algorithm improves on regular backtracking is in a case like this: "aaaaab",
# with wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaa"],
# i.e. the worst case scenario for Word Break I, where no partition is valid due to the last letter 'b'.
# In this case there are no cached results, and the runtime improves from O(2^n) to O(n^2).


def wordBreakII(s, wordDict):

    def helper(idx):
        print(f"idx={idx}")
        if idx in memo:
            print(f" *return memo={memo}")
            return memo[idx]

        res = []
        for j in range(idx, len(s)):
            subStr = s[idx:j+1]
            if subStr in wordDict:
                print(f"  subStr={subStr}")
                if j+1 == len(s):
                    res.append(subStr)
                else:
                    r = helper(j+1)
                    for each in r:
                        res.append(" ".join([subStr, each]))
                        print(f"  each={each}, idx={idx}, subStr={subStr}, res={res}")

        memo[idx] = res
        print(f"return memo={memo}, idx={idx}")
        return memo[idx]

    memo={}
    return helper(0)

s = "aaaaaa"
wordDict=['a','aa','aaa','aaaa','aaaaa','aaaaaa']
rtn = wordBreakII(s, wordDict)
print(rtn)
print(len(rtn))  #2^(n-1)

# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# wordDict=['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa','aaaaaaaaa','aaaaaaaaaa']
# print(wordBreakII(s, wordDict))

# 0123 45678 9   12
# pine apple pen apple
#                 12: apple
#             9: pen apple
#         4: apple pen apple, applepen apple
# pine apple pen apple, pine applepen apple, pineapple pen apple



def wordBreak(s, wordDict):

    N = len(s)
    boolDp = [ False for _ in range(N+1)]
    boolDp[0] = True
    for i in range(N):
        for j in range(i+1, N+1):
            if boolDp[i] and s[i:j] in wordDict:
                print(s[i:j])
                boolDp[j] = True
    print(f"boolDp={boolDp}")
    if not boolDp[-1]: return []

    dp = [[] for _ in range(N+1)]
    dp[0] = [""]
    for i in range(N):
        for j in range(i+1, N+1):
            if s[i:j] in wordDict:
                print(f"*s[i:j]={s[i:j]}, i={i}")
                for each in dp[i]:
                    if i == 0:
                        resStr = s[i:j]
                    else:
                        resStr = each + " " + s[i:j]
                    dp[j].append(resStr)

    print(f"dp={dp}")
    return [s for s in dp[-1]]


# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# print(wordBreak(s, wordDict))





class Solution:
    # solution 1
    def wordBreakII_1(self, s, wordDict):

        def helper(start):
            if start in memo:
                return memo[start]
            res = []
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    if i+1 == len(s):
                        res.append(s[start:i+1])
                    else:
                        rtn = helper(i+1)
                        for each in rtn:
                            res.append(' '.join([s[start:i+1], each]))

            memo[start] = res
            return memo[start]

        memo = {}
        return helper(0)

    # solution 2 - better (using shortest and longest length of wordDict)
    def wordBreakII(self, s, wordDict):

        def helper(s):
            if s in memo:
                return memo[s]
            res = []
            for i in range(shortest, min(longest, len(s)) + 1):
                if s[:i] in wordDict:
                    if i == len(s):
                        res.append(s[:i])
                    else:
                        remain = helper(s[i:])
                        for each in remain:
                            res.append(' '.join([s[:i], each]))
            memo[s] = res
            return memo[s]

        if not s or not wordDict: return
        shortest = min(map(len, wordDict))
        longest = max(map(len, wordDict))
        memo = {}
        return helper(s)

s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat", "ta"]
s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

obj = Solution()
# print(obj.wordBreakII_1(s, wordDict))




########################################################################################

class Solution10:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return
        wordDict = set(wordDict)
        longest = max(map(len, wordDict))
        shortest = min(map(len, wordDict))
        m = len(s)
        memo = {}
        print(f"longest={longest}, shortest={shortest}, m={m}, s={s}")

        def dfs(s):
            print(f"s={s}")
            if s in memo:
                return memo[s]
            res = []
            for i in range(shortest, min(longest, len(s))+1):
                print(f"s[:i]={s[:i]}, i={i}")
                if s[:i] in wordDict:
                    if i == len(s):
                        res.append(s[:i])
                        print(f"res={res}")
                    else:
                        remain = dfs(s[i:])
                        print(f"remain = {remain}, i={i}, s[i:] = {s[i:]}")
                        for each in remain:
                            # res.append(s[:i]+' '+each)
                            res.append(' '.join([s[:i], each]))
                            print(f"each={each}, res={res}")
            memo[s] = res
            return res
        return dfs(s)

s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat", "ta"]
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog", "anddog", "atsanddog"]
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
obj = Solution()
# print(obj.wordBreak(s, wordDict))


class Solution2:
    def wordBreak(self, s, wordDict):
        from collections import defaultdict
        memo = defaultdict(list)

        for j in range(1, len(s) + 1):
            for i in range(j-1, -1, -1):
                w = s[i:j]
                print(f"i={i}, j={j}, w={w}")
                if w in wordDict:
                    print(f"  w={w}, memo={memo}")
                    if i == 0:
                        memo[j - 1] += [w]
                    elif i > 0 and i - 1 in memo:
                        memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))
                    print(f"memo={memo}")

        return memo[len(s) - 1]

    # 다시해보기
    def wordBreak2(self, s, wordDict):
        from collections import defaultdict
        memo = defaultdict(list)
        res = []
        tRes = []

        def wB(start):
            print(f"start={start}")
            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                w = s[start:end]
                print(f"w={w}")
                if w in wordDict:
                    tRes.append(w)
                    if end == len(s):
                        res.append(tRes)
                    elif not wB(end):
                        tRes.pop()
            memo[start] = res
            print(f"res={res}")
            return False

        return wB(0)

# s = "atsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog", "anddog", "atsanddog"]
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
# s="a"
# wordDict = ["a"]
# s="aaaaaaa"
# wordDict = ["aaaa","aa"]
# s="aaaaaaaaaaaaaaaaaaa"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

obj = Solution2()
# print(obj.wordBreak2(s, wordDict))



# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# 31 / 39 test cases passed.


class Solution3:
    # 140. Word Break II

    # def wordBreak2(self, s, wordDict):
    #
    #     from collections import defaultdict
    #
    #     def wBreakRe(start):
    #
    #         end = len(s)
    #         print(f"start={start}, end={end}")
    #         if start in memo:
    #             print(f"return memo {memo[start]}")
    #             return memo[start]
    #
    #         for i in range(start, end):
    #             w = s[start: i + 1]
    #             print(f"for-i={i}, w={w}")
    #             if w in wordDict:
    #
    #                 if i + 1 >= end:
    #                     # rtn = ""
    #                     memo[start] = s[start:i + 1]
    #                     print (f"  memo[start]={memo[start]}, memo={memo}")
    #                     return memo[start]
    #                 else:
    #                     print(f"*call wBreakRe, res={res}, memo={memo}")
    #                     rtn = wBreakRe(i + 1)

    #                     if rtn:
    #                         memo[start] = s[start:i + 1] + " " + rtn
    #                         print(f"  rtn ={rtn}, memo[start]={memo[start]}, memo={memo}")
    #                         return memo[start]
    #
    #                 print(f" rtn={rtn}, res={res} ")
    #
    #         print(f"**return None")
    #         return None
    #
    #     memo = defaultdict(list)
    #     wBreakRe(0)
    #     return memo[0]


# by ms, before memoization, time limit exceeded, 01052020
    def wordBreak2(self, s, wordDict):

        from collections import defaultdict

        def wBreakRe(start):
            print(f"start={start}")

            if start in memo:
                print(f"return memo {memo[start]}")
                return memo[start]

            for i in range(start, end):
                w = s[start: i + 1]
                print(f"for  i={i}, w={w}")
                if w in wordDict:

                    if i + 1 >= end:
                        tmpS.append(w)
                        # memo[start] = w
                        # print (f"  memo={memo} return memo[start]")
                        # return memo[start]
                    else:
                        tmpS.append(w)
                        print(f"*call wBreakRe, memo={memo}, w={w}, tmpS={tmpS}")
                        wBreakRe(i + 1)
                        # tmpS = w + " " + tmpS
                        print(f"w={w}, tmpS = {tmpS}")
                            # memo[start] += list((map(lambda x: w + " " + x, tmpStr)))
                            # print(f"    memo[start]={memo[start]}, memo={memo}")
                        # else:
                            # tmpStr.pop()

        tmpS = []
        end = len(s)
        memo = defaultdict(list)
        wBreakRe(0)
        return memo[0]


    def wordBreak1(self, s, wordDict):
        from collections import defaultdict
        memo = defaultdict(list)
        res = []
        maxWordLen = len(max(wordDict, key=len))

        for j in range(1, len(s) + 1):
            i = j-1
            maxI = j - maxWordLen if j - maxWordLen > 0 else 0
            print(f" maxI={maxI}, maxWordLen={maxWordLen}")
            while i >= maxI:

            # for i in range(j-1, -1, -1):
                w = s[i:j]
                print(f"i={i}, j={j}, w={w}, memo={memo}")
                if w in wordDict:

                    memo[j - 1] += [w]
                    # res += list((map(lambda x: x + " " + w, memo[i - 1])))
                    memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))

                    print(f"  w={w}, memo={memo}, res = {res}")
                    # if i > 0 and i - 1 in memo:
                    #     memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))
                    #
                    #     print(f"memo={memo}")
                    # elif i > 0 and j == len(s):
                    #     memo[j - 1] += []
                    # elif i == 0:
                    #     memo[j - 1] += [w]
                    #     print(f"???? memo={memo}, w={w}")

                i -= 1

        def getResultWord(memo):
            lastWords = memo[len(s) - 1]

            if not lastWords:
                return False

            r = ""
            res = []
            for w in lastWords:
                r += memo[len(s)-len(w)-1]


        return getResultWord(memo)
        # return res

# wordDict = ["cat", "cats", "and", "sand", "dog", "anddog", "catanddog"]
# s = "catsanddog"
s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

# s="a"
# wordDict = ["a"]

# s="aaaaaaa"
# wordDict = ["aaaa","aa"]

# s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# s="aaaaaa"
# wordDict=["a","aa","aaa","aaaa"]

# print(len(s))
# print( len(max(wordDict, key=len)))
# obj = Solution2()
# print(obj.wordBreak2(s, wordDict))



'''
    # 1- by ms, before memoization
    def wordBreak2(self, s, wordDict):

        def wBreakRe(start, end):

            print(f"start={start}, end={end}")

            for i in range(start, end):
                w = s[start: i +1]
                print(f"i={i}, w={w}")
                if w in wordDict:
                    res.append(w)

                    if i == en d -1:
                        fRes.append(" ".join(res))
                        print(f" [end word] i={i} , fRes={fRes}, res={res}")
                        if res: res.pop()
                        return True

                    # next word
                    print(f"*call wBreakRe, res={res}")
                    rtn = wBreakRe( i +1, end)
                    print(f" rtn={rtn}, res={res} ")
                    if res: res.pop()
                    print(f"  popped, res={res} ")


            print(f"**return False")
            return False

        fRes = []
        res = []
        memo = {}
        wBreakRe(0, len(s))
        return fRes
'''

'''
# 2.
# by ms - iteration - need to do better space complexity
# 31 / 39 passed
    # Memory Limit Exceeded
    # s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    def wordBreak(self, s, wordDict):
        from collections import defaultdict
        memo = defaultdict(list)

        maxWordLen = len(max(wordDict, key=len))

        for j in range(1, len(s) + 1):
            i = j-1
            maxI = j - maxWordLen if j - maxWordLen > 0 else 0
            print(f" maxI={maxI}, maxWordLen={maxWordLen}")
            while i >= maxI:

            # for i in range(j-1, -1, -1):
                w = s[i:j]
                print(f"i={i}, j={j}, w={w}, memo={memo}")
                if w in wordDict:
                    print(f"  w={w}, memo={memo}")
                    if i > 0 and i - 1 in memo:
                        memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))

                        print(f"memo={memo}")
                    elif i > 0 and j == len(s):
                        memo[j - 1] += []
                    elif i == 0:
                        memo[j - 1] += [w]
                        print(f"???? memo={memo}, w={w}")

                i -= 1

        return memo[len(s) - 1]
'''

'''
# copied
# https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
# works well!!
def wordBreak_dictFirst(self, s, wordDict):

    # copied, using wordDict at first.
    def helper(s, wordDict):

        print(f"s = {s}, wordDict={wordDict}")
        if s in memo:
            print(f"return memoization s={s}, memo={memo}")
            return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            print(f"  word={word}, len(word) = {len(word)}, len(s)={len(s)}")
            if not s.startswith(word):
                print(f"    s.startswith(word)={s.startswith(word)}")
                continue
            if len(word) == len(s):
                res.append(word)
                print(f"   len(word) == len(s) , res={res}")
            else:
                print(f" * s[len(word):] ={s[len(word):]}")
                resultOfTheRest = helper(s[len(word):], wordDict)
                print(f" ** s[len(word):] ={s[len(word):]}, resultOfTheRest={resultOfTheRest}")
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    print(f"   for item={item}")
                    res.append(item)
                    print(f"        res={res}")
        memo[s] = res
        print(f"res={res}, memo={memo}")
        return res

    memo = {}
    return helper(s, wordDict)
'''

'''
    def wordBreak2(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
'''


# next challenges: 472. Concatenated Words



'''
        # leetcode history copy

        if not s or not wordDict:
            return
        wordDict = set(wordDict)
        longest = max(map(len, wordDict))
        shortest = min(map(len, wordDict))
        m = len(s)
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            res = []
            for i in range(shortest, min(longest, len(s))+1):
                if s[:i] in wordDict:
                    if i == len(s):
                        res.append(s[:i])
                    else:
                        remain = dfs(s[i:])
                        for each in remain:
                            res.append(s[:i]+' '+each)
            memo[s] = res
            return res
        return dfs(s)

#         from collections import defaultdict
#         memo = defaultdict(list)

#         for j in range(1, len(s) + 1):
#             for i in range(j-1, -1, -1):
#                 w = s[i:j]
#                 # print(f"i={i}, j={j}, w={w}")
#                 if w in wordDict:
#                     # print(f"  w={w}, memo={memo}")
#                     if i == 0: 
#                         memo[j - 1] += [w] 
#                     elif i > 0 and i - 1 in memo:
#                         memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))

#                         # print(f"memo={memo}")
#                     # elif i > 0 and j == len(s):
#                     #     print(f"aaaa  memo={memo}")
#                     #     memo[j - 1] += []
#                     #     print(f"bbbb  memo={memo}")
#                     # print(f"memo={memo}")

#         return memo[len(s) - 1]


#         return self.helper(s, wordDict, {})
    
#     def helper(self, s, wordDict, memo):
#         if s in memo: return memo[s]
#         if not s: return []

#         res = []
#         for word in wordDict:
#             if not s.startswith(word):
#                 continue
#             if len(word) == len(s):
#                 res.append(word)
#             else:
#                 resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
#                 for item in resultOfTheRest:
#                     item = word + ' ' + item
#                     res.append(item)
#         memo[s] = res
#         return res
        
        
        
        
# 31 / 39 passed
# Memory Limit Exceeded
# s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# 
#             from collections import defaultdict
#             memo = defaultdict(list)

#             for j in range(1, len(s) + 1):
#                 for i in range(j-1, -1, -1):
#                     w = s[i:j]
#                     # print(f"i={i}, j={j}, w={w}, memo={memo}")
#                     if w in wordDict:
#                         # print(f"  w={w}, memo={memo}")
#                         if i > 0 and i - 1 in memo:
#                             memo[j - 1] += list((map(lambda x: x + " " + w, memo[i - 1])))

#                             # print(f"memo={memo}")
#                         elif i > 0 and j == len(s):
#                             memo[j - 1] += []
#                         elif i == 0:
#                             memo[j - 1] += [w]

#             return memo[len(s) - 1] 

'''