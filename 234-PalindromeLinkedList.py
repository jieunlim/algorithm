# 234. Palindrome Linked List

# Could you do it in O(n) time and O(1) space?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head):

        def isP(li):
            i, j = 0, len(li)-1
            while i < j:
                if li[i] != li[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        # if not head:
        #     return False

        li = []

        node = head
        while node:
            li.append(node.val)
            node = node.next

        return isP(li)

# https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
    def isPalindrome2(self, head):
        # fast = slow = head
        # # find the mid node
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # # reverse the second half
        # node = None
        # while slow:
        #     nxt = slow.next
        #     slow.next = node
        #     node = slow
        #     slow = nxt
        # # compare the first and second half nodes
        # while node: # while node and head:
        #     if node.val != head.val:
        #         return False
        #     node = node.next
        #     head = head.next
        # return True


        fast = mid = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        # reverse the second half
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        # compare the first and second half nodes
        while prev: # while node and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(1)
# l4 = ListNode(1)

l1.next = l2
l2.next = l3
# l3.next = l4

l1 = []
obj = Solution()
print(obj.isPalindrome(l1))


# 92. Reverse Linked List II
# 237. Delete Node in a Linked List
# 725. Split Linked List in Parts

# 379. Design Phone Directory
# 845. Longest Mountain in Array
# 977. Squares of a Sorted Array