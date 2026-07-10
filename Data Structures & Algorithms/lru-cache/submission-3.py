class ListNode: #general listnode class
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key      #for this problem, need to store a key and value 
        self.val = val
        self.prev = prev    #as well as prev, next
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}           #this dict will act as the cache to track the least recently-used nodes

        self.head = ListNode()      #sentinal nodes. Head = LRU
        self.tail = ListNode()      #tail = Most recently-used

        self.head.next = self.tail  #make initial connections to sentinals
        self.tail.prev = self.head

        self.capacity = capacity    #initialize the capacity

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
        if key in self.hashmap:         #check if the input key is already in the cache (hashmap). If yes,
            node = self.hashmap[key]    #get the corresponding node for the key
            self.remove_node(node)      #now we have to update the cache. Remove the node from it's current spot
            self.add_to_front(node)     #and place it at the front

            return node.val             #return the node's value, as requested
        
        return -1           #if the key isn't in the cache, just return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:         #check if key already in the cache. If yes,
            node = self.hashmap[key]    #get the node at the key
            node.val = value            #update the value to the new input value
            self.remove_node(node)
        
        new_node = ListNode(key=key, val=value) #make a node with the key, value
        self.add_to_front(new_node)             #and now add it to the front of the list
        self.hashmap[key] = new_node            #and assign it in cache

        if len(self.hashmap) > self.capacity:   #if we've exceed the capacity after inserting a new node 
            lru_node = self.tail.prev           #get the least recently-used node (tail.prev due to sentinal)
            self.remove_node(lru_node)          #and remove it 
            del self.hashmap[lru_node.key]      #as well as it's place in the cache

# time: O(1) per operation
# space: O(c); c = LRU capacity