class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        c = self.tail.prev
        c.next = node
        node.prev = c
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])
        return self.hashmap[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.hashmap) == self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.hashmap[lru_node.key]
            new_node = Node(key, value)
            self.insert(new_node)
            self.hashmap[key] = new_node

        
