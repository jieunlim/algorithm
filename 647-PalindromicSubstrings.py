
# 647. Palindromic Substrings

# O(N^2)
# O(1)
class Solution:
    def countSubstrings(self, s):
        def countPalindrome(left, right):

            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt

        rCnt = 0
        for i in range(len(s)):
            rCnt += countPalindrome(i, i)
            rCnt += countPalindrome(i, i+1)

        return rCnt


    def cntPaliSubstring3(self, S):

        N = len(S)
        ans = 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            print(f"left={left}, right={right}")
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
                print(f"left={left}, right={right}, ans={ans}")
        return ans


    def countSubstrings1(self, s):
        if not s:
            return 0

        n = len(s)
        table = [[False for x in range(n)] for y in range(n)]
        count = 0

        # Every isolated char is a palindrome
        for i in range(n):
            table[i][i] = True
            count += 1

        print(f"table={table}, count={count}")
        # Check for a window of size 2
        for i in range(n-1):
            print(f"i={i}")
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1
                print(f"table={table}, count={count}")

        # Check windows of size 3 and more
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                print(f"** k={k}, i={i}, j={j}")
                if table[i+1][j-1] and s[i] == s[j]:
                    table[i][j] = True
                    count += 1
                    print(f"table={table}, count={count}")

        return count

    # Algorithm: DP, optimized
    # Time: O(n^2)
    # Space: O(n)
    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [True, ]  # dp[i] is True iff the substring of length i is palindromic, so dp[0] is always True
        for i in reversed(range(n)):
            next_dp = [True, ]
            next_dp.append(True)
            count += 1
            print(f"* i={i}, next_dp={next_dp}, count={count}")
            for j in range(i + 1, n):
                # substring length: j - i + 1 (>= 2)
                print(f"j={j}")
                if s[i] == s[j] and dp[j - i - 1]:
                    next_dp.append(True)
                    count += 1
                else:
                    next_dp.append(False)
                print(f"next_dp = {next_dp}, count={count}")
            dp = next_dp
            print(f" dp={dp}")

        return count

s="abba"
s="aaa"
obj=Solution()
print(obj.countSubstrings(s))

# for (int l = 1; l < n; ++l) {
#    for (int i = 0; i < n-l; ++i) {
#        int j = i + l;
#        if (s[i] == s[j] && dp[i+1][j-1] == j-i-1) {
#            dp[i][j] = dp[i+1][j-1] + 2;
#        } else {
#            dp[i][j] = 0;
#        }
#    }
# }


