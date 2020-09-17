
# 21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

# recursively
# time O(M+N), space O(M+N) stack

    def mergeTwoLists(self, l1, l2):

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


            # if l1 is None:
            #     print(f"l1 is none:  {l2.val}, {l2.next}")
            #     return l2
            # elif l2 is None:
            #     print(f"l2 is none:  {l1.val} {l1.next}")
            #     return l1
            # elif l1.val < l2.val:
            #     print(f"-{l1.val}, {l2.val}")
            #     l1.next = self.mergeTwoLists(l1.next, l2)
            #     print(f"l1.val = {l1.val}, l1.next = {l1.next}")
            #     return l1
            # else:
            #     print(f"--{l1.val}, {l2.val}")
            #     l2.next = self.mergeTwoLists(l1, l2.next)
            #     print(f"l2.val = {l2.val}, l2.next={l2.next}")
            #     return l2

    def mergeTwoLists22(self, l1, l2):
        if not l1:
            print(f"not l1, {l2.val}")
            return l2
        elif not l2:
            print(f"not l2, {l1.val}")
            return l1

        node = ListNode(-1)
        if l1.val < l2.val:
            node.val = l1.val
            node.next = self.mergeTwo(l1.next, l2)
        else:
            node.val = l2.val
            node.next = self.mergeTwo(l1, l2.next)
        return node

#iteratively
# time O(M+N), space O(1)
    def mergeTwoLists2(self, l1, l2):
        dummy = cur = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        cur.next = l1 if l1 is not None else l2

        return dummy.next

flist1 = ListNode(1)
flist2 = ListNode(3)
flist3 = ListNode(5)

slist1 = ListNode(2)
slist2 = ListNode(4)
slist3 = ListNode(6)

flist1.next = flist2
flist2.next = flist3

slist1.next = slist2
slist2.next = slist3

obj = Solution()
rtn = obj.mergeTwoLists(flist1, slist1)


while rtn:
    print(rtn.val)
    rtn = rtn.next

# print(rtn.val)
# print(rtn.next.val)
# print(rtn.next.next.val)
# print(rtn.next.next.next.val)
# print(rtn.next.next.next.next.val)
# print(rtn.next.next.next.next.next.val)

