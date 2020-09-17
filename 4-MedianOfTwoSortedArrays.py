# 4. Median of Two Sorted Arrays
# Solution 1 - THIS IS THE SOLUTION
# time O(log(min(m,n))), space O(1)
# Sorted, Log time ==> binary search
# https://leetcode.com/problems/median-of-two-sorted-arrays/solution/
# https://www.youtube.com/watch?v=LPFhl65R7ww&feature=emb_logo

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        start, end, half = 0, m, (m+n+1)//2

        print(f"  nums1={nums1}, nums2={nums2}, m={m}, n={n}, half={half}")

        while start <= end:
            i = (start+end)//2
            j = half - i
            print(f"i ={i}, j ={j}, nums1[i-1]={nums1[i-1]}, nums1[i]={nums1[i]}, nums2[j-1]={nums2[j-1]}, nums2[j]={nums2[j]}")
            if i < m and nums1[i] < nums2[j-1]:
                start = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                end  = i-1
            else:

                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                print(f"max_of_left={max_of_left}")

                if (m + n) % 2 == 1:
                    print(f"return max_of_left ={max_of_left}")
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                print(f"min_of_right = {min_of_right}")
                print(f"*return {(max_of_left + min_of_right) / 2.0}")
                return (max_of_left + min_of_right) / 2.0


# nums1 = [3, 10, 13, 15, 18, 20, 21, 24, 30, 50]
# nums2 = [1, 2, 4, 6, 8, 9, 11, 12, 16, 32, 59]

nums1=[1,2,5,7,9,15,20,25,40]
nums2=[3,4,8,12,13,18,21,22,23,25]

obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))



# 280. Wiggle Sort
# 350. Intersection of Two Arrays II
# 1010. Pairs of Songs With Total Durations Divisible by 60

'''
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    print(f"A={A}, B={B}")
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    print(f"m={m}, n={n}, imin={imin}, imax={imax}, half_len={half_len}")
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        print(f"i={i}, j={j}, m={m}")

        if i < m and B[j-1] > A[i]:
            print(f" B[j-1] {B[j-1]} > A[i] {A[i]}")
            # i is too small, must increase it
            imin = i + 1
            print(f"imin={imin}, imax={imax}")
        elif i > 0 and A[i-1] > B[j]:
            print(F", A[i-1] {A[i-1]} > B[j] {B[j]} ")
            # i is too big, must decrease it
            imax = i - 1
            print(f"imax={imax} "
                  f", imin={imin}")
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            print(f"max_of_left={max_of_left}")

            if (m + n) % 2 == 1:
                print(f"return max_of_left ={max_of_left}")
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            print(f"min_of_right = {min_of_right}")
            print(f"*return {(max_of_left + min_of_right) / 2.0}")
            return (max_of_left + min_of_right) / 2.0

class Solution:
    # Discussion Solution
    # https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
    def findMedianSortedArrays2(self, nums1, nums2) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        # when total length is odd, the median is the middle
        if (len1 + len2) % 2 != 0:
            print(f"# (len1 + len2) // 2 ={(len1 + len2) // 2}")
            return self.get_kth(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
        else:
            # when total length is even, the median is the average of the middle 2
            print(f"### {(len1 + len2) // 2} ")
            middle1 = self.get_kth(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
            print(f"### {(len1 + len2) // 2 - 1} ")
            middle2 = self.get_kth(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2 - 1)
            print(f"middle1={middle1}, middle2={middle2}")
            return (middle1 + middle2) / 2

    # if the sum of index is smaller than half(k), search right side of the smaller value array. start(smaller) = m+1
    # is bigger than half k, search left side of the bigger value array. end(bigger) = m-1
    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        print(f"**nums1={nums1}, nums2={nums2}, start1={start1}, end1={end1}, start2={start2}, end2={end2}, k={k}")
        if start1 > end1:
            return nums2[k - start1]
        if start2 > end2:
            return nums1[k - start2]

        middle1 = (start1 + end1) // 2
        middle2 = (start2 + end2) // 2
        middle1_value = nums1[middle1]
        middle2_value = nums2[middle2]

        print(f"middle1={middle1}, middle2={middle2}, middle1_value={middle1_value}, middle2_value={middle2_value}")

        # if sum of two median's indicies is smaller than k
        if (middle1 + middle2) < k:
            print(f"1 (middle1 + middle2) < k")
            # if nums1 median value bigger than nums2, then nums2's first half will always be positioned before nums1's median, so k would never be in num2's first half
            if middle1_value > middle2_value:
                print(f"    1-1 middle1_value > middle2_value")
                return self.get_kth(nums1, nums2, start1, end1, middle2 + 1, end2, k)
            else:
                print(f"    1-2 not middle1_value > middle2_value")
                return self.get_kth(nums1, nums2, middle1 + 1, end1, start2, end2, k)
        # if sum of two median's indicies is bigger than k
        else:
            print(f"2 else (middle1 + middle2) < k")
            # if nums1 median value bigger than nums2, then nums2's first half would be merged before nums1's first half, thus k always come before nums1's median, then nums1's second half would never include k
            if middle1_value > middle2_value:
                print(f"    2-1 middle1_value > middle2_value")
                return self.get_kth(nums1, nums2, start1, middle1 - 1, start2, end2, k)
            else:
                print(f"    2-2 not middle1_value > middle2_value")
                return self.get_kth(nums1, nums2, start1, end1, start2, middle2 - 1, k)


nums1 = [1, 3]
nums2 = [2]

nums1 = [3, 10, 13, 15, 18, 20, 21, 24, 30, 50]
nums2 = [1, 2, 4, 6, 8, 9, 11, 12,16, 32, 59]

# nums1=[4,8,9, 10]
# nums2=[2,3,6, 7]
# print(median(nums1, nums2))
obj = Solution()
# print(obj.findMedianSortedArrays(nums1, nums2))
print(obj.findMedianSortedArrays2(nums1, nums2))


'''

'''
#  Sol
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        print(f"l = {l}")
        if l % 2 == 1:
            print(f"1: {l // 2}")
            return self.kth(A, B, l // 2)
        else:
            print(f"2: {l//2}, {l//2-1}")
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.


    def kth(self, a, b, k):
        if not a:
            print(f"return b[k] = {b[k]}")
            return b[k]
        if not b:
            print(f"return a[k] = {a[k]}")
            return a[k]

        print(f"a={a}, b={b}, k={k}")
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        print(f"ia={ia}, ib={ib}, ma={ma}, mb={mb}")
        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            print(f"ia + ib < k")
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                print(f"ma > mb a={a}, b[ib + 1:]={b[ib + 1:]}, k - ib - 1={k - ib - 1}")
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                print(f"else ma > mb a[ia + 1:]={a[ia + 1:]}, b={b}, k - ia - 1={k - ia - 1}")
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            print(f"else > ")
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                print(f"ma > mb: a[:ia]={a[:ia]}, b={b}, k={k} ")
                return self.kth(a[:ia], b, k)
            else:
                print(f"else ma < mb: a={a}, b[:ib]={b[:ib]}, k={k} ")
                return self.kth(a, b[:ib], k)
'''