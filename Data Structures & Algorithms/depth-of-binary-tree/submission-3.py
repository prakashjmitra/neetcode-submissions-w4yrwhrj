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
        number = 1
        return max(self.maxDepthHelper(root.left, number), self.maxDepthHelper(root.right, number))
        
    def maxDepthHelper(self, node, counter):
        if node == None:
            return counter
        if node.left == None and node.right == None:
            counter = counter + 1
            return counter
        elif node.left == None:
            counter = counter + 1
            return self.maxDepthHelper(node.right, counter)
        elif node.right == None:
            counter = counter + 1
            return self.maxDepthHelper(node.left, counter)
        else:
            counter = counter + 1
            return max(self.maxDepthHelper(node.left, counter),self.maxDepthHelper(node.right, counter))