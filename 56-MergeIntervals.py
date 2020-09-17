
# 56. Merge Intervals

# 1) To ensure a.start <= b.start, sort the intervals on the start time
# 2) if a overlap b, a.end >= b.start, we need to merge then into a new interval.
#  c.start = a.start
#  c.end = max(a.end, b.end)

# N - total number of intervals,
# iterating the intervals only once which will take O(n), O(nlogn) but since we need to sort the intervals.
# so, time complexity is O(nlogn)
# space complexity: O(n), Collections.sort() either uses Merge sort or Timsort.

# Sort, O(nlgn), space O(1) (or O(N) ofr sort intervals)

# https://leetcode.com/problems/merge-intervals/discuss/21332/Short-python-solution
import collections
class Solution:
    def merge(self, intervals):

        if len(intervals) == 0: return []

        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        print(f"intervals={intervals}, res ={res}")
        for n in intervals[1:]:
            print(f"n={n}, {n[0]}, {n[-1]}, {res[-1][-1]}")
            if n[0] <= res[-1][-1]:
                res[-1][-1] = max(n[-1], res[-1][-1])
            else:
                res.append(n)
            print(f"res={res}")
        return res

intervals = [[1,3],[2,6],[8,10]]
intervals = [[1,2],[3,5]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
intervals = [[1,3],[2,6],[8,10],[15,18]]
obj = Solution()
print(obj.merge(intervals))

# 57. Insert Interval
# 252. Meeting Rooms

# 253. Meeting Rooms II
# 495. Teemo Attacking
# 616. Add Bold Tag in String
# 715. Range Module
# 759. Employee Free Time
# 763. Partition Labels
# 986. Interval List Intersections
# Question: How do you add intervals and merge them for a large stream of intervals? (Facebook Follow-up Question)
# Inspired by https://leetcode.com/problems/merge-intervals/discuss/21452/Share-my-interval-tree-solution-no-sorting
# We need to have two functions for the tree (add interval and query tree).