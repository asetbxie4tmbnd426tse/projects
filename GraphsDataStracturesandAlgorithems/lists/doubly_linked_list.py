from node import Node

class DLList:

    def __init__(self, head = None):
        self.__head = Node(head) if not head else head
        self.__tail = head
        self.__lengh = 1 if not head else 0
    # It is better to create an attribute that hold the list's lenth and incrament every time we add a node.
    # We can have a constent time (O(1)) insted of linear time (O(n))

    def __str__(self) -> str:
            temp = self.__head
            ret = ""
            while temp is not None:
                ret = ret + str(temp.get_val()) + ", "
                temp = temp.get_next()
            return f"[{ret[:-2]}]"

    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def get_lengh(self):
        return self.__lengh
    
    def __increment_lengh(self) -> None:
        self.__lengh += 1
  
    def __set_head(self, val):
        n = Node(val, next=self.__head)
        self.__head.set_prev(n)
        self.__head = n
        return self.__head
    
    #def set_tail

    def __add_after(self, val, after_node: Node):
        # this funtion is a utility for add, and shoud only by used privetly.
        # the function adds a no
        # val is the value of the node we add. after_node is the node we want to add after
        # the function returns the node before the node we added
        n = Node(val)
        temp = after_node.get_next()
        after_node.set_next(n)
        n.set_prev(after_node)
        n.set_next(temp)
        temp.set_prev(n)
        return after_node
    
    def set_head(self, val):
        # the function returns the new head
        ret = Node(val)
        ret.set_next(self.__head)
        self.__head = ret
        self.__increment_lengh()
        return ret

    def insert(self, position, val):
        # position is 0 based index or Node. val is the value of the node we add
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
            print("position must be a type of int or node. Also position must be lower or equal to the list lengh")
    
    def append(self, val):
        # the function adds a node to the end of list, and returns the node we added
        n = Node(val,prev=self.__tail)
        self.__tail.set_next(n)
        self.__tail = n
        return n

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
        temp.get_next().set_prev(prev)
        temp.detach()
        return temp
    
    def remove_tail(self):
        # this function's main purpse is to be a dequeue when i implement a queue
        ret = self.__tail
        self.__tail = self.__tail.get_prev()
        ret.detach()
        return ret

    def clone(self):
        ret = DLList(self.__head.get_val())
        n=self.__head.get_next()
        while n.get_next() is not None:
            ret.append(n.get_val())
        return ret
