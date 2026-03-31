class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node



    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.storage:
            self.remove(self.storage[key])
            self.insert(self.storage[key])
            return self.storage[key].value
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.remove(self.storage[key])
        self.storage[key] = Node(key,value)
        self.insert(self.storage[key])
        if len(self.storage) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.storage[lru.key]

            

