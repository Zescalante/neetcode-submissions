class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}

        self.head = ListNode() #sentinal nodes
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def add_to_front(self, node):   #attach new node to front
        next_node = self.head.next

        node.prev = self.head
        node.next = next_node

        self.head.next = node
        next_node.prev = node

    def remove_node(self, node):   #remove node 

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node 



    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove_node(node)
            self.add_to_front(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove_node(node)
            self.add_to_front(node)
        
            return
        
        new_node = ListNode(key=key, val=value)
        self.add_to_front(new_node)
        self.hashmap[key] = new_node

        if len(self.hashmap) > self.capacity:
            lru_node = self.tail.prev
            self.remove_node(lru_node)
            del self.hashmap[lru_node.key]