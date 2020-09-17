
# 44. Wildcard Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # 'abcc'
        # 'a*c'
        si, pi, tmpS, star = 0, 0, 0, -1

        while si < len(s):
            if pi < len(p) and p[pi] in ['?', s[si]]:
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == '*':
                star = pi
                tmpS = si
                pi += 1
            elif star != -1:
                pi = star + 1
                tmpS += 1
                si = tmpS
            else:
                return False

        while pi < len(p) and p[pi] == '*':
            pi += 1

        return pi == len(p)


# recursion with memoization
# DP iteration time O(mn), space O(mn)
# backtracking


class Solution:
    def isMatch2(self, s, p):
        print(f"s={s}, p={p}")
        sLen, pLen = len(s), len(p)
        sIdx = pIdx = match = 0
        starIdx = -1

        while sIdx < sLen:
            print(f"sIdx={sIdx}, pIdx={pIdx}, starIdx={starIdx}, match={match}")
            if pIdx < pLen and p[pIdx] in ['?', s[sIdx]]:
                sIdx += 1
                pIdx += 1
            elif pIdx < pLen and p[pIdx] == '*':
                starIdx = pIdx
                match = sIdx
                pIdx += 1
                print(f"match={match}")
            elif starIdx != -1:
                pIdx = starIdx + 1
                match += 1
                sIdx = match
            else:
                return False

        print(f"pIdx={pIdx}")
        while pIdx < pLen and p[pIdx] == '*':
            pIdx += 1

        return pIdx == pLen

    # Approach 3 - backtracking
    # time O(min(S, P)), space O(1)
    def isMatch22(self, s, p):
        print(f"s={s}, p={p}")
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:

            print(f"s_idx={s_idx}, s_len={s_len}")
            # If the pattern caracter = string character
            # or pattern character = '?'
            print(f"p_idx={p_idx}, p_len={p_len}, p={p}, s={s}")
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                s_idx += 1
                p_idx += 1
                print(f"s_idx={s_idx}, p_idx={p_idx}")
            # If pattern character = '*'
            elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
                print(f"star_idx={star_idx}, s_tmp_idx={s_tmp_idx}, p_idx={p_idx}")
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                print(f"star_idx={star_idx}")
                return False
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                print(f"else")
                # Backtrack: check the situation
                # when '*' matches one more character
                p_idx = star_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
                print(f"    p_idx={p_idx},s_idx={s_idx}, s_tmp_idx={s_tmp_idx}")

        # The remaining characters in the pattern should all be '*' characters
        print(f"return '{p[p_idx:]}', {all([])}, {all([1==1, 2==2])}")
        return all(x == '*' for x in p[p_idx:])

    # DP
    # https: // leetcode.com / problems / wildcard - matching / discuss / 17845 / Python - DP - solution
    def isMatch(self, s, p):

        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False] * length

        print(f"dp={dp}, s={s}, p={p}")
        for i in p:
            print(f"i={i}")
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
                    print(f" [for1] n={n}, s[n]={s[n]} dp={dp}")
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
                    print(f" [for2] n={n} dp={dp}")
            dp[0] = dp[0] and i == '*'
            print(f"dp={dp}")
        return dp[-1]

    def isMatch_DP(self, s, p):
        print(f"s={s}, p={p}")
        dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        print(f"dp={dp}")

        for j in range(1, len(p) + 1):
            print(f"j={j}, p[j-1]={p[j-1]}")
            if p[j - 1] != '*':
                break
            dp[0][j] = True
        print(f"dp={dp}\n")

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                print(f"i={i}, p[j-1]={p[j-1]}, s[i - 1]={s[i - 1]} dp={dp}")
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]
                    print(f"if - dp={dp}")
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                    print(f"else - dp={dp}")
        return dp[-1][-1]

    def isMatch3(self, s, p):
        s_cur = 0;
        p_cur = 0;
        match = 0;
        star = -1;
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur = p_cur + 1
            elif (star != -1):
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False

        while p_cur < len(p) and p[p_cur] == '*':
            p_cur = p_cur + 1

        if p_cur == len(p):
            return True
        else:
            return False



s = "cb"
p = "?a"
# s="aa"
# p="*"
s = "acdcb"
p = "a*c?b"
#
# s="adcbdk"
# p="*a*b?k"

# s = "aa"
# p = "a"
obj = Solution()
print(obj.isMatch2(s, p))




# Recursion with memoization
class Solution2:
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0], ]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    def helper(self, s, p):
        print(f"s={s}, p={p}, self.dp={self.dp}")
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            print(f" AAA  s={s}, p={p}")
            dp[(s, p)] = self.helper(s[1:], p[1:])
            print(f" after AAA  s={s}, p={p}")
        elif p[0] == '*':
            print(f" BBB  s={s}, p={p}")
            dp[(s, p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
            print(f" after BBB  s={s}, p={p}")
        else:
            dp[(s, p)] = False
            print(f" CCC dp[(s, p)]={dp[(s, p)]}, s={s}, p={p}")

        print(f"return dp[(s, p)] = {dp[(s, p)]}, s={s}, p={p}")
        return dp[(s, p)]

    def isMatch(self, s, p):
        p = self.remove_duplicate_stars(p)
        # memorization hashmap to be used during the recursion
        self.dp = {}
        print(f"p={p}")
        return self.helper(s, p)

