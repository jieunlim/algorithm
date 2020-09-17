# 155. Min Stack
# using a tuple in the first instance and calling min (on just 2 values) each time a push operation occurs
# Approach 1: Stack of Value/ Minimum Pairs
# time O(1), space O(n) (actually O(2n) for push)

class Solution:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))
    def pop(self):
        if self.stack: self.stack.pop()

    def top(self):
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):
        if self.stack: return self.stack[-1][1]
        else: return None

obj = Solution()
obj.push(1)
obj.push(4)
obj.push(0)
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.getMin())
print(obj.top())


# 716. Max Stack
# 239. Sliding Window Maximum


class Solution2:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:

        # We always put the number onto the main stack.
        self.stack.append(x)

        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])

        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]