class Node:
    
    def __init__(self, val, next = None, prev = None, is_doubly_linked = False):
        # time complexity : O(1). space complexity: O(n), since val is generic, it can deferent inputs of deferent size/
        # for example: to deferent string sizes
        self.__val = val
        self.__next: Node = next
        self.__prev: Node = prev
    
    def get_val(self):
        # time complexity : O(1). space complexity: O(1).

        return self.__val
    
    def get_next(self):
        # time complexity : O(1). space complexity: O(1).
        return self.__next
    
    def get_prev(self):
        # time complexity : O(1). space complexity: O(1).
        return self.__prev
    
    def set_val(self, val) -> None:
        # time complexity : O(1). space complexity: O(1), since val is generic, it can deferent inputs of deferent size.
        # for example: to deferent string sizes
        self.__val = val
    
    def set_next(self, next) -> None:
        # the argument next must be a node
        # time complexity : O(1). space complexity: O(1), since self.__next points to where the next node is stord
        self.__next = next
    
    def set_prev(self, prev) -> None:
        # the argument prev must be a node
        self.__prev = prev
    
    def detach(self) -> None:
        # the function detaches the node from the list, stack, queue is belongs to
        self.__next = None
        self.__prev = None
    
    def clone(self):
        return Node(self.__val, self.__next, self.__prev)