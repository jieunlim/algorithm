# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# https://youtu.be/z6wr9E-Bm1c

class Solution:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    #         h o r s e
    #       0 1 2 3 4 5  w1 = "horse", w2 = ""
    #     r 1 1 2 2 3 4
    #     o 2 2 1 2 3 4
    #     s 3 3 2 2 2 3
    #
    #         r o s
    #       0 1 2 3
    #     h 1 1 2 3
    #     o 2 2 1 2
    #     r 3 2 2 2
    #     s 4 3 3 2
    #     e 5 4 4 3
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        print(f"table={table}")
        for i in range(m + 1):
            table[i][0] = i
        print(f"table={table}")
        for j in range(n + 1):
            table[0][j] = j
        print(f"table={table}")

        print(f"m={m}, n={n}, table={table}")
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                    print(f"smae i={i}, j={j}, - table={table}")
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                    print(f"i={i}, j={j}, table={table}")
        print(f"table={table}")
        return table[-1][-1]

    def minDistance2(self, word1, word2):
        def helper(i, j):
            print(f"i={i}, j={j}")
            if i == 0: return j
            if j == 0: return i

            if (i, j) in memo:
                print(f"return memo[({i}, {j})] = {memo[(i, j)]}")
                return memo[(i, j)]

            s = 0 if word1[i-1] == word2[j-1] else 1
            print(f"insert i-1={i-1}, j={j}")
            insert = helper(i-1, j) + 1
            print(f" insert={insert}, i={i}, j={j}")
            print(f" delete i={i}, j-1={j-1}")
            delete = helper(i, j-1) + 1
            print(f" delete={delete}, i={i}, j={j}")
            print(f"replace i-1={i-1}, j-1={j-1}, s={s}")

            replace = helper(i-1, j-1) + s
            print(f" replace={replace}, i={i}, j={j}")

            memo[(i, j)] = min( insert, delete, replace)
            print(f"memo[({i}, {j})]= {memo[(i, j)]}")
            return memo[(i, j)]

        memo = {}
        return helper(len(word1), len(word2))

    def minDistance22(self, word1: str, word2: str) -> int:
        def helper(i, j):
            if i == 0: return j
            if j == 0: return i

            if (i, j) in memo:
                return memo[(i, j)]

            s = 0 if word1[i - 1] == word2[j - 1] else 1
            memo[(i, j)] = min(helper(i - 1, j) + 1, helper(i, j - 1) + 1, helper(i - 1, j - 1) + s)
            return memo[(i, j)]

        memo = {}
        return helper(len(word1), len(word2))

# 1. base case: word1 = "" or word2 = "" => return length of other string
# 2. recursive case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
# 3. recursive case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing

# time: O(mn), space: O(mn) where m and n are the lengths of word1 and word2, respectively

    def minDistance3(self, word1, word2):
        def mDistance(i, j):
            if i == len(word1) and j == len(word2):
                print(f" return same : 0 ")
                return 0
            if i == len(word1):
                print(f" end i : {len(word2) - j}")
                return len(word2) - j
            if j == len(word2):
                print(f" end j : {len(word1) - i}")
                return len(word1) - i

            print(f"i={i}, j={j}")
            if (i, j) not in memo:
                print(f"{word1[i]}, {word2[j]}")
                if word1[i] == word2[j]:
                    print(f" same char ")
                    ans = mDistance(i + 1, j + 1)
                else:
                    print(f"insert i={i}, j+1={j+1}")
                    insert = 1 + mDistance(i, j + 1)
                    print(f" insert={insert}, i={i}, j={j}")
                    print(f"delete i+1={i+1}, j={j}")
                    delete = 1 + mDistance(i + 1, j)
                    print(f" delete={delete}, i={i}, j={j}")
                    print(f"replace i+1={i+1}, j+1={j+1}")
                    replace = 1 + mDistance(i + 1, j + 1)
                    print(f" replace={replace}, i={i}, j={j}")

                    print(f" ({i}, {j}) insert={insert}, delete={delete}, replace={replace}")
                    ans = min(insert, delete, replace)
                    print(f"   **ans={ans} i={i}, j={j}")

                memo[(i, j)] = ans
            return memo[(i, j)]
        memo = {}
        return mDistance(0,0)

    def minDistance4(self, word1, word2):
        def helper(i, j):
            # if i == len(word1) and j == len(word2): return 0
            if i == len(word1): return len(word2) - j
            if j == len(word2): return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            s = 0 if word1[i] == word2[j] else 1
            memo[(i, j)] = min( helper(i+1, j) + 1, helper(i, j+1) + 1, helper(i+1, j+1) + s)
            return memo[(i, j)]

        memo = {}
        return helper(0, 0)

w1="hors"
w2="ros"
# w1="a"
# w2="bac"
# w1 = "intention"
# w2 = "execution"
w1="horse"
w2="ros"
obj = Solution()
print(obj.minDistance(w1, w2))