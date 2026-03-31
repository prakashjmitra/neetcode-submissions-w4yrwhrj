# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return head.next
        counter = 0
        actual = 0
        node = head
        while node:
            node = node.next
            counter = counter + 1
        value = counter - n
        second = head
        while actual < value -1:
            second = second.next
            actual = actual + 1
        if counter == n:
            head = head.next
            return head
        else:
            print(second.val)
            second.next = second.next.next
            

        print(counter)
        return head

            