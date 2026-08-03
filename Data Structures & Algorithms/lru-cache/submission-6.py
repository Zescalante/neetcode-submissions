from collections import deque
class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode() #LRU will go here
        self.tail = ListNode()  #MRU will go here

        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key] #want to move this node to MRU (tail)

        #detach from it's current location
        self.remove(node)

        #reattach at end
        self.add_to_tail(node)

        return node.val

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def add_to_tail(self, node):
        prev_temp = self.tail.prev

        node.next = self.tail
        node.prev = prev_temp

        self.tail.prev = node
        prev_temp.next = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value

            node = self.cache[key] #want to move this node to MRU (tail)

            #detach from it's current location
            self.remove(node)

            #reattach at end
            self.add_to_tail(node)

        else:
            new_node = ListNode(key=key, val=value)
            self.add_to_tail(new_node)
            self.cache[key] = new_node
        
            if len(self.cache) > self.capacity:
                
                node = self.head.next
                self.cache.pop(node.key)
                self.remove(node)

