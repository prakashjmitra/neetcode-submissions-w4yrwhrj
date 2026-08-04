# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        curr = root
        array = []
        nodes = deque()
        nodes.append(root)
        array.append(root.val)
        while nodes:
            node = nodes.pop()
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if node.val not in array:
                array.append(node.val)
        array.sort()
        return array[k-1]
        
        