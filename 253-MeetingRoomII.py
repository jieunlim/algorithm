
# 253. Meeting Rooms II
from typing import List
import heapq
class Solution:
    # time O(nlgn), space O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        print(f"intervals={intervals}")
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        print(f"free_rooms = {free_rooms} ")

        # For all the remaining meeting rooms
        for i in intervals[1:]:
            print(f"i={i}")
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
                print(f"   free_rooms={free_rooms}")

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])
            print(f"heappush-{i[1]}, free_rooms={free_rooms}")

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

    # def minMeetingRooms____(self, intervals):
    #     intervals.sort(key=lambda x: x.start)
    #     heap = []  # stores the end time of intervals
    #     for i in intervals:
    #         if heap and i.start >= heap[0]:
    #             # means two intervals can use the same room
    #             heapq.heapreplace(heap, i.end)
    #         else:
    #             # a new room is allocated
    #             heapq.heappush(heap, i.end)
    #     return len(heap)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:

        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        print(f"start_timings={start_timings},end_timings={end_timings}, L={L}")
        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            print(f"start_pointer={start_pointer}, end_pointer={end_pointer}")
            print(f"start_timings[start_pointer]{start_timings[start_pointer]} >= end_timings[end_pointer]{end_timings[end_pointer]}")
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            print(f"used_rooms={used_rooms},end_pointer={end_pointer}")
            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

            print(f"used_rooms={used_rooms},start_pointer={start_pointer}")
        return used_rooms

intervals = [[0, 30],[5, 10],[15, 20]]
obj = Solution()
print(obj.minMeetingRooms(intervals))