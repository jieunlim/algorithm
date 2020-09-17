# 203. Remove Linked List Elements
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int):

        dummy = prev = ListNode(-1)

        dummy.next = prev.next = head
        # cur = head

        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head

            head = head.next

        return dummy.next

        # dummyH = prev = ListNode(0)
        # dummyH.next = prev.next = head
        # curr = head
        #
        # while curr:
        #     if curr.val == val:
        #         prev.next = curr.next
        #     else:
        #         prev = curr
        #     curr = curr.next
        #
        # return dummyH.next

    # https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).
    def removeElements2(self, head, val):

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(3)

l1.next = l2
l2.next = l3
l3.next = l4

val = 3
obj = Solution()
r = obj.removeElements(l1, val)

pr = r
while pr:
    print(pr.val)
    pr = pr.next

# 27. Remove Element