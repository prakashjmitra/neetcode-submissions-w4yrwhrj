# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        dummy = ListNode()
        if list1.val >= list2.val:
            dummy.next = list2
            list2 = list2.next
        else:
            dummy.next = list1
            list1 = list1.next
        tail = dummy.next
        head1 = list1
        head2 = list2

        while head1 or head2:
            if head1 and head2:
                if head1.val >= head2.val:
                    tail.next = head2
                    head2 = head2.next
                else:
                    tail.next = head1
                    head1 = head1.next
                tail = tail.next
            elif head1 and not head2:
                tail.next = head1
                break
            else:
                tail.next = head2
                break
        return dummy.next

        



        
    

        