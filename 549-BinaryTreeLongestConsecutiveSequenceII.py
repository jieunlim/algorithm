
# 549. Binary Tree Longest Consecutive Sequence II

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, arr):
        if not arr: return

        root = TreeNode(arr[0])

        dQ = deque()
        dQ.append(root)

        i = 1
        while dQ:
            node = dQ.popleft()

            if i < len(arr):
                if arr[i] is not None and node:  # is not None for dealing with '0' value
                    node.left = TreeNode(arr[i])
                    dQ.append(node.left)
                else:
                    dQ.append(None)
            i += 1
            if i < len(arr):
                if arr[i] is not None and node:
                    node.right = TreeNode(arr[i])
                    dQ.append(node.right)
                else:
                    dQ.append(None)
            i += 1

        # self.inOrderT(root)
        return root

    def inOrderT(self, root):
        if root:
            self.inOrderT(root.left)
            print(root.val)
            self.inOrderT(root.right)


    def longestConsecutive(self, root):
        def dfs(node, parent):
            if not node:
                return 0, 0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l[0] = max(l[0], li + rd + 1, ld + ri + 1)
            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0
        l = [0]
        dfs(root, root)
        return l[0]


    def longestConsecutive2(self, root):
        return max(self.get_max(root))

    def get_max(self, root):
        """Return max increasing and max decreasing ending at root, and max overall."""
        if not root:
            return 0, 0, 0

        inc, dec = 1, 1

        li, ld, lt = self.get_max(root.left)
        ri, rd, rt = self.get_max(root.right)

        if root.left:
            if li and root.left.val - root.val == 1:
                inc = li + 1

            if ld and root.left.val - root.val == -1:
                dec = ld + 1

        if root.right:
            if ri and root.right.val - root.val == 1:
                inc = max(inc, ri + 1)

            if rd and root.right.val - root.val == -1:
                dec = max(dec, rd + 1)

        return inc, dec, max(inc + dec - 1, lt, rt)
arr = [1 ,2 ,3]
arr = [2 ,1 ,3]
obj = Solution()
root = obj.buildTree(arr)
obj.inOrderT(root)
print()
print(obj.longestConsecutive2(root))


# 리턴값 : 부모보다 1 작으면 자기 자식들중에 작아지는값 중 최대길이 리턴
# 1크면 커지는 값 중 최대길이 리턴
#
# Max : 차일드중에 작아지는 값만 있으면 그 최대 길이 + 1(본인) 비교
# 커지는 값만 있으면 그 최대길이 + 1 비교
# 둘다 있으면 합 + 1 비교

'''
class Solution {
    int max = 0;
    int dfs(TreeNode cur, TreeNode parent) {
        if(cur == null) return 0;
        int ret = 0;
        //left
        int left = dfs(cur.left, cur);
        //right
        int right = dfs(cur.right, cur);
        //max
        int temp = 1;
        int flag = 0;
        if (parent != null && (parent.val == cur.val -1 || parent.val == cur.val +1)) ret = 1;
        if (cur.left != null && cur.left.val == cur.val + 1) {
            temp += left;
            flag = 1;
            if (parent != null && parent.val == cur.val -1) ret = temp;
        }
        else if (cur.left != null && cur.left.val == cur.val - 1) {
            temp += left;
            flag = 2;
            if (parent != null && parent.val == cur.val + 1) ret = temp;
        }

        if (cur.right != null && cur.right.val == cur.val + 1) {
            if (flag == 1) temp = Math.max(temp, right +1);
            else temp += right;
            if (parent != null && parent.val == cur.val - 1) ret = Math.max(ret, right +1);
        }

        else if (cur.right != null && cur.right.val == cur.val - 1) {
            if (flag == 2) temp = Math.max(temp, right + 1);
            else temp += right;
            if (parent != null && parent.val == cur.val + 1) ret = Math.max(ret, right +1);
        }
        max = Math.max(temp, max);


        return ret; 
    }
    public int longestConsecutive(TreeNode root) {
        dfs(root, null);
        return max;
    }
'''
