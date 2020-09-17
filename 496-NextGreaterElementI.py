
# 496. Next Greater Element I
def nextGreaterElement(nums1, nums2):
    res = [-1]*len(nums1)
    for i1, n1 in enumerate(nums1):
        found = False
        for n2 in nums2:
            if n1 == n2:
                found = True
            if found and n1 < n2:
                res[i1] = n2
                break
    return res


def nextGreaterElement2(nums1, nums2):
    dict = {}
    stack = []
    res = []

    for x in nums2:
        while stack and stack[-1] < x:
            dict[stack.pop()] = x
        stack.append(x)

    for x in nums1:
        res.append(dict.get(x, -1))

    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement2(nums1, nums2))