class BTN(): # BTN stands for binary tree node
    def __init__(self, val, left=None, right=None):
        self.__val = val
        self.__left = left
        self.__right = right

    def get_val(self):
        return self.__val
    
    def get_left(self):
        return self.__left
    
    def get_val(self):
        return self.__right
    
    def set_val(self, val) -> None:
        self.__val = val

    def set_left(self, left) -> None:
        #
        if isinstance(left, BTN):
            self.__left = left
        else:
            self.__left = BTN(val=left)
    
    def set_right(self, right) -> None:
        if isinstance(right, BTN):
            self.__right = right
        else:
            self.__right = BTN(val=right)
    
    def is_leaf(self) -> bool:
        return not self.__left and not self.__right
    
    def height(self) -> int:
        # return the height of the tree.
        if self.is_leaf():
            return 1
        return 1 + max(self.__left.height(),self.__right.height())
    
    def count(self) -> int:
        # return the number of nodes from the current BTN.
        # if the current BTN is the root, the count will return the number of all BTNs.
        if self.is_leaf():
            return 1
        return 1 + self.__left.count() + self.__right.count()
    
    def invert(self) -> None:
        # the function inverts the tree
        temp = self.__left
        self.__left = self.__right
        self.__right = temp

        self.__left.invert()
        self.__right.invert()