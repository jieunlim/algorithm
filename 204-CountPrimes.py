# 204. Count Primes
class Solution:
    # O(n)
    # O(n)
    def countPrimes(self, n: int) -> int:

        cnt = 0
        arr = [0 for _ in range(n)]

        for i in range(2, n):

            if arr[i] == 0:
                cnt += 1
                j = 1
                while i * j < n:
                    arr[i * j] = 1
                    j += 1

        return cnt

    # O(n^2)
    # O(1)
    def countPrimes2(self, n: int) -> int:

        cnt = 0
        for i in range(2, n):
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag: cnt += 1

        return cnt
