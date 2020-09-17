
# 170. Two Sum III - Data structure design
# Should we keep the list in order while inserting new numbers in the function add(number) ?
# Or should we do the sorting on demand, i.e. at the invocation of find(value) ?

# The usage pattern of the desired data structure in the online judge, as we would discover,
# is that the add(number) function would be called frequently which might be followed a less frequent call of find(value) function.
# ==> The usage pattern implies that we should try to minimize the cost of add(number) function. As a result,
# we sort the list within the find(value) function instead of the add(number) function.
# time - add O(1), find O(nlgn + n) => O(nlgn) for sorting, space - O(n)

class TwoSum:
    def __init__(self):
        self.numArray = []
        self.cnt = 0

    def add(self, number):
        self.numArray.append(number)
        self.cnt += 1

    def find(self, value):
        i, j = 0, self.cnt-1
        s_nums = sorted(self.numArray)

        while i < j:
            s = s_nums[i] + s_nums[j]
            if s == value:
                return True
            elif s < value:
                i += 1
            else:
                j -= 1

        return False

obj = TwoSum()
# obj.add(1)
# obj.add(3)
# obj.add(4)
# obj.add(5)
# print(obj.find(4))
# print(obj.find(7))
obj.add(3)
obj.add(1)
obj.add(2)
print(obj.find(3))