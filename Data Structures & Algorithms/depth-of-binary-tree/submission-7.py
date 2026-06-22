# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        def maxDepthHelper(node, val):
            if node == None:
                return val
            return max(maxDepthHelper(node.left,val + 1), maxDepthHelper(node.right, val + 1))
       
        return max(maxDepthHelper(root.left, 1), maxDepthHelper(root.right, 1))



            
            