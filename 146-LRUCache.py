
# 146. LRU Cache

# Least Recently Used cache
# Hash
# DLinkedList - key, value, next, prev
# LRUCache
# capacity, cache, size, head, tail
# get(key) - find the value, move to head
# put(key, value)
#  if exists: update, move to head
#   else: create, check capacity



# LRU Cache
# Least Recently Used
# get, put(insert)
#      delete, insert, order
# Hash  O(1), O(1) ,n
# Queue O(N), O(1) ,y
# LL    O(N), O(1) ,y
# D LList O(1), O(1) ,y

# stored in Hashmap
# Head(recent) - Tail(old)
# Doubly LL - order

# Doulby LL - key, value, next, prev
# LRUCache - capacity, cache, size, head, tail
#           - get(key)->value : search value, move to head(recent)
#           - put(key, value) : serarch key, value
#               if exists: update value, move to head
#               else: new node(add to DLL, hashmap), check capacity

###################################
# get(key) - get the value of the key if the key exists in the cache, otherwise return -1
# put(key, value) - Set or insert the value if the key is not already present.
#           - When the cache reached its capacity,
#           it should invalidate the least recently used item before inserting a new item.

#  Could you do both operations in O(1) time complexity?

# Approach 1: Ordered dictionary
# Python - OrderedDict
# Java - LinkedHashMap
# time - O(1), space - O(capacity)
# 1) get(key) - return value /-1 if not exists in the
# cache
# 2) put(key, value) - set or insert/ invalidate LRU
# item if the cache reached it’s capacity

##########################################################
class LRUCache:

    #     def __init__(self, capacity: int):

    #     def get(self, key: int) -> int:

    #     def put(self, key: int, value: int) -> None:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DLinkedList(), DLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def moveToHead(self, node):

        self.removeNode(node)
        self.addNode(node)

    def removeNode(self, node):
        n = node.next
        p = node.prev

        n.prev = p
        p.next = n

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node: return -1

        self.moveToHead(node)
        return node.value

    def popTail(self):

        tail = self.tail.prev
        self.removeNode(tail)
        return tail

    def put(self, key: int, value: int) -> None:

        node = self.cache.get(key)
        if not node:
            new = DLinkedList()
            new.key = key
            new.value = value

            self.addNode(new)
            self.size += 1
            self.cache[key] = new

            if self.size > self.capacity:
                tail = self.popTail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.moveToHead(node)


class DLinkedList:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


##########################################################


from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key: int):

        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) #FIFO


obj = LRUCache(3)
tst_num = 4
tst_val = 'ABC'
print(f"get {tst_num} ->", obj.get(tst_num))
obj.put(tst_num, tst_val)
print(f"get {tst_num} ->", obj.get(tst_num))
obj.put(5, 'DDD')
obj.put(6, 'EEE')
print(format(obj))
obj.put(7, 'FFF')
print(format(obj))
print(f"get {5} ->", obj.get(5))
print(format(obj))
obj.put(4, 'ABB')
print(format(obj))
print("========")

# OrderedDict([items])
# https://docs.python.org/3/library/collections.html#collections.OrderedDict
# popitem(last=True) #LIFO, last=False #FIFO
# move_to_end(key, last=True) - default is last = true, move to right end

class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        if key not in self:
            return -1
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

lru = LRU(2)
lru.__setitem__(1, 'A')
lru.__setitem__(2, 'B')
lru.__setitem__(3, 'C')
print(lru.__getitem__(1))
print(lru.__getitem__(2))
print(lru.__getitem__(3))
print(f"=====")

# Approach 2: Hashmap + DoubleLinkedList
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache2():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node #watch this order
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

lru2 = LRUCache2()