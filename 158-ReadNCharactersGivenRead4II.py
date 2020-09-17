# 158. Read N Characters Given Read4 II - Call multiple times

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/49601/What-is-the-difference-between-call-once-and-call-multiple-times

# What is the difference between call once and call multiple times?
# Think that you have 4 chars "a, b, c, d" in the file, and you want to call your function twice like this:
#
# read(buf, 1); // should return 'a'
# read(buf, 3); // should return 'b, c, d'
# All the 4 chars will be consumed in the first call.
# So the tricky part of this question is how can you preserve the remaining 'b, c, d' to the second call.

class Solution:
    def read(self, buf: List[str], n: int) -> int:
        # print(f"[start] buf={buf[:n]}, n={n}, queue={self.queue}")
        total = 0
        while total < n:
            if self.queue:
                buf[total] = self.queue.popleft()
                total += 1
                # print(f"total={total}, buf={buf[:n]} queue={self.queue}")
            else:
                tmp_buf = [' '] * 4
                count = read4(tmp_buf)
                # print(f"tmp_buf={tmp_buf}, count={count}")
                if not count:
                    break
                self.queue.extend(tmp_buf[:count])
                # for i in range(count):
                #     self.queue.append(tmp_buf[i])
                # print(f"queue={self.queue}")
        # print(f"[return] buf={buf[:n]}, total={total}, queue={self.queue}")
        # print()
        return total

    def __init__(self):
        self.queue = collections.deque()

# "abcde"
# [1,2,1]

# stdout
# [start] buf=[' '], n=1, queue=deque([])
# tmp_buf=['a', 'b', 'c', 'd'], count=4
# queue=deque(['a', 'b', 'c', 'd'])
# total=1, buf=['a'] queue=deque(['b', 'c', 'd'])
# [return] buf=['a'], total=1, queue=deque(['b', 'c', 'd'])
#
# [start] buf=['a', ' '], n=2, queue=deque(['b', 'c', 'd'])
# total=1, buf=['b', ' '] queue=deque(['c', 'd'])
# total=2, buf=['b', 'c'] queue=deque(['d'])
# [return] buf=['b', 'c'], total=2, queue=deque(['d'])
#
# [start] buf=['b'], n=1, queue=deque(['d'])
# total=1, buf=['d'] queue=deque([])
# [return] buf=['d'], total=1, queue=deque([])

class Solution2:
    def read(self, buf, n):
        print(f"[start] n={n}")
        i = 0
        while i < n:
            buf4 = [''] * 4
            _ = read4(buf4)
            self.queue.extend(buf4)
            count = min(len(self.queue), n - i)
            print(f"buf4={buf4}, self.queue={self.queue}, count={count}")
            if not count:
                break
            buf[i:] = [self.queue.popleft() for _ in range(count)]
            i += count
            print(f"buf={buf}, i={i}")
        return i

    def __init__(self):
        self.queue = collections.deque()

# [start] n=1
# buf4=['a', 'b', 'c', 'd'], self.queue=deque(['a', 'b', 'c', 'd']), count=1
# buf=['a'], i=1
# [start] n=2
# buf4=['e', '', '', ''], self.queue=deque(['b', 'c', 'd', 'e', '', '', '']), count=2
# buf=['b', 'c'], i=2
# [start] n=1
# buf4=['', '', '', ''], self.queue=deque(['d', 'e', '', '', '', '', '', '', '']), count=1
# buf=['d'], i=1

# 157. Read N Characters Given Read4

class Solution(object):
    def read(self, buf, n):
        i = 0
        while i < n:
            buf4 = [''] * 4
            count = read4(buf4)
            if not count:
                break
            count = min(count, n-i)
            buf[i:] = buf4[:count]
            i += count
        return i