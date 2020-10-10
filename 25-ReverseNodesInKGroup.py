# 25. Reverse Nodes in k-Group

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1: return head
        dummy = next_head = ListNode(None)
        dummy.next = head
        prev = curr = head

        while True:
            count = 0
            while curr and count < k:
                count += 1
                curr = curr.next
            if count == k:
                h, t = curr, prev   # assign the first node of next k-group and the first node of current k-group to h(ead), t(ail)
                for _ in range(k):   # this is NOT a standard reversing by swapping arrows between adjacent nodes
                    tmp = t.next     # instead it poplefts a node successively (ref. Campanula's comment)
                    t.next = h
                    h = t
                    t = tmp
                    # one-line implementation: t.next, t, h = h, t.next, t
                next_head.next = h   # connect the last node of the previous reversed k-group to the head of the current reversed k-group
                next_head = prev     # prepare for connecting to the next to-be-reversed k-group
                prev = curr   # head of the next yet to be reversed k-group
            else:   # curr = None and count does not reach k i.e. list is exhausted
                return dummy.next
