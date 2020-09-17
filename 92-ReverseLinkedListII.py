# 92. Reverse Linked List II
# Reverse a linked list from position m to n

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    def reverseBetween(self, head, m, n):
        p = dummy = ListNode(0)
        dummy.next = head

        for _ in range(m-1):
            p = p.next

        cur = nxTmp = p.next
        prev = None
        for _ in range(n-m+1):
            cur = nxTmp
            nxTmp = nxTmp.next
            cur.next = prev
            prev = cur

        p.next.next = nxTmp
        p.next = prev

        return dummy.next

    # https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
    # O(n), O(1)
    def reverseBetween1(self, head, m, n):
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        cur, prev = p.next, None
        print(f"cur.val={cur.val}")
        for _ in range(n - m + 1):
            cur.next, prev, cur = prev, cur, cur.next
        print(f"p.val={p.val}")
        p.next.next = cur
        p.next = prev

        return dummy.next

    # using only head variable without p doesn't work in case input is ([5], m=1, n=1 )
    def reverseBetween3(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 2):
            head = head.next
        cur, prev = head.next, None
        print(f"cur.val={cur.val}")
        for _ in range(n - m + 1):
            cur.next, prev, cur = prev, cur, cur.next
        print(f"head.val={head.val}")
        head.next.next = cur
        head.next = prev

        return dummy.next

    def reverseBetween2(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head

        cur, prev = head, dummy
        for _ in range(m - 1):
            cur = cur.next
            prev = prev.next

        for _ in range(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        prev = dummy = ListNode(-1);

        for i in range(m - 1):
            prev.next = head
            head = head.next
            prev = prev.next;

        for i in range(m, n + 1):
            if (i == m):
                end = cur = head
                head = head.next
                continue
            p = cur;
            cur = head;
            head = head.next;
            cur.next = p;

        prev.next = cur;
        end.next = head;
        return dummy.next

        # dummy->1->2->3->4->5

        #         prev = dummy = ListNode(-1)
        #         dummy.next = head

        #         for i in range(m-1):
        #             prev = head
        #             head = head.next

        #         pHead = prev
        #         mHead = head

        #         for i in range(m, n+1):
        #             cur = head
        #             head = head.next
        #             cur.next = prev
        #             prev = cur

        #         mHead.next = head
        #         pHead.next = prev

        #         return dummy.next



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

m = 2
n = 4
obj = Solution()
r = obj.reverseBetween(l1, m, n)

pr = r
while pr:
    print(pr.val)
    pr = pr.next