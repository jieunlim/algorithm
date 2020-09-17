
# 896. Monotonic Array

def isMonotonic(A):

    if len(A) < 2: return True

    increasing = decreasing = True
    for i in range(len(A)-1):
        # print(A[i], A[i+1])
        if A[i] > A[i+1]:
            increasing = False
        elif A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing

A=[2,3,2]
print(isMonotonic(A))