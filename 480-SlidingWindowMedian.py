# 480. Sliding Window Median

#  O(N*K)  - 1) inserting/removeing numbers from heaps of size 'K' - O(logK)
#  2) removing element - linear serach O(K)
# Space O(K) - storing all the numbers within the sliding window

import heapq
class Solution:
    def slidingWindowMedian(self, nums, k):
        if not nums: return []

        result = [0.0 for _ in range(len(nums)-k+1)]
        minHeap, maxHeap = [], []
        for i in range(len(nums)):
            # O(logK)
            if not maxHeap or -maxHeap[0] >= nums[i]:
                heapq.heappush(maxHeap, -nums[i])
            else:
                heapq.heappush(minHeap, nums[i])

            # O(logK)
            self.rebalance(maxHeap, minHeap)

            if i - k + 1 >= 0:
                if len(maxHeap) == len(minHeap):
                    result[i-k+1] = (-maxHeap[0]+minHeap[0])/2
                else:
                    result[i - k + 1] = -maxHeap[0]

                rNum = nums[i-k+1]
                print(f"maxHeap={maxHeap}, minHEap={minHeap}, rNum={rNum}")
                if -maxHeap[0] >= rNum:
                    print(f"maxHeap={maxHeap}")
                    self.remove(maxHeap, -rNum)
                else:
                    print(f"-maxHeap[0]={-maxHeap[0]}, minHeap={minHeap}")
                    # O(K) - linear search
                    self.remove(minHeap, rNum)
                # O(logK)
                self.rebalance(maxHeap, minHeap)

        return result

    def remove(self, heap, rNum):
        print(f"heap={heap}, rNum={rNum}")
        # idx = heap.index(rNum)
        heap.remove(rNum)
        heapq.heapify(heap)

    def rebalance(self, maxHeap, minHeap):

        if len(maxHeap) > len(minHeap) + 1:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        elif len(maxHeap) < len(minHeap):
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))

nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums=[2147483647,1,2,3,4,5,6,7,2147483647]
k=2
obj = Solution()
print(obj.slidingWindowMedian(nums, k))



# 295. Find Median from Data Stream



from heapq import *
import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
                # add the median to the the result array
                if len(self.maxHeap) == len(self.minHeap):
                    # we have even number of elements, take the average of middle two elements
                    result[i - k + 1] = -self.maxHeap[0] / \
                                        2.0 + self.minHeap[0] / 2.0
                else:  # because max-heap will have one more element than the min-heap
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                print(f"i - k + 1={i - k + 1}, result={result}")
                # remove the the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)

                self.rebalance_heaps()

        return result

    # removes an element from the heap keeping the heap property
    def remove(self, heap, element):
        ind = heap.index(element)  # find the element
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


    def rebalance_heaps(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


# main()



