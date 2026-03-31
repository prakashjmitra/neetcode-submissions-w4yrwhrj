"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}
        node = head
        while node:
            copy = Node(node.val)
            copies[node] = copy
            node = node.next
        node = head
        while node:
            copy = copies[node]
            copy.next = copies[node.next]
            copy.random = copies[node.random]
            node = node.next
        return copies[head]


        