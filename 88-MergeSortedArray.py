
# 88. Merge Sorted Array

# time O(m+n), space O(1)
class Solution:
    def mergeSort(self, num1, m, num2, n):

        i , j = m-1, n-1
        idx = m+n-1

        while i >= 0 and j >= 0:
            if num1[i] > num2[j]:
                num1[idx] = num1[i]
                i -= 1
            else:
                num1[idx] = num2[j]
                j -= 1
            idx -= 1

        print(f"j={j}, num1={num1}, {num1[:j+1]}, {num2[:j+1]}")
        # add missing elements from nums2
        num1[:j+1] = num2[:j+1]

    def mergeSort2(self, num1, m, num2, n):
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # while i >= 0:
        #     nums1[k] = nums1[i]
        #     i -= 1
        #     k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    def mergeSortedArray(nums1, m, nums2, n):

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        while m== 0 and n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1

num1 = [1,2,3,0,0,0,0]
m = 3
num2 = [2,5,6]
n = 3

num1 = [0]
m = 0
num2 = [1]
n = 1
# [0]

# num1 = [1,0,0,0]
# m = 1
# num2 = [1,2,3]
# n = 3
num1 = [4,0,0,0]
m = 1
num2 = [1,2,3]
n = 3

nums1=[1]
m=1
nums2=[]
n=0

nums1=[2,0]
m=1
nums2=[1]
n=1
obj = Solution()
obj.mergeSort(num1, m, num2, n)
print(num1)