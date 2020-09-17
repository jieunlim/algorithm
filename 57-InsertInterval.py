# 57. Insert Interval
# time O(N), space O(N) for output
class Solution:

    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':

        if not intervals:
            return [newInterval]
        elif not newInterval:
            return intervals

        res, start, end = [], 0, 1
        i = 0
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        res.append(newInterval)
        return res + intervals[i:]

    def insertInterval2(intervals, newInterval):

        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # N <= AE
        # N-NE - A-AE
        # or overlapping if A <= NE
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        return res + intervals[i:]

    def insertInterval(self, intervals, newInterval):
        # A-AE, N-NE : A.end < N.start : res(A)
        # N-NE, A-AE : A.start > N.end : res(N) + rest of intervals

        # A-B-AE-BE : N = min(start), NE = max(end)
        # A-B-BE-AE
        # B-A-BE-AE
        # B-A-AE-BE

        result = []
        start, end = 0, 1
        for i in range(len(intervals)):
            print(f"i={i}, result={result}")
            if intervals[i][end] < newInterval[start]:
                result.append(intervals[i])
            elif intervals[i][start] > newInterval[end]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval[start] = min(intervals[i][start], newInterval[start])
                newInterval[end] = max(intervals[i][end], newInterval[end])
                print(newInterval)
        result.append(newInterval)
        return result

    def insert(intervals, new_interval):
        merged = []
        i, start, end = 0, 0, 1

        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i][end] < new_interval[start]:
            merged.append(intervals[i])
            i += 1

        print(f"merged={merged}")
        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and intervals[i][start] <= new_interval[end]:
            new_interval[start] = min(intervals[i][start], new_interval[start])
            new_interval[end] = max(intervals[i][end], new_interval[end])
            i += 1

        # insert the new_interval
        merged.append(new_interval)
        print(f"merged={merged}, i={i}")

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged


    def insert2(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        print(f"new_start={new_start}, new_end={new_end}, output={output}")
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            print(f"idx={idx}, n={n}, new_start={new_start} intervals[idx][0]={intervals[idx][0]}")
            output.append(intervals[idx])
            idx += 1

        print(f"output={output}")
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
            print(f"{output[-1][1]} < {new_start}, output={output}")
        # if there is an overlap, merge with the last interval
        else:
            print(f"output[-1][1]={output[-1][1]}, new_end={new_end}")
            output[-1][1] = max(output[-1][1], new_end)

        # add next intervals, merge with newInterval if needed
        while idx < n:
            print(f"idx={idx}, n={n}")
            interval = intervals[idx]
            start, end = interval
            idx += 1
            print(f" interval={interval}, start={start}, end={end}, idx={idx}")
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
            print(f"output={output}")
        return output

    # O(nlgn) time, the same as Merge Intervals
    # https://leetcode.com/problems/merge-intervals/
    def insert1(self, intervals, newInterval):
        print(f"intervals={intervals}, newInterval={newInterval}")
        intervals.append(newInterval)
        print(f"intervals={intervals}")
        res = []
        for i in sorted(intervals, key=lambda x: x[0]):
            print(f"i={i}")
            if res and res[-1][-1] >= i[0]:
                res[-1][-1] = max(res[-1][-1], i[-1])
                print(f"  res[-1][-1]={res[-1][-1]}")
            else:
                res.append(i)
                print(f"  i={i}, res={res}")

        return res



    # O(n) time, not in-place, make use of the
    # property that the intervals were initially sorted
    # according to their start times
    def insert2(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i[-1] < n[0]:
                res.append(i)
            elif n[-1] < i[0]:
                res.append(n)
                return res + intervals[index:]  # can return earlier
            else:  # overlap case
                n[0] = min(n[0], i[0])
                n[-1] = max(n[-1], i[-1])
        res.append(n)
        return res

    def insert3(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
    # def insert(self, intervals, newInterval):

        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i[-1] < n[0]:
                res.append(i)
            elif n[-1] < i[0]:
                res.append(n)
                return res + intervals[index:]  # can return earlier
            else:  # overlap case
                n[0] = min(n[0], i[0])
                n[-1] = max(n[-1], i[-1])
        res.append(n)
        return res


class Solution2(object):
    def insert(self, intervals, newInterval):

        index = len(intervals)
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                index = i
                break

        intervals.insert(index, newInterval)

        ans = []
        for interval in intervals:
            if not ans or interval[0] > ans[-1][-1]:
                ans.append(interval)
            else:
                ans[-1][-1] = max(ans[-1][-1], interval[-1])
        return ans

intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] #non-overlapping intervals, sorted
newInterval = [4,8]


intervals = []
newInterval = [5,7]


intervals = [[1,5]]
newInterval = [6,8]

obj = Solution()
print(obj.insert(intervals, newInterval))