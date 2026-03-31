# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        col = {}
        while node.next!= None:
            if node not in col:
                col[node] = 1
            else:
                return True
            node = node.next
        return False 