# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def depth(node):
            nonlocal maxi
            if node == None:
                return 0
            if depth(node.left) + depth(node.right) > maxi:
                maxi = depth(node.left) + depth(node.right)
            return 1 + max(depth(node.left), depth(node.right))
        maxi = 0
        depth(root)
        return maxi
        