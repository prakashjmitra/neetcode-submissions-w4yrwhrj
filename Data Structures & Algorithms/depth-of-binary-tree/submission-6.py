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
            if node.left and node.right:
                return max(maxDepthHelper(node.left, val + 1),maxDepthHelper(node.right, val + 1))
            elif node.left and not node.right:
                val += 1
                return maxDepthHelper(node.left, val)
            elif node.right and not node.left:
                val += 1
                return maxDepthHelper(node.right, val)
            else:
                val = val + 1
                return val
        sum1 = 1
        sum2 = 1
        left = maxDepthHelper(root.left, sum1)
        right = maxDepthHelper(root.right, sum2)
        print(left, right)
        return max(left, right)



            
            