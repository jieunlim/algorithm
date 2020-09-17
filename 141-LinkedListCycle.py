# 141. Linked List Cycle
# Given a linked list, determine if it has a cycle in it.
# return True/False

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # https://leetcode.com/problems/linked-list-cycle/discuss/44539/AC-Python-76ms-Floyd-loop-detection-in-7-lines
    # Floyd's Cycle Detection Alogrithm or Tortoise and Hare Algorithm
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    # Hash
    # Leetcode Solution Approach 1
    def hasCycle2(self, head):
        dict = set()
        while head:
            if head in dict:
                return True
            else:
                dict.add(head)
            head = head.next
        return False

head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

head.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

obj = Solution()
print(obj.hasCycle(head))


# https://codingfreak.blogspot.com/2012/09/detecting-loop-in-singly-linked-list_22.html
# https://pieceofcode.kr/algorithm-cycle-detection-tortoise-and-hare/
# 사이클 찾는 방법
# 1) 방문 기록할 set, hash를 사용, extra space O(n) 필요
# 2) Floyd's tortoise and hare 알고리즘 이용: space O(1), read only input array
#    - 사이클의 존재여부, 시작위치, 길이를 찾을 수 있음.
#
# <Tortoise and hare algorithm>