# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertHelper(node):
            if node == None:
                return
            if node.left and node.right:
                temp = node.left 
                node.left = node.right
                node.right = temp
                invertHelper(node.left)
                invertHelper(node.right)
            elif node.left and not node.right:
                node.right = node.left
                node.left = None
                invertHelper(node.left)
                invertHelper(node.right)
            elif node.right and not node.left:
                node.left = node.right
                node.right = None
                invertHelper(node.left)
                invertHelper(node.right)
            return node
        return invertHelper(root)

            
            
