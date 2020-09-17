
# 583. Delete Operation for Two Strings
# time O(m*n)
# space O(
def deleteTwo(t1, t2):

    def DT(t1, t2):
        print(f"t1={t1}, t2={t2}, memo={memo}")
        if not t1:
            return len(t2)
        elif not t2:
            return len(t1)

        if (t1, t2) in memo:
            return memo[(t1, t2)]

        if t1[0] == t2[0]:
            memo[(t1, t2)] = DT(t1[1:], t2[1:])
        else:
            memo[(t1, t2)] = min(DT(t1[1:], t2), DT(t1, t2[1:])) + 1
        return memo[(t1, t2)]

    memo = {}
    return DT(t1, t2)

t1 = "sea"
t2 = "eat"
t1 = "dinitrophenylhydrazine"
t2 = "acetylphenylhydrazine"
print(deleteTwo(t1, t2))

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103267/Python-Straightforward-with-Explanation
