# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curr = head
        dummy = None
        counter = 0
        while curr:
            curr = curr.next
            counter +=1 
        print(counter)
        remove = counter - n
        prev = head

        for i in range(remove):
            temp = prev
            prev = prev.next
            dummy = temp
        if dummy and prev:
            print(dummy.val, prev.val)
        
        if dummy:
            if prev.next == None:
                dummy.next = None
            else:
                dummy.next = prev.next
        else:
            if remove == 0:
                return head.next
            if remove == 1:
                if prev.next.next:
                    prev.next = prev.next.next
            return head
        return head
        

        
        
        


        