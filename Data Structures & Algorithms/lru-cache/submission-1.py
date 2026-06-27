from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.usage = deque()
        

    def get(self, key: int) -> int:
        if key in self.map:
            self.usage.remove(key)
            self.usage.append(key) 
            return self.map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.usage.remove(key)
        elif len(self.map) == self.capacity:
            to_remove = self.usage.popleft()
            self.map.pop(to_remove)

        self.map[key] = value
        self.usage.append(key)