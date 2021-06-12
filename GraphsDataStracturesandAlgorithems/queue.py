from node import Node
from lists.doubly_linked_list import DLList


class Queue(DLList):
    # i chose doubly linked list in order to have a constant time to the front and back of the queue and constant
    # time when i enqueue and dequeue access 
    def __init__(self, head):
        super().__init__(head=head)
    
    def enqueue(self, val):
        return self.set_head(val)
    
    def dequeue(self):
        return self.remove_tail()
    