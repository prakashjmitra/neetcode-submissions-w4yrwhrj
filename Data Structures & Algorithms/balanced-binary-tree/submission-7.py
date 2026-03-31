# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            height = 1 + max(left[1],right[1])
            return [balanced,height]
        return dfs(root)[0]



        


        
            

    # def getHeight(self, val) -> int:
    #     if not val:
    #         return -1
    #     if not val.left and not val.right:
    #         return 0
    #     return 1 + max(self.getHeight(val.left),self.getHeight(val.right))
        
        