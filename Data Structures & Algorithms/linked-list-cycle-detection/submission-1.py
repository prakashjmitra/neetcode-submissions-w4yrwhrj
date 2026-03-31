# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        counter = 0
        col = {}
        while node.next!= None:
            if node.next.val < counter:
                return True
            node = node.next
            counter = counter + 1
        return False 