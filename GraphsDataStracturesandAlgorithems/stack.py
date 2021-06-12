from node import Node
from lists.list import List


class Stack(List):
    def __init__(self, head=None):
        super().__init__(head=head)
    
    def pop(self):
        # the time complexity is still O(1) (constant) because we 
        # remove the head wich will always be in the top of the list
        return self.remove(self.__head.get_val())
    
    def top(self):
        return self.__head.get_val()
    
    def push(self, val):
        return self.set_head(val)
    
    def is_empty(self):
        return self.__lengh == 0
    
    def size(self):
        return self.__lengh