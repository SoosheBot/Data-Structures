"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #To-dos
        #check if empty
        #if empty put node here/at root  
        #else
          #if left doesn't exist
                #create left
            #else
                #leftnode.insert value
            #if right doesn't exist
                #create right
            #else
                #rightnode.insert value
        # if new < node.value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: #value is greater than or equal to
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
           

    # Return True if the tree contains the value
    # False if it does not
    # def contains(self, target):
        #To-dos:
        #check tree for value at the root
        # if root node doesn't have the value, return false and move on
        # check branch on the right
        # if value is in a node on the right return true and break
        #else return false and go check the left node
        #if value is in a node on the left branch return true and break
   

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if target < self.value:
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    # in-class version of get_max using while loop
    def get_max(self):
        while self.right is not None:
            self = self.right
        
        return self.value

    # alternative method to do the get_max
    # def get_max(self):
    #     if self.right:
    #         return self.right.get_max()
    #     else:
    #         return self.value

    # Call the function `fn` on the value of each self
    def for_each(self, fn):
       fn(self.value)
       
       if self.left:
           self.left.for_each(fn)

       if self.right:
           self.right.for_each(fn)

    # Alternative way to write this:
    # def for_each(self, fn):
    #     fn(self.value)
    #     if self.left:
    #         self.left.for_each(fn)
    #     if self.right:
    #         self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every self, starting with the given self,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass