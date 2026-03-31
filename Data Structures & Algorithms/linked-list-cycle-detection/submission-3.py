# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        node = head
        values = []
        while node.next != None:
            if node.val in values:
                return True
            values.append(node.val)
            node = node.next

        return False