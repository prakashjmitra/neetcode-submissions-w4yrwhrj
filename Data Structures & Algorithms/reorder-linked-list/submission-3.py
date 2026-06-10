# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #First, find middle node
        if head.next == None:
            return 
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        prev = None
        while temp and temp.next!= None:
            temp2 = temp.next
            temp.next = prev
            prev = temp
            temp = temp2
        temp.next = prev
        while head and temp:
            save = head.next
            save2 = temp.next
            head.next = temp
            head.next.next = save
            temp = save2
            head = head.next.next
        