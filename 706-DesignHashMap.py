
# 706. Design HashMap
# Hashmap is a common data structure that is implemented in various forms in different language,
# e.g. dict in Python and HashMap in Java.
# The most distinguish characteristic about hashmap is that it provides a fast access to a value
# that is assiciated with a given key.

# 1) hash function design
# the purpose of hash function is to map a key value to an address in the storage space.
# For a good hash function, it should map different keys evenly across the storage space,
# so that we don't end up with the case that the majority of the keys are concentrated in a few spaces

# 2) collision handling
# Essentially the hash function reduces the vast key space into a limited address space.
# As a result, there could be the case where two different keys are mapped to the same address,
# which is what we call "collision".
# Since the collision is inevitable, it is important that we have a stradgy to handle the collision.
# In case of collision, where two different keys are mapped to the same address, we use a bucket to hold all the values.
# The bucket is a container that hold all the values that are assigned by the hash function.
# We could use either a Linkedlist or an Array to implement the bucket data structure.


# https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
# Hash with chaining

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        # self.m = 1000;
        self.m = 997 #better to choose a prime number
        self.h = [None] * self.m

    def put(self, key, value):
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):

        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):

        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)