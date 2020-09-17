
# 692. Top K Frequent Words

import collections, heapq
class Solution:
    # sort
    # O(nlogn)
    def topKFrequent(self, words, k):

        count = collections.Counter(words)
        # print(count )
        candidates =sorted(count.keys(), key=lambda w:(-count[w], w))
        return candidates[:k]

    # heap
    # O(nlogk) (k <= N)
    def topKFrequent2(self, words, k):

        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        print(f"count={count}, heap={heap}")
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

words=["i", "love", "leetcode", "i", "love", "coding"]
k = 2
words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k=4
obj = Solution()
print(obj.topKFrequent2(words, k))