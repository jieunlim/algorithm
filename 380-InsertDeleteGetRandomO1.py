# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/163782/Python-solution
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            return False
        else:
            self.arr.append(val)
            self.length += 1
            self.s[val] = self.length - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        print(f"remove val={val}")
        if val in self.s:
            print(f"s={self.s}, arr={self.arr}")
            idx = self.s[val]
            last = self.arr[self.length - 1]
            print(f"  idx={idx}, last={last}")
            self.arr[idx] = last
            self.s[last] = idx
            del self.s[val]
            self.arr.pop()
            self.length -= 1
            print(f"s={self.s}, arr={self.arr}")
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, self.length - 1)
        return self.arr[idx]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()

print(obj.insert(4))
print(obj.insert(3))
print(obj.insert(5))
print(obj.getRandom())
print(obj.insert(1))
print("insert 1:", obj.s, obj.arr)
print(obj.remove(2))
print(obj.insert(2))
print("insert 2:", obj.s, obj.arr)
print(obj.getRandom())
print(obj.remove(5))
print("remove 1:", obj.s, obj.arr)
print(obj.insert(2))  #False
print(obj.getRandom())
print(obj.getRandom())

'''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

'''