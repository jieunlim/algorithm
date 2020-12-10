# 382. Linked List Random Node

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        result, node, count = 0, self.head, 1
        while node:
            x = random.randint(1, count)
            if x == count:
                result = node.val
            node = node.next
            count += 1
        return result




#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def __init__(self, head):
        self.h = head
        self.length = 0

        cur = head

        while cur:
            self.length += 1
            cur = cur.next

    def getRandom(self):

        r = random.randint(0, self.length - 1)
        cur = self.h
        i = 0
        while i < r:
            cur = cur.next
            i += 1
            if not cur:
                return self.h.val

        return cur.val