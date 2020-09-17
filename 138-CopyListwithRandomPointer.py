# 138. Copy List with Random Pointer
# Solution1 - recursive O(N), O(N)
# Solution2 - iterative with O(N) space
# Solution3 - iterative with O(1) space

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

# Solution1-recursive O(N), space O(N)
class Solution:
    # copy simple linked list
    def copyList(self, head):
        if not head:
            return None

        node = Node(head.val, None)
        node.next = self.copyList(head.next)

        return node

    def __init__(self):
        self.visitedHash = {}

    def copyLinkedList(self, head):

        if not head:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)

        self.visitedHash[head] = node
        node.next = self.copyLinkedList(head.next)
        node.random = self.copyLinkedList(head.random)

        return node



# Solution 1 - copied, for testing
class Solution1(object):

    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        print(f"head={head.val}")
        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        print(f"visitedHash={self.visitedHash}")
        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        if node.next: print(f"head={head.val}, node.next={node.next.val}")
        else: print(f"head={head.val}, no next")
        node.random = self.copyRandomList(head.random)
        if node.random: print(f"head={head.val}, node.random={node.random.val}")
        else: print(f"head={head.val}, no random")

        return node

    # Solution3
    def copyRandomList3(self, head):
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old

l1 = Node(7, None, None)
l2 = Node(13, None, None)
l3 = Node(1, None, l1)

l1.next = l2
l1.random = l3
l2.next = l3
l2.random = None

obj = Solution()
# r = obj.copyRandomList3(l1)
r = obj.copyList(l1)
print(id(l1), id(l1.next), id(l1.next.next))
print(id(r), id(r.next), id(r.next.next))
pr = r

print(pr.val, pr.random.val)
print(pr.next.val, pr.next.random)
print(pr.next.next.val, pr.next.next.random.val)
while pr:
    print(pr.val)
    pr = pr.next

# print(r.random.val)
# print(r.random.random.val)
# print(r.next.random)


####################################################################
class Solution(object):

    # Solution2
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            print(f"node={node.val}, visited={self.visited}")
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        print(f"old_node.val={old_node.val}, new_node.val={new_node.val}, visited={self.visited[old_node].val}")
        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:
            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            if new_node.random: print(f"new_node.random={new_node.random.val}")
            if new_node.next: print(f"new_node.next={new_node.next.val}")

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

            if old_node: print(f"old_node={old_node.val}")
            if new_node: print(f"new_node={new_node.val}")

        return self.visited[head]
    # END of solution2


    def copyRandomList2(self, head: 'Node') -> 'Node':
        import collections
        """dict with old Nodes as keys and new Nodes as values. 
        Doing so allows us to create node's next and random 
        as we iterate through the list from head to tail. 
        Otherwise, we need to go through the list backwards.
        defaultdict() is an efficient way of handling missing keys """
        map_new = collections.defaultdict(lambda: Node(None, None, None))
        map_new[None] = None  # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop

        nd_old = head
        while nd_old:
            print(f"nd_old={nd_old.val}, map_new={map_new}")
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]


    def copyRandomListe(self, head):

        dic = collections.defaultdict(lambda: Node(10))
        #dic[None] = None
        if head==None:
            return head
        n = head
        while n:
            dic[n].label = n.label
            if n.next==None:
                dic[n].next=None
            else:
                dic[n].next = dic[n.next]
            if n.random==None:
                dic[n].random=None
            else:
                dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

l1 = Node(7, None, None)
l2 = Node(13, None, None)
l3 = Node(1, None, l1)

l1.next = l2
l1.random = l3
l2.next = l3
l2.random = None

obj = Solution()
# r = obj.copyRandomList2(l1)
# pr = r
#
# while pr:
#     print(pr.val)
#     pr = pr.next