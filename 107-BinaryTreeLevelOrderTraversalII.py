class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res, maxV = [], 0
        dic = {}

        myQ = deque()
        myQ.append((root, 0))

        while myQ:
            node, level = myQ.popleft()
            # print(f"node.val={node.val}, level={level}")
            if level not in dic:
                dic[level] = [node.val]
            else:
                dic[level].append(node.val)

            if node.left:
                maxV = max(maxV, level+1)
                myQ.append((node.left, level+1))
            if node.right:
                maxV = max(maxV, level+1)
                myQ.append((node.right, level+1))

        # print(f"maxV={maxV}")
        # for i in range(0, maxV+1):
        for i in range(maxV, -1, -1):
            res.append(dic[i])
        return res