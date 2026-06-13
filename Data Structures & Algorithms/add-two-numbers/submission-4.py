# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        number1 = 0
        number2 = 0
        add = 0
        counter1 = 0
        sums = []
        while first or second:
            if first and second:
                number1 += (first.val * (10 ** counter1))
                number2 += second.val * (10 ** counter1)
                first = first.next
                second = second.next
            elif first and not second:
                number1 += first.val * (10 ** counter1)
                first = first.next
            elif not first and second:
                number2 += second.val * (10 ** counter1)
                second = second.next

            counter1 += 1
        add = number1 + number2
        print(number1, number2)
        print(add)
        number = str(add)
        number = number[::-1]
        newhead = ListNode()
        answer = newhead
        counter = 0
        while counter< len(number):
            if counter == len(number) - 1:
                break
            print("reached 2")
            newhead.val = number[counter]
            print(number[counter])
            newhead.next = ListNode()
            newhead = newhead.next
            counter = counter + 1
        newhead.val = number[counter]
        return answer


        