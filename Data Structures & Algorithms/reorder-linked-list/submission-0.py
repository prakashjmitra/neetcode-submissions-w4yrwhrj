# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        temp = None
        while second:
            temp1 = second.next
            second.next = temp
            temp = second 
            second = temp1
        second = temp
        first = head
        while second:
            temp3 = first.next
            temp4 = second.next
            first.next = second
            second.next = temp3
            first = temp3
            second = temp4
        
       



        