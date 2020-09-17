
# 252. Meeting Rooms
# O(nlgn) for sorting then O(n), space O(1)
def canAttendMeetings(intervals):
    # intervals.sort(key=lambda x:x[0])
    intervals = sorted(intervals, key=lambda x:x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
print(canAttendMeetings(intervals))