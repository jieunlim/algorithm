# 523. Continuous Subarray Sum

# O(n)
# O(min(k, n))
def checkSubarraySum(nums: List[int], k: int) -> bool:
    if not nums: return True

    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0:
            return True
    if k == 0:
        return False

    # modDict = {0:-1, 5:0, 1:1, 5:2
    modDict, modK = {0: -1}, 0
    for i, n in enumerate(nums):
        modK = (modK + n) % k
        if modK in modDict:
            if i - modDict[modK] >= 2:
                return True
        else:
            modDict[modK] = i
    return False

# O(n^2)
def checkSubarraySum(nums: List[int], k: int) -> bool:
    if not nums: return True

    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0:
            return True
    if k == 0:
        return False
    # [23, 2, 4, 6, 7]
    # 0, 23, 25, 29, 35, 42
    numSums = [0]
    for i in range(1, len(nums) + 1):
        numSums.append(numSums[i - 1] + nums[i - 1])

    for i in range(len(numSums) - 2):
        for j in range(i + 2, len(numSums)):
            if (numSums[j] - numSums[i]) % k == 0:
                return True
    return False

def checkSubarraySum22(nums, k):

    for i in range(len(nums)-1):
        if nums[i] == 0 and nums[i+1] == 0:
            return True

    if k == 0: return False

    modIdxDic = {0:-1}
    modK = 0

    for i, n in enumerate(nums):
        modK = (modK + n)%k
        if modK in modIdxDic and i - modIdxDic[modK] >= 2:
            return True
        elif modK not in modIdxDic:
            modIdxDic[modK] = i
    return False

def checkSubarraySum11(nums, k):
    def check(nums, k):
        if k < 0:
            k = -k
        L = len(nums)
        if L < 2:
            return False
        if k == 0:
            for i in range(L-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        dic = {0:-1}
        curSum_k = 0
        for i in range(L):
            curSum_k = (curSum_k + nums[i]) % k
            print(f"i={i}, curSum_k={curSum_k}, dic={dic}")
            if curSum_k in dic:
                if i - dic[curSum_k] > 1:
                    return True
            else:
                dic[curSum_k] = i
                print(f"dic[curSum_k]={dic[curSum_k]}")
        return False
    return (check(nums, k))


def checkSubarraySum33(nums, k):
    if k == 0:
        return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))

    mods, cum_sum_mod_k = {0: -1}, 0
    for i, n in enumerate(nums):
        cum_sum_mod_k = (cum_sum_mod_k + n) % k
        print(f"i={i}, cum_sum_mod_k={cum_sum_mod_k}, mods={mods} ")
        if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
            return True
        if cum_sum_mod_k not in mods:
            mods[cum_sum_mod_k] = i
        print(f"   mods={mods}")
    return False



# O(n^2)
def checkSubarraySum44(nums, k):

    if not nums: return True

    for i in range(len(nums)-1):
        if nums[i] == 0 and nums[i+1] == 0:
            return True
    if k == 0:
        return False
    # [23, 25, 29, 35, 42]
    sums = [0]
    for i in range(1, len(nums)+1):
        sums.append(nums[i-1]+sums[i-1])

    print(sums)
    for i in range(len(nums)-1):
        for j in range(i+2, len(nums)+1):
            if (sums[j] - sums[i])%k == 0:
                return True

    return False

# O(n^2)
def checkSubarraySum55(nums: List[int], k: int) -> bool:
    if not nums: return True

    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0:
            return True
    if k == 0:
        return False

    for i in range(len(nums)):
        for j in range(i, len(nums) - 1):
            # print(nums[i:j+2])
            if sum(nums[i:j + 2]) % k == 0: return True
    return False

def checkSubarraySum55(nums, k):

    for i in range(len(nums)-1):
        if nums[i] == 0 and nums[i+1] == 0:
            return True

    if k == 0: return False

    # sums = [0, 23, 25, 29,35,42]
    # nums = [23, 2, 4, 6, 7]

    # nums = [1, 0]  sums=[0, 1, 1]
    sums = [0 for _ in range(len(nums) + 1)]
    for i in range(1, len(nums)+1):
        sums[i] = sums[i-1] + nums[i-1]

    print(sums)
    for i in range(len(nums)-1):
        for j in range(i+2, len(nums)+1):
            if (sums[j] - sums[i])%k == 0:
                return True

    return False

def checkSubarraySum66(nums, k):
    if len(nums) < 2: return False
    length = len(nums)
    sums = [0 for _ in range(length + 1)]
    for i in range(1, length + 1):
        sums[i] = nums[i - 1] + sums[i - 1]

    for i in range(length - 1):
        for j in range(i + 2, length + 1):
            if k != 0:
                if (sums[j] - sums[i]) % k == 0:
                    return True
            elif sums[j] - sums[i] == 0:
                return True
    return False

# sums = [0, 23, 25, 31, 35, 42]

nums=[23,2,6,4,7]
k=6 #T
nums=[23,2,6,4,7]
k=0 #F
# nums = [2,4]
# k=6 #T
# nums=[23,2,6,4,7]
# k=0 #F
# nums=[23,2,6,4,7]
# k=-6 #T
# nums = [0,0]
# k=0 #True
# nums=[0,1,0]
# k=0 #False

# nums=[0]
# k=0 # false;
# nums=[5, 2, 4]
# k=5 # false;
# nums=[0, 0]
# k=100 # true;
# nums=[1,5]
# k=-6 #true;

# nums=[1,0,1,0,1]
# k=4 #F

# nums=[0,0]
# k=-1
# nums=[1,1]
# k=-1
# nums=[0, 0, 1]
# k=100 # true;

# [1,1]
# -1 #T

# [0,1,0]
# -1 #T
print(checkSubarraySum(nums, k))




