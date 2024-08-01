class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

class LRU:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node("Head", "Head")
        self.tail = Node("Tail", "Tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def add_next_to_head(self, node):
        head_neigh = self.head.next
        head_neigh.prev = node
        node.next = head_neigh
        self.head.next = node
        if node.next:
            node.next.prev = node



        return

    def get(self, key):

        if key in self.hash_map:
            node = self.hash_map[key]

            self.remove_node(node)

            self.add_next_to_head(node)

            return node.value
        else:
            return -1


    def put(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.remove_node(node)
            self.add_next_to_head(node)

        else:
            if self.capacity == len(self.hash_map):
                # delete tail
                print("cap")
                node_to_be_removed = self.tail.prev
                self.remove_node(node_to_be_removed)
                del self.hash_map[key]
                del node_to_be_removed

            node = Node(key,value,None, None)
            self.hash_map.update({key:node})
            self.add_next_to_head(node)


        return 1


    def __print_cache(self):
        node = self.head.next
        while node:
            print(node.value, "  ")
            node=node.next


lru = LRU(3)
lru.put(1,1)
lru.put(1,11)
lru.put(2,2)
lru.put(3,3)
lru.put(4,4)

lru.get(3)