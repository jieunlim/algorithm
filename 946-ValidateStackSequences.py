
# 946. Validate Stack Sequences
# time O(N)
# space O(N)
def validateStack(pushed, popped):

    stack = []
    i = 0
    for p in pushed:
        stack.append(p)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return stack == []
    # return i == len(popped)

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]
print(validateStack(pushed, popped))