# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        answer = []
        nodeslist = deque()
        answer.append(root.val)
        nodeslist.append(root)
        while nodeslist:
            empty = []
            for i in range(len(nodeslist)):
                node = nodeslist.popleft()
                if node.left:
                    nodeslist.append(node.left)
                if node.right:
                    nodeslist.append(node.right)
                empty.append(node.val)
            answer.append(max(empty))
        answer.pop(0)

        return answer
                
                
                


            


        