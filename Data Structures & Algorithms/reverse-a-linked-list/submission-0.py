# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        node = head
        prev = None
        while node.next!= None:
            print("reached",prev)
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        node.next = prev
        return node
    
        
        
    