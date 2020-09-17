# 169. Majority Element

# Hash
# O(n), O(n)
def majorityElement(nums):
    from collections import defaultdict
    dict = defaultdict(int)

    for n in nums:
        dict[n] += 1

    for n in dict:
        if dict[n] > len(nums)//2:
            return n

    return -1

# Hash
# O(n), O(n)
def majorityElement2(nums):
    from collections import Counter
    cnt = Counter(nums)
    print(f"cnt={cnt} ")
    return max(cnt.keys(), key=cnt.get)

# Sort
# O(nlgn), O(1)
def majorityElement3(nums):
    nums.sort()
    print(f"len(nums) // 2={len(nums) // 2}")
    return nums[len(nums) // 2]

nums = [3,2,3]
# nums=[1.,2,3,4,5,5,5,5]
print(majorityElement3(nums))
