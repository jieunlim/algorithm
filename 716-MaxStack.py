# 716. Max Stack

# https://leetcode.com/problems/max-stack/discuss/108933/O(1)-isn't-possible
# Because if it were, you could use this data structure to sort an array of numbers in O(n) time.
# So, at the very least, either push(x) or popMax() must be O(logn)


# https://leetcode.com/problems/max-stack/discuss/140017/Fast-and-Simple-Python-Solution-(lazy-updates-beating-100)
# These 2 lines:
# self.lsd.remove(self.ls[-1][0])
# self.hpd.remove(-self.hp[0][1])
# are not necessary, because self.id is unique and once the number of its id id deleted, we won't encounter it again
#
# The 2 lines are used to save space.
# Imagine you add 1000 values to the stack and you pop 999 values. Without the 2 lines, the sets still have all the ids.
class MaxStack:
    def __init__(self):
        self.ls = []        # list (stack)
        self.hp = []        # heap
        self.hpd = set()    # id of items deleted in ls but not hp
        self.lsd = set()    # id of items deleted in hp but not ls
        self.id = 0

    def push(self, x):
        self.ls.append((self.id, x))
        heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self):
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self):
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self):
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self):
        x = self.peekMax()
        _, nid = heappop(self.hp)
        self.lsd.add(-nid)
        return x