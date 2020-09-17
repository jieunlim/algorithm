# 2. Add Two Numbers

# Time O(max(M, N)), space(max(M, N)) - max(M,N)+1
# M, N is represents the length of l1 and l2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers_22(self, l1, l2):

        def helper(l1, l2, carry=0):
            if not l1 and not l2 and not carry:
                return None

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            r = ListNode(total % 10)
            r.next = helper(l1.next if l1 else None, l2.next if l2 else None, carry)

            return r
        return helper(l1, l2)

     def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
                print(f"v1={v1}")
                if l1: print(f"l1.val={l1.val}")
            if l2:
                v2 = l2.val
                l2 = l2.next
                print(f"v2={v2}")
                if l2: print(f"l2.val={l2.val}")
            carry, val = divmod(v1+v2+carry, 10)
            print(f"carry={carry}, val={val}")
            n.next = ListNode(val)
            n = n.next
        return root.next


    def addTwoNumbers2(self, l1, l2):

        def ATN(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return

            print(f" carry={carry}")
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next

            node = ListNode(v % 10)
            carry = v // 10

            print(f"node={node.val}, carry={carry}")
            if l1 or l2 or carry :
                node.next = ATN(l1, l2, carry)

            return node

        return ATN(l1, l2, 0)

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        twoSum = p_twoSum = ListNode(0)
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            carry, digitSum = divmod(l1_val + l2_val + p_twoSum.val, 10)
            p_twoSum.val = digitSum

            if l1:  l1 = l1.next
            if l2:  l2 = l2.next

            if l1 or l2 or carry > 0:
                p_twoSum.next = ListNode(carry)
                p_twoSum = p_twoSum.next

        return twoSum

l1 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(9)
l1.next = l11
l11.next = l12
l2 = ListNode(5)
l21 = ListNode(6)
# l22 = ListNode(4)
l2.next = l21
# l21.next = l22
obj = Solution()

rtn = obj.addTwoNumbers3(l1, l2)
prtn = rtn

while prtn:
    print(prtn.val)
    prtn = prtn.next
