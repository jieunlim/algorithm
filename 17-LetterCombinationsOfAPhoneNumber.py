# 17. Letter Combinations of a Phone Number
# https://leetcode.com/tag/backtracking/

# time O(3^N*4^M)
# N is the number of digits in the input that maps to 3 letters(2, 3,4,5,6,8)
# M is the number of digits in the input that maps to 4 letters(7,9)
# space O(3^N*4^M)
class Solution:
    def letterCombinations(self, digits):

        def backTracking(index, path=""):
            if len(path) == len(digits):
                res.append(path)
                return

            for ch in dic[digits[index]]:
                backTracking(index + 1, path + ch)

        if not digits:
            return []

        res = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        backTracking(0)
        return res


    # https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8067/Python-easy-to-understand-backtracking-solution.
    #  DFS - recursion ?
    #  This is just DFS + recursion, there's no backtracking here.
    # To do backtracking, we would need to remove or back out of the current state.
    # But we just keep building strings until we satisfy the base case then return.
    # For a true backtracking solution, we need to abandon some non-optimal cases.

    def letterCombinations2(self, digits):
        def dfs(index, path):
            print(f"index={index}, path={path}, res={res}")
            if len(path) == len(digits):
                res.append(path)
                print(f" return res={res}")
                return

            for ch in dic[digits[index]]:
                print(f"  ch={ch}")
                dfs(index + 1, path + ch)
                print(f"  after dfs ch={ch},  index={index}, path={path}, res={res}")

        if not digits:
            return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        print(f"digits={digits}, dic={dic}")
        dfs(0, "")
        return res

    #
    # def dfs(self, digits, dic, index, path, res):
    #     if len(path) == len(digits):
    #         res.append(path)
    #         return
    #     for i in xrange(index, len(digits)):
    #         for j in dic[digits[i]]:
    #             self.dfs(digits, dic, i + 1, path + j, res)

    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])


        output = []
        if digits:
            backtrack("", digits)
        return output

input="23"
obj = Solution()
print(obj.letterCombinations2(input))


# 17. Letter Combinations of a Phone Number

def letterCombination(digits):

    def helper(path, idx):
        if len(path) == len(digits):
            res.append("".join(path[:]))
            return

        for d in pLetters[digits[idx]] :
            path.append(d)
            helper(path, idx+1)
            path.pop()

    res = []
    pLetters = {'1':['a','b','c'], '2':['d','e','f'], '3':['g','h','i']}
    helper([], 0)
    return res

digits='12'
print(letterCombination(digits))


# 51. N-Queens

