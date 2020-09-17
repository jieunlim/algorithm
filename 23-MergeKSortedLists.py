# 23. Merge k Sorted Lists
#  Two ways - 1.Divide and conquer, 2-Heap

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 1. Divide and conquer
    # time O(NlogK) - divide: K is the number of linked lists, merge: n is the total number of nodes in two lists
    # space(O(1))
    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        print(f"mid = {mid}")
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])

        print(f"l={id(l)}, r={id(r)}")
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        print(f"dummy={id(dummy)}, cur={id(cur)}")

        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r

        return dummy.next

    # 2. Heap - time: O(Nlogk) where k is the number of linked list, space O(k)-for heap
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        import heapq
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]

        pq = []
        for i in range(len(lists)):
            if lists[i]:
                pq.append((lists[i].val, i, lists[i]))
        heapq.heapify(pq)

        dummy = curr = ListNode(-1)
        while pq:

            nodeVal, idx, node = heapq.heappop(pq)
            curr.next = node

            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

            curr = curr.next
        return dummy.next

    def mergeK(self, lists):

        dummy = cur = ListNode(-1)
        pq = []
        # O(K)
        for i in range(len(lists)):
            pq.append((lists[i].val, i, lists[i]))

        # O(KLogK) - K is the number of the input lists
        heapq.heapify(pq)

        # O(NLogK)
        while pq:
            nodeVal, idx, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next

            if node.next:
                # O(LogK)
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next


    def mergeKLists_heap(self, lists):
        import heapq

        dummy = cur = ListNode(-1)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                # to avoid comparative issues, "i" added to tuple
                # TypeError: '<' not supported between instances of 'tuple' and 'list'

        while heap:
            node = heapq.heappop(heap)

            cur.next = node[2]
            cur = cur.next

            if node[2].next:
                heapq.heappush(heap, (node[2].next.val, node[1], node[2].next))
        return dummy.next

    def mergeKLists_heap2(self, lists):

        pre = cur = ListNode(0)

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return pre.next
    #
    # def mergeKLists_heap(self, lists):
    #
    #     from heapq import heapify, heappop, heapreplace
    #
    #     # heap = list()
    #     # for i, head in enumerate(lists):
    #     #     if head:
    #     #         heap.append((head.val, i, head) )
    #     heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    #     heapify(heap)
    #
    #     dummy = cur = ListNode(-1)
    #
    #     while heap:
    #         val, i, node = heap[0]
    #         if node.next is None:
    #             heappop(heap)
    #         else:
    #             heapreplace(heap, (node.next.val, i, node.next))  #heappop & heappush
    #         cur.next = node
    #         cur = cur.next
    #
    #     return dummy.next

'''
        from heapq import heappush, heappop, heapreplace, heapify

        # for i, head in enumerate(lists):
        #     print(f"i={i}, head.val={head.val}, head={id(head)}")

        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        print(f"heap ={heap} \n")
        heapify(heap)
        print(f"(heapify) \n heap = {heap}\n")

        dummy = ListNode(0)
        curr = dummy

        while heap != []:
            val, i, node = heap[0]
            print(f"val={val}, i={i}, node ={id(node)}")
            if not node.next:  # exhausted one linked-list
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next))  # return min val then replace the item
                print(heap)
            print(f"cur.next={id(curr.next)}")
            curr.next = node
            print(f"cur.next={id(curr.next)}")
            curr = curr.next
        return dummy.next
'''



list11=ListNode(10)
list12=ListNode(40)
list13=ListNode(50)

list11.next = list12
list12.next = list13

list21=ListNode(1)
list22=ListNode(30)
list23=ListNode(40)

list21.next = list22
list22.next = list23

list31=ListNode(20)
list32=ListNode(60)

list31.next = list32

l4 = ListNode(5)
l41 = ListNode(15)
l42 = ListNode(41)

l4.next = l41
l41.next = l42


lists = [[],[1]]  #for -> if lists[i]
lists = []
lists = [[]]

# lists = [list11, list21, list31, l4]
lists = [list11, list21, list31]
obj = Solution()
# rtn = obj.mergeKLists(lists)
rtn = obj.mergeKLists_heap(lists)

while rtn:
    print(rtn.val)
    rtn = rtn.next

# print(lists)
# for i in range(len(lists)):
#     print(f"{i}th list:")
#     while lists[i]:
#         print(lists[i].val)
#         lists[i] = lists[i].next
