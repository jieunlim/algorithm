# 295. Find Median from Data Stream


import heapq

class findMedianFromData:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):

        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        print(f"self.maxHeap[0] = {self.maxHeap[0]}")
        print(f"maxHeap={self.maxHeap}, minHeap={self.minHeap}")
    def findMedian(self):

        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2
        else:
            return -self.maxHeap[0]


obj = findMedianFromData()
obj.addNum(1)
obj.addNum(3)
print(obj.findMedian())
obj.addNum(2)
obj.addNum(5)
obj.addNum(0)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())






# insert O(logN)
# findMedian O(1)
# space O(N)
from heapq import *


class MedianOfAStream:

  maxHeap = []  # containing first half of numbers
  minHeap = []  # containing second half of numbers

  def insert_num(self, num):
    if not self.maxHeap or -self.maxHeap[0] >= num:
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))

  def find_median(self):
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0


# 480. Sliding Window Median


###########################

import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 2)  #O(logN)
print(heap)
print(heap[0])
print(heapq.heappushpop(heap, 4))
print(heap)
# arr=[4,3,1,6,9]
# heapq.heapify(arr)
# print(arr)
# heapq.heappush(arr, 0)
# print(arr)
print("===============")


# Max Heap - median - Min Heap
# O(logn) + O(1) -> O(logn), space O(n)
# https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find

from heapq import *

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        print(f"num = {num}")
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

        print(f"small={self.small}")
        print(f"large={self.large}")

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())



# Binary Insertion Sort
# Todo


# Time Limit Exceeded
# Insertion Sort O(n) + Binary Search O(logn)
# space O(n) - linear space to hold input a container
# MS
class Solution():
    def __init__(self):
        self.nums = []

    def addNum(self, num):

        if len(self.nums) < 1:
            self.nums.append(num)
        else:
            self.nums.append(num)
            i = len(self.nums)-1
            while i > 0 and self.nums[i-1] > self.nums[i]:
                self.nums[i - 1], self.nums[i] = self.nums[i], self.nums[i-1]
                i -= 1
        print(self.nums)

    def findMedian(self):
        size = len(self.nums)

        if size%2 == 0:
            m_val = (self.nums[size//2] + self.nums[(size//2)-1])/2
        else:
            m_val = self.nums[size // 2]

        return m_val

# def findMedian():

obj = Solution()
obj.addNum(4)
obj.addNum(3)
obj.addNum(2)
obj.addNum(1)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
obj.addNum(100)
print(obj.findMedian())
