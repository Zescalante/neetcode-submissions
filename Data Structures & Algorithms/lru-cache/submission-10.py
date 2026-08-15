class ListNode: #want to use listnode to allow for O(1) insertion and removal
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val  
        self.prev = prev    
        self.next = next

class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()

        # sentinals for the list. head will have LRU. tail will have MRU
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity 
        self.cache = {} #want to store the key, address of each node

    def move_to_tail(self, node):
        #disconnect the node where it was 
        node.prev.next, node.next.prev = node.next, node.prev
        #now attach in new spot
        old_prev = self.tail.prev #store the old previous from sentinal tail

        node.next = self.tail
        node.prev = old_prev

        old_prev.next = node
        self.tail.prev = node

    def add_node(self, node):
        
        prev_node = self.tail.prev

        node.prev, node.next = prev_node, self.tail
        prev_node.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            ans = node.val   #store the answer

            self.move_to_tail(node) #now update the order. Move to MRU

            return ans

        return -1 

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.move_to_tail(node) #update the order. Move to MRU

        else:
            node = ListNode(key=key, val=value)
            self.cache[key] = node

            self.add_node(node)

            if len(self.cache) > self.capacity:
                node_remove = self.head.next
                self.cache.pop(node_remove.key)

                # self.head.next, node.next.prev = node.next, self.head
                self.head.next, node_remove.next.prev = node_remove.next, self.head
