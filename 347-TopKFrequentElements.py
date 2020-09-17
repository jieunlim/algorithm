
# 347. Top K Frequent Elements

# 1.using heap
# 2.selection algorithm
# 3.bucket sort
class Solution:

    # TC : O(NlogN) heapify
    # SC: O(N)
    #       O(N) for hash, O(k) for heap
    from collections import Counter
    import heapq
    def topKFrequent(nums, k):

        # O(N) : N - the # of input array (N <= len(nums))
        count = Counter(nums)
        pq = []
        for i in count:
            pq.append((-count[i], i))
        # O(NLogN)
        heapq.heapify(pq)

        print(pq)
        res = []
        # O(klogN)
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
            print(i)

        return res

    def topKFrequent(self, nums, k):
        import collections, heapq
        count = collections.Counter(nums)

        print(f"count={count}")
        return heapq.nlargest(k, count.keys(), key=count.get)

    # O(n) for Counter method + O(nlgn) to build a heap --> O(nlgn)
    # space O(n)
    # https://leetcode.com/problems/top-k-frequent-elements/discuss/177967/Python-or-Heap-%2B-Counter-tm
    def topKFrequent2(self, nums, k):
        from collections import Counter
        from heapq import heappop, heapify

        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]
        heapify(max_heap)
        print(f"max_heap={max_heap}")
        for i in range(k):
            res.append(heappop(max_heap)[1])
        return res


obj = Solution()
nums = [1,1,1,2,2,3,3,3,3]
k = 2
print(obj.topKFrequent2(nums, k))


# 215. Kth Largest Element in an Array
# 25. Reverse Nodes in k-Group
# 24. Swap Nodes in Pairs