# 829. Consecutive Numbers Sum

# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?
# N=21
# answer: 4  , 다음 4가지 경우-[[1,2,3,4,5,6], [6,7,8],[10,11],[21]]

class Solution:
    # O(n^2),
    # Brute Force - Time Limit Exceeded
    def consecutiveNumbersSum(self, N):
        res = 0
        for i in range(1, N+1):
            sum = 0
            for j in range(i, N+1):
                sum += j
                if sum == N: res += 1
                elif sum > N: break
        return res

    # k로 시작하는 i개의 숫자를 합해서 N이 되는 경우를 찾는다고 하면,
    # N = k + (k+1) + (k+2) + (k+3) + .... + (k + i-1) 인 경우를 찾는 것임.
    # N = k*i + (1 + 2+ 3+ ... + i-1)
    # N = k*i + i*(i-1)/2
    # k*i = N - i*(i-1)/2
    # 결국, 이 문제는 모든 가능한 i 값을 찾는 것임

    def consecutiveNumbersSum2(self, N: int) -> int:
        i, ans = 1, 0
        while N > i * (i - 1) // 2:
            print(f"i={i}")
            print(f"i * (i - 1) // 2={i * (i - 1) // 2}")
            print(f"(N - i * (i - 1) // 2)={(N - i * (i - 1) // 2)}")
            print(f"(N - i * (i - 1) // 2)%i={(N - i * (i - 1) // 2)%i}")
            if (N - i * (i - 1) // 2) % i == 0:
                ans += 1
                print(f"ans={ans}")
            i += 1
        print(f"ans={ans}")
        return ans

    def consecutiveNumbersSum3(self, N):
        cnt=0
        for d in range(1, N+1):
            diff=d*(d-1)//2
            nd = N - diff
            print(f"d = {d}, diff={diff}, nd={nd}")
            if nd<=0:
                print(f"break")
                break
            if nd%d==0:
                cnt+=1
                print(f"cnt={cnt}")
        print(f"cnt={cnt}")
        return cnt

    # odd/even을 나누어서 규칙을 찾음.
    # 연속된 숫자의 이 N되는 연속된 숫자의 갯수를 i라고 하면,
    #   i가 짝수개인 경우 N%i == i//2 이면 성립, 홀수개인 경우는  N%i == 0 이면 성립

    # N = 21 인 경우,
    # i = 1 (한 개의 숫자로 21이 되는 경우는 [21])
    # i = 2 (두 개의 연속된 숫자를 합해서 N=21 값이 되는 경우, [10,11]을 찾기 위한 것)
    #   N = k + (k+1)
    #   2k + 1 이므로 N//2 몫은 10인 k값, 나머지 N%i 가 == i//2 이면 존재(짝수개인 경)
    # i = 3, N = k + (k+1) + (k+2) 이 성립해야 함, ([6,7,8])
    #   N = 3k + (1+2) = 3(k+1) 이므로 나머지 N%i 가 0 이면 존재, 21%3 = 0 이므로 존재.우(홀수개인 경우)
    # i = 4, N = k + (k+1) + (k+2) + (k+3)
    #   N = 4k + (1+2+3) = 4(k+1) + 2 이므로 N%i는 21%4 = 1, i//2 = 2, 같지 않으므로 4개짜리는 없음.
    # i = 5, N = 5k + (1+2+3+4), N = 5(k+2), N%i 가 0 이면 존재, 21%5 = 1, 나머지가 0이 아니므 5개짜리는 없음.
    # i = 6, N = 6k + (1+2+3+4+5), N = 6k + 5*6//2 = 6(k+2) + 3, N%i = 3 (6//2값) 존재, 21%6= 3.
    # i = 7,
    #   위에 나온 식에서 보면 k*i = N - i*(i-1)/2
    #   k = N//i - (i-1)//2
    #   if N//i <= (i-1)//2  --> break (N//i 으로 나오는 값인 몫이, 답이 되는 array의 중간값이므로, 이 값이 갯수의 절반 (i-1)//2 보다 작거나 같으면,
    #   배열 중간값의 양쪽으로 연결되는 값  negative 가 생기므로 더 이상의 갯수는 없음.)

    def consecutiveNumbersSum4(self, N):
        cnt = 1
        print(f"N={N}")
        for i in range(2, N+1):
            v1 = N//i
            v2 = N%i
            print(f"i={i}, v1={v1}, v2={v2}, {i//2}")

            if v1 <= (i-1)//2:
                print(f"{v1} < {i/2}, break")
                break

            if i%2 == 1:    #odd
                if v2 == 0 :# and v1 > (i-1)/2:
                    cnt += 1
                    print(f"(1)cnt={cnt}")
            else:       #even
                if v2 == i//2:
                    cnt += 1
                    print(f"(2)cnt={cnt}, i={i}")

        return cnt
obj = Solution()
N = 21
# N=662711
print(obj.consecutiveNumbersSum3(N))




# https://leetcode.com/problems/consecutive-numbers-sum/discuss/128959/JavaPython-3-5-liners-O(N-0.5)-Math-method-w-explanation-and-analysis.

# N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer; therefore
#
# N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i,
# which implies that as long as N - (i - 1) * i / 2 is k times of i,
# we get a solution corresponding to i; Hence iteration of all possible values of i,
# starting from 1, will cover all cases of the problem.
# Solve the equation i * (i - 1) / 2 = N, we know i ~ N ^ 0.5
# Loop runs at most N ^ 0.5 times, so
# Time O(N^0.5), space O(1)

# https://leetcode.com/problems/consecutive-numbers-sum/discuss/144847/Python-3-~132ms-Series-with-explanation

# java
# public int consecutiveNumbersSum(int N) {
#    int result = 1;
#
#    for (int i=2; i<N; i++) {
#        int v1 = N / i;
#        int v2 = N % i;
#        if (v1 < i/2) break;
#        if (i % 2 == 1) {
#            if (v2 == 0 && v1 > i / 2) result++;
#        } else {
#            if (v2 == i/2) result++;
#        }
#    }
#
#    return result;
# }
#
