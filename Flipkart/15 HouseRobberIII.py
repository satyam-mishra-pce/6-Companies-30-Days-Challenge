# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return (0, 0)
            sub = (dfs(node.left), dfs(node.right))

            return (node.val + sub[0][1] + sub[1][1], max(sub[0]) + max(sub[1]))

        return max(dfs(root))
