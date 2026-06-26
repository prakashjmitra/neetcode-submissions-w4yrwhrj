# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = True
        def helper(node):
            nonlocal check
            if node == None:
                return 0
            elif abs(helper(node.left) - helper(node.right)) > 1 or abs(helper(node.right) - helper(node.left)) > 1:
                check = False
            return 1 + max(helper(node.left),helper(node.right))
        helper(root)
        return check
        