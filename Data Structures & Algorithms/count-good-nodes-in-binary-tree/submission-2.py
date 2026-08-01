# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(self, node, maxi):
            if not node:
                return 0
            result = 0
            if node.val >= maxi:
                result += 1
                maxi = node.val
            result += helper(self, node.left,maxi)
            result += helper(self, node.right, maxi)
            return result

        return 1 + helper(self, root.left, root.val) + helper(self, root.right, root.val)
        
        
        
        
        
            


        