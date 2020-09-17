# 160. Intersection of Two Linked Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # copied code from this link
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
    # refer this explanation
    # https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            if pa: print(f"pa={pa.val}")
            else: print("pa None")
            if pb: print(f"pb={pb.val}")
            else: print("pb None")
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

        # the idea is if you switch head, the possible difference between length would be countered.
        # On the second traversal, they either hit or miss.
        # if they meet, pa or pb would be the node we are looking for,
        # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None


headA = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(4)
headB = ListNode(3)

headA.next = h2
h2.next = h3
headB.next = h3

obj = Solution()
r = obj.getIntersectionNode2(headA, headB)

pr = r
while pr:
    print(pr.val)
    pr = pr.next