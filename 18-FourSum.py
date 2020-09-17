# 18. 4Sum
# time O(N^3)
# space

def fourSum2(nums, target):
    n = len(nums)

    if n < 4:
        return
    elif n == 4:
        if sum(nums) == target:
            # return [sorted(nums)]
            return [nums]
    res = []
    nums.sort()
    print(nums)

    for i in range(n-3):
        print(f"i={i}")
        if target < 4*nums[i] or target > 4*nums[n-1]:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i+1, n-2):
            print(f"j={j}")
            target3 = target - nums[i]
            if target3 < 3 * nums[j] or target3 > 3 * nums[n - 1]:  # **MISSING THIS**
                break

            if j > i+1 and nums[j] == nums[j - 1]:
                continue

            l, r = j + 1, n - 1

            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                print(f"i={i}, j={j}, l={l}, r={r}, total={total}")
                if total == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
                print(f"res={res}")
    return res

nums=[1,1,1,-1,0,2,2,0,1]
target=3
nums=[-1,0,1,2,-1,-4]
target=-1
print(fourSum2(nums, target))


# 84 ms
# https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)

def fourSum(nums, target):
    def findNsum(l, r, target, N, result, results):
        print(f"l={l}, r={r}, target={target}, N={N}, result={result}, results={results}")

        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                print(f"else i={i}")
                if i == l or (i > l and nums[i-1] != nums[i]):
                    print(f" call findNSum ")
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results

# nums = [1, 0, -1, 0, -2, 2] #[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# nums=[0,0,0,0]
# nums=[-3,-2,-1,0,0,1,2,3]
nums=[1,0,-1,0,-2,2]
target=0
# nums=[-1,-5,-5,-3,2,5,0,4]
# target=-7
# print(fourSum(nums, target))
