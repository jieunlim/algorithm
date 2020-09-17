# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/discuss/93927/python-O(n2)-solution-with-hashtable
# O(n^2)
import collections
def fourSumCount(A, B, C,D):
    hashmap = collections.defaultdict(int)
    for a in A:
        for b in B:
            hashmap[a + b] += 1
    count = 0
    for c in C:
        for d in D:
            count += hashmap[-c - d]
    return count

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A,B,C,D))