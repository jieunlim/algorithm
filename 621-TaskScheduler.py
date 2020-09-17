# 621. Task Scheduler

# time O(N), N is a number of tasks to excute, Array charMap is 26, constant time
# space O(1)
def leastInterval(tasks, n):
    charMap = [ 0 for _ in range(26)]
    for c in tasks:
        charMap[ord(c)-ord('A')] += 1

    charMap.sort()

    maxVal = charMap[25] - 1
    idleSlots = maxVal * n

    for i in range(24, -1, -1):
        idleSlots -= min(charMap[i], maxVal)

    return idleSlots + len(tasks) if idleSlots > 0 else len(tasks)

tasks = ['A','A','B']
n = 2
print(leastInterval(tasks, n))


#
# import collections
# def leastInterval(tasks, N):
#     task_counts = collections.Counter(tasks).values()
#     M = max(task_counts)
#     Mct = task_counts.count(M)
#     return max(len(tasks), (M - 1) * (N + 1) + Mct)

import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        c = collections.defaultdict(int)
        print(f"c={c}")

        for task in tasks:
            print(f"task={task}")
            c[task] += 1
            print(f"c[task]={c[task]}, c={c}")

        # k = max([c[i] for i in c])
        k = max(c.values())
        print(f"k={k} ")
        p = 0
        for i in c:
            print(f"i={i}, c[i]={c[i]}")
            if c[i] == k:
                p += 1
                print(f"p={p}")

        print(f"len(tasks)={len(tasks)}, tasks={tasks}")
        print(f"k={k}, n={n}, p={p}, (k-1)*(n+1) + p={(k-1)*(n+1) + p}")
        return max(len(tasks), (k-1)*(n+1) + p)

# tasks = ["A","A","A","B","C","B"]
# n = 2
# obj = Solution()
# print(obj.leastInterval(tasks, n))


# https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
from heapq import heappush, heappop
from collections import Counter


# Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution2:
    def inverse(self, num):
        return -1 * num

    def leastInterval(self, tasks, n: int) -> int:
        # What are the inputs here
        #   - tasks - a list of strings the represent information we're processing
        #   - n - the time between tasks of the exact same time. This would leave us room to process other tasks
        # we asking for here?
        #   - We're looking for an int as an output. That's because we're returning a count
        #   - We're looking for the minimum number of intervals that we're going to use for the problem

        # How I think we're going to solve the problem
        # 1. We process the most important tasks often
        #   - That's because we want to process everything quickly, and processing it quickly means processing the most frequent tasks immediately after the cooldown time is over is necessary.
        # 2. Determine my interval
        #   - I want to be able to determine what step I'm at
        # 3. Create a dict of counts since I last processed my task

        # Task map to store if we've seen the item before
        task_count = Counter(tasks)
        current_time = 0
        current_heap = []

        print(f"task_count={task_count}")
        # Sorting from least to greatest inside of the heap current_heap
        for k, v in task_count.items():
            print(f"k={k}, v={v}, current_heap={current_heap}")
            heappush(current_heap,
                     (self.inverse(v), k))  # Pushes item from least to greatest (hence the negative values)

        # Here we're running through the entire heap and processing the sorted tasks

        print(f"current_heap={current_heap}")
        while current_heap:  # We're running until this list runs out because we intend to pop elements from it
            index, temp = 0, []
            print(f"index={index}, n={n}")
            while index <= n:
                print(f"* while *")
                current_time += 1  # We're counting the interval time here
                print(f"current_time={current_time}, current_heap={current_heap}")
                if current_heap:
                    timing, taskid = heappop(current_heap)
                    print(f"timing={timing}, taskid={taskid}")
                    # We're checking to see if it's at the end of the overall count.
                    # Remember that it was negative at the beginning
                    if timing != -1:
                        temp.append((timing + 1, taskid))
                        print(f"temp={temp}")
                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                # This will automatically exit out of the overall tasks
                print(f"current_heap={current_heap}, temp={temp}")
                if not current_heap and not temp:
                    print(f"break")
                    break
                else:
                    index += 1
                    print(f"index={index}")
                print(f"** while **")
            # Because we transfered all of the items from the heap to temp, we're transferring them back to know if we should continue
            # heap -> If we're not out of tasks -> temp
            # temp -> Because we're not out -> heap
            for item in temp:
                heappush(current_heap, item)
                print(f"(heappush) current_heap={current_heap}")
            # We only stop if we're out of tasks
            # (Constantly checking the current_heap for if it's empty)
        print(f"return current_time={current_time}")
        return current_time

    def leastInterval2(self, tasks, n):
        curr_time, h = 0, []
        for v in Counter(tasks).values():
            heappush(h, -1 * v)
        print(f"tasks={tasks}, h={h}")
        while h:
            temp = []
            for _ in range(n + 1):
                curr_time += 1
                print(f"curr_time={curr_time}")
                if h:
                    x = heappop(h)
                    print(f"  x={x}")
                    if x != -1:
                        # if current element does not used out this time, so there could be idles
                        # and it cannot be used again in this n+1 space, so removed to temp and add back later
                        # we can add all left idles if no h but have temp, to improve time complexity.
                        temp.append(x + 1)
                        print(f"  temp={temp}")
                if not h and not temp:  # not temp, add idle
                    print(f"  break")
                    break
            for item in temp:
                heappush(h, item)
                print(f"  heappush h={h}")
        print(f"return curr_time={curr_time}")
        return curr_time

    def leastInterval3(self, tasks, n):
        curr_time, h = 0, []
        for k, v in Counter(tasks).items():
            heappush(h, (-1 * v, k))
        print(f"*h={h}")
        while h:
            i, temp = 0, []
            print(f"h={h}, i={i}, temp={temp}, n={n}")
            while i <= n:
                curr_time += 1
                print(f"cur_time={curr_time}, h={h}")
                if h:
                    x, y = heappop(h)
                    print(f" x={x}, y={y}")
                    if x != -1:
                        temp.append((x + 1, y))
                        print(f" temp={temp}")
                if not h and not temp:
                    break
                else:
                    i += 1
                    print(f" i={i}")
            print(f"temp={temp}, h={h}")
            for item in temp:
                heappush(h, item)
                print(f"item={item}, h={h}")

            print(f"i={i}, n={n}, curr_time={curr_time}, x={x}, y={y}, h={h}")
        print(f"curr_time={curr_time}")
        return curr_time

    def leastInterval4(self, tasks, n):

        curr_time, h = 0, []
        for v in collections.Counter(tasks).values():
            heapq.heappush(h, -1*v)
        while h:
            temp = []
            for _ in range(n+1):
                curr_time += 1
                if h:
                    x = heapq.heappop(h)
                    if x != -1:
                    # if current element does not used out this time, so there could be idles
                    # and it cannot be used again in this n+1 space, so removed to temp and add back later
                    # we can add all left idles if no h but have temp, to improve time complexity.
                        temp.append(x+1)
                if not h and not temp:#not temp, add idle
                    break
            for item in temp:
                heapq.heappush(h, item)
        return curr_time

# tasks = ["A","A","A","B","B","B"]
tasks = ["A","A","A","B","C","B"]
n = 2

obj = Solution2()
print(obj.leastInterval4(tasks, n))

# 767. Reorganize String