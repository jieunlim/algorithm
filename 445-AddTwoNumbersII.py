
# 445. Add Two Numbers II
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #         s1= [7,2,4,3]
        #         s2= [5,6,4]
        #         7<-0<-8<-7
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        prev = None
        carry = 0

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            newNode = ListNode(total % 10)

            # newNode = ListNode(carry)
            newNode.next = prev
            prev = newNode

        # return node if carry else node.next
        return prev

    def addTwoNumbers2(self, l1, l2):
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        print(stack1, stack2)

        node = ListNode(0)
        carry = 0
        while stack1 or stack2:
            print(stack1, stack2)
            if stack1: carry += stack1.pop()
            if stack2: carry += stack2.pop()

            carry, val = divmod(carry, 10)
            node.val = val

            head = ListNode(carry)
            head.next = node
            node = head

        return node.next if node.val == 0 else node

l1 = ListNode(9)
l11 = ListNode(7)
l12 = ListNode(4)
l13 = ListNode(3)
l1.next = l11
l11.next = l12
l12.next = l13

l2 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)
l2.next = l21
l21.next = l22

obj = Solution()

rtn = obj.addTwoNumbers(l1, l2)
prtn = rtn

while prtn:
    print(prtn.val)
    prtn = prtn.next