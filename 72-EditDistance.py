# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        print(f"m={m}, n={n}, table={table}")
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        print(f"table={table}")
        return table[-1][-1]


# 1. base case: word1 = "" or word2 = "" => return length of other string
# 2. recursive case: word1[0] == word2[0] => recurse on word1[1:] and word2[1:]
# 3. recursive case: word1[0] != word2[0] => recurse by inserting, deleting, or replacing

# time: O(mn), space: O(mn) where m and n are the lengths of word1 and word2, respectively

    def minDistance2(self, word1, word2):
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
                    print(f" insert i={i}, j={j}")
                    insert = 1 + mDistance(i, j + 1)
                    print(f" insert={insert}")
                    print(f" delete i={i}, j={j}")
                    delete = 1 + mDistance(i + 1, j)
                    print(f" delete={delete}")
                    print(f" replace i={i}, j={j}")
                    replace = 1 + mDistance(i + 1, j + 1)
                    print(f" replace={replace}")

                    print(f" ({i}, {j}) insert={insert}, delete={delete}, replace={replace}")
                    ans = min(insert, delete, replace)
                    print(f"   **ans={ans} i={i}, j={j}")

                memo[(i, j)] = ans
            return memo[(i, j)]
        memo = {}
        return mDistance(0,0)

w1="ros"
w2="horse"
# w1="a"
# w2="bac"
# w1 = "intention"
# w2 = "execution"
obj = Solution()
print(obj.minDistance2(w1, w2))