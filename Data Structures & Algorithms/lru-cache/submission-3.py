class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)

            return self.cache[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.stack[0]]
                self.stack.pop(0)
                
                self.cache[key] = value
                self.stack.append(key)
                
            else:
                self.cache[key] = value
                self.stack.append(key)
        
