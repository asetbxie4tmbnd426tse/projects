from node import Node

class List:

    def __init__(self, head = None):
        self.__head = Node(head) if head is not None else head
        self.__lengh = 1 if head is not None else 0
    # It is better to create an attribute that hold the list's lenth and incrament every time we add a node.
    # We can have a constent time (O(1)) insted of linear time (O(n))
    # def lengh(self):
    #    ret = 0
    #    n = self.__head
    #    while n is not None:
    #        ret += 1
    #        n = n.get_next()
    #    return ret

    def __str__(self) -> str:
        temp = self.__head
        ret = ""
        while temp is not None:
            ret = ret + str(temp.get_val()) + ", "
            temp = temp.get_next()
        return f"[{ret[:-2]}]"

    def get_head(self):
        return self.__head
    
    def get_lengh(self):
        return self.__lengh
    
    def __increment_lengh(self) -> None:
        self.__lengh += 1
  
    def __set_head(self, val):
        n = Node(val, next=self.__head)
        self.__head = n
        return self.__head

    def __add_after(self, val, after_node: Node):
        # this funtion is a utility for add, and shoud only by used privetly.
        # the function adds a no
        # val is the value of the node we add. after_node is the node we want to add after
        # the function returns the node before the node we added
        n = Node(val)
        temp = after_node.get_next()
        after_node.set_next(n)
        n.set_next(temp)
        return after_node
    
    def set_head(self, val):
        # the function returns the new head
        ret = Node(val)
        ret.set_next(self.__head)
        self.__head = ret
        self.__increment_lengh()
        return ret

    def insert(self, position, val):
        # position is 0 based or the node to be next to. val is the value of the node we add
        # the function returns the node we added or will print the a massage
        try:
            if isinstance(position, Node):
                ret = self.__add_after(val, position)
                self.__increment_lengh()
            else:
                temp=self.__head
                for i in range(0, position):
                    temp = temp.get_next()
                ret = self.__add_after(val, after_node=temp)
                self.__increment_lengh()
            return ret
        except Exception:
            print("position must be a type of int or Node. Also position must be lower or equal to the list lengh")
    
    def append(self, val):
        # the function adds a node to the end of list, and returns the node we added
        temp=self.__head
        while temp.get_next() is not None: # i decided to use while instead of for loop, even though we have the lengh of 
            temp=temp.get_next()           # the list, to ensure proper resolt and remove unnecessary depandencise(in case there 
        temp.set_next(Node(val))           # was a defect with the counting of the lengh).
        self.__increment_lengh()
        return temp.get_next()
    
    def remove(self, val=None, appearance=1):
        # the function removes the node with the value of val. by difualt it will remove the first appearance, but it can be change.
        # the function returns the node we removed. if such node is not found,
        # the function will return None.
        temp=self.__head
        if temp.get_val() == val:
            if appearance == 1:
                self.__head=self.__head.get_next()
                temp.detach()
                return temp
            appearance -= 1
        
        while temp is not None:
            if temp.get_val() == val:
                if appearance == 1:
                    break
                appearance -= 1
            prev = temp
            temp= temp.get_next()
        
        prev.set_next(temp.get_next())
        temp.detach()
        return temp


    def clone(self):
        ret = List(self.__head.get_val())
        n=self.__head.get_next()
        while n.get_next() is not None:
            ret.append(n.get_val())
        return ret
    
    def reverse(self) -> None:
        # the function recverses the list
        n = self.__head
        prev = None
        while n is not None:
            temp = n.get_next()
            n.set_next(prev)
            prev = n
            n = temp

