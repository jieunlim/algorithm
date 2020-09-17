# 148. Sort List
# time complexity O(NlogN)
# MergeSort space complexity for Linked list is O(1) with O(logN) recursion
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):

        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(second)

        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next


llist = ListNode(4)
llist2 = ListNode(2)
llist1 = ListNode(1)
llist3 = ListNode(3)

llist.next = llist2
llist2.next = llist1
llist1.next = llist3

obj = Solution()
rtn = obj.sortList(llist)

print(rtn.val)
print(rtn.next.val)
print(rtn.next.next.val)
print(rtn.next.next.next.val)





























############################################
#mergesort
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    # merge sort, recursively
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        print(f" slow.val={slow.val}, fast.val={fast.val}")
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(f" while- slow.val={slow.val}, fast.val={fast.val}")
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    # merge in-place without dummy node
    def merge(self, l, r):
        if not l or not r:
            return l or r
        print(f"l.val={l.val}, r.val={r.val}")
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        print("a")
        while l and r:
            if l.val < r.val:
                print("b")
                l = l.next
            else:
                print("c")
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        print("d")
        pre.next = l or r
        print(head)
        return head

llist = ListNode(4)
llist2 = ListNode(2)
llist1 = ListNode(1)
llist3 = ListNode(3)

llist.next = llist2
llist2.next = llist1
llist1.next = llist3

obj = Solution()
# obj = Solution2()

rtn = obj.sortList(llist)


print(rtn.val)
print(rtn.next.val)
print(rtn.next.next.val)
print(rtn.next.next.next.val)



# basic\MergesortLinkedlist.py
# https://leetcode.com/problems/sort-list/discuss/111266/you-should-use-bottom-up-merge-sort-to-solve-this-with-python-sample-code
#
# O(nlgn) sort -> topdown,bottomup merge sort, 2way/3way quicksort, heapsort
# bottomup mergesort and heapsort are in-place(O(1) space complexity)  <===????
# Since the data structure here is singly linked list, heap sort is ruled out as it requires random data access.
# That leaves us with Bottom-up Merge Sort.

# Bottom up merge sort

# https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity
# bottom-up merge sort. It is the reverse procedure of regular merge sort.

# Merge sort
# time O(nlogn)
# space O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):

        if head is None: return None

        def getSize(head):
            counter = 0
            while (head is not None):
                counter += 1
                head = head.next
            return counter

        def split(head, step):
            i = 1
            while (i < step and head):
                head = head.next
                i += 1

            if head is None: return None
            # disconnect
            temp, head.next = head.next, None
            if temp: print(f"temp={temp.val}")
            print(f"temp={temp}")
            return temp

        def merge(l, r, head):
            cur = head
            while (l and r):
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                print(f"cur={cur.val}")
                cur = cur.next

            cur.next = l if l is not None else r
            while cur.next is not None: cur = cur.next

            print(f"cur={cur.val}")
            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        print(f"size={size}")
        while (bs < size):
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                if l: print(f"l={l.val}")
                if r: print(f"  r={r.val}")
                if cur: print(f"  cur={cur.val}")

                tail = merge(l, r, tail)
                print(f"tail={tail.val}")
            bs <<= 1
            print(f"bs={bs}")
        return dummy.next
llist = ListNode(7)
llist1 = ListNode(1)
llist2 = ListNode(2)
llist3 = ListNode(3)
llist4 = ListNode(4)
llist5 = ListNode(5)
llist6 = ListNode(6)

llist.next = llist2
llist2.next = llist1
llist1.next = llist3
llist3.next = llist5
llist5.next = llist4

obj = Solution()

# r = obj.sortList(llist)
pr = r
while pr:
    print(pr.val)
    pr = pr.next





# https://leetcode.com/problems/sort-list/discuss/296168/python-quicksort-90
class Solution3(object):
    def sortList(self, head):

        bla, _ = self.sort(head)

        return bla

    def sort(self, head):

        if not head or not head.next:
            return head, head

        partition = head
        partition_head = partition
        left_head = ListNode(0)
        right_head = ListNode(0)
        left_node = left_head
        right_node = right_head
        node = partition

        while node.next:
            node = node.next
            if node.val < partition.val:
                left_node.next = node
                left_node = node
            elif node.val > partition.val:
                right_node.next = node
                right_node = node
            else:
                partition.next = node
                partition = node

        partition.next = None
        left_node.next = None
        right_node.next = None

        left_head, left_tail = self.sort(left_head.next)

        right_head, right_tail = self.sort(right_head.next)

        node = left_tail

        if not node:
            node = partition_head
            left_head = partition_head
        else:
            node.next = partition_head
        partition.next = right_head

        if not right_tail:
            right_tail = partition

        return left_head, right_tail


# https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
class Solution22:
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))



# 21. Merge Two Sorted Lists