# 1296. Divide Array in Sets of K Consecutive Numbers
import collections

def isPossibleDivide2(nums, k):
    ctr = collections.Counter(nums)
    for num in nums:
        start = num
        while ctr[start - 1]:
            start -= 1
        while start <= num:
            while ctr[start]:
                for victim in range(start, start + k):
                    if not ctr[victim]:
                        return False
                    ctr[victim] -= 1
            start += 1
    return True

def isPossibleDivide(nums, k):

    if len(nums) % k != 0:
        return False

    counter = collections.Counter(nums)
    print(counter)
    keys = sorted(counter.keys())

    cnt = len(nums) // k

    for n in keys:
        if counter[n] > 0:
            maxCnt = counter[n]
            for i in range(n, n+k):
                print(f"i={i}, counter={counter}, maxCnt={maxCnt}")
                if counter[i] < maxCnt:
                    return False
                counter[i] -= maxCnt
                print(f"    counter={counter}, maxCnt={maxCnt}")
    return True

def isPossibleDivide22(nums, k):
    count = collections.Counter(nums)
    keys = sorted(count.keys())
    print(f"count={count}, keys={keys}")
    for n in keys:
        print(f"n={n}")
        if count[n] > 0:
            minus = count[n]
            for i in range(n, n + k):
                print(f"  i={i}, minus={minus}")
                if count[i] < minus:
                    return False
                count[i] -= minus
                print(f"   count={count}")
    return True

nums = [1,2,2,3]
k = 2
print(isPossibleDivide(nums, k))