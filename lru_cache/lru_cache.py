import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, 
    the current number of nodes it is holding, 
    a doubly-linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.items_holding = 0
        self.DoublyLinkedList = DoublyLinkedList()
        self.storage = {}



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            element = self.storage[key]
            self.DoublyLinkedList.move_to_front(self.storage[key])
            return self.element[key].value[1]
        else:
            return None

        

    """
    Adds the given key-value pair to the cache. 
    The newly-
    added pair should be considered the most-recently used
    entry in the cache. 
    If the cache is already at max capacity
    before this entry is added, 
    then the oldest entry in the cache needs to be removed to make room. 
    Additionally, in the case that the key already exists in the cache, 
    we simply want to overwrite the old value associated with the key with the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage.keys():
            self.storage[key].value = (key, value)
            self.DoublyLinkedList.move_to_front(self.storage[key])
            return self.storage[key]
        elif key not in self.storage.keys():
            self.items_holding += 1
            self.storage[key] = self.DoublyLinkedList.add_to_head([key, value])

            if self.items_holding > self.limit:
                self.items_holding -= 1
                least_used = self.DoublyLinkedList.remove_from_tail()
                del self.storage[least_used.value[0]]


            return self.storage[key]
