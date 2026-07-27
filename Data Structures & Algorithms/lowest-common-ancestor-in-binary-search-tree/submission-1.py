# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(self, current, node1, node2):
            if node2.val < node1.val:
                temp = node2
                node2 = node1
                node1 = temp
            if current.val == node1.val or current.val == node2.val:
                print("reached")
                return current
            elif node1.val < current.val and current.val < node2.val:
                return current
            elif node1.val > current.val and node2.val > current.val:
                return helper(self, current.right, node1, node2)
            elif node1.val < current.val and node2.val < current.val:
                return helper(self, current.left, node1, node2)
            
        return helper(self, root, p, q)
        