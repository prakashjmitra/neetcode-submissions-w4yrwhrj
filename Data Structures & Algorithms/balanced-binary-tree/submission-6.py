# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.backup = True
        if not root:
            return True
        def checkBalance(node):
            if not node:
                return 0
            left = checkBalance(node.left)
            right = checkBalance(node.right)
            self.res = (abs(checkBalance(node.left) - checkBalance(node.right)) <= 1)
            if self.res == False:
                self.backup = False
            return 1 + max(left, right)
        checkBalance(root)
        return self.backup

        


        
            

    # def getHeight(self, val) -> int:
    #     if not val:
    #         return -1
    #     if not val.left and not val.right:
    #         return 0
    #     return 1 + max(self.getHeight(val.left),self.getHeight(val.right))
        
        