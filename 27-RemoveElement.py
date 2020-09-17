# 27. Remove Element

# Two Pointers - when elements to remove are rare
# time O(n)
# space O(1)

def removeElement(arr, val):
    i, n = 0, len(arr)

    while i < n:
        if arr[i] == val:
            arr[i] = arr[n-1]
            n -= 1
        else:
            i += 1
    return n


arr = [2,3,2,3]
val = 3
print(removeElement2(arr, val))