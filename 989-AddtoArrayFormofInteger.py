
# 989. Add to Array-Form of Integer
def addToArrayForm(A, K):

    listK = []
    while K:
        listK.append(K%10)
        # print(listK, K)
        K = K//10

    B = listK[::-1]
    carry = 0
    res = []
    while A or B or carry:
        a = A.pop() if A else 0
        b = B.pop() if B else 0

        total = a + b + carry
        res.append(total%10)
        carry = total//10

    return res[::-1]

print(addToArrayForm(A, K))