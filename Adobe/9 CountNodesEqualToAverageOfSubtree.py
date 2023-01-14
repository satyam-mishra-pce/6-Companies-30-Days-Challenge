# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        count = 0
        def dfs(node):
            if node is None:
                return (0, 0)
            nonlocal count
            v = node.val
            leftsum, leftcount = dfs(node.left)
            rightsum, rightcount = dfs(node.right)
            totalsum = v + leftsum + rightsum
            totalnodes = 1 + leftcount + rightcount
            if (totalsum // totalnodes) == v:
                count += 1
            return (totalsum, totalnodes)
        
        dfs(root)
        return count
