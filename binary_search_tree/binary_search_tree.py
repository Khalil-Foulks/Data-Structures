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
from queue import Queue 
from stack import Stack 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # left case?
        # check if the value is less than the root value?
        if value < self.value:
            # move to the left and check if it is none?
            if self.left == None:
                # insert node here
                new_node = BSTNode(value)
                self.left = new_node
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right case?
        if value >= self.value:
        # otherwise
            # move to the right and check if it is none?
            if self.right == None:
                # insert the node here
                new_node = BSTNode(value)
                self.right = new_node
            # otherwise
            else:
                # call insert on the root's right node
                self.right.insert(value)   
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if the node is == target
        if self.value == target:
            # if true return true
            return True
        # otherwise check if target is < node value
        elif target < self.value:
            # if left is None, target doesn't exist in tree, return false
            if self.left == None:
                return False  
            # if left value is = target return true
            elif self.left.value == target:
                return True
            # otherwise move down left, call contains on left node
            else:
                self.left.contains(target)
        # otherwise check if target is >= node value
        elif target > self.value: 
            # if right is None, target doesn't exist in tree, return false
            if self.right == None:
                return False  
            # if right value is = target return true
            elif self.right.value == target:
                return True
            # otherwise move down right, call contains on right node
            else:
                self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # run the function passing in the value of the node
        fn(self.value)

        #if left is not none run for each on left
        if self.left != None:
            # call function on left
            self.left.for_each(fn)


        # if right is not None run for each on right
        if self.right != None:
            # call function on right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):

        if self.value is None:
            return
        if self.left:
            self.left.in_order_print()
            
        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        curr_node = self
        # instantiate a queue
        q = Queue()
        # enqueue our starting node (self)
        q.enqueue(curr_node)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue the current node
            curr_node = q.dequeue()
            # print the nodes value
            print(curr_node.value)
            # check if left child exists
            if curr_node.left is not None:
                # enqueue left child
                q.enqueue(curr_node.left)

            # check if right child exists
            if curr_node.right is not None:
                # enqueue right child            
                q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        curr_node = self
        # instantiate a stack
        q = Stack()
        # push our starting node (self)
        q.push(curr_node)
        # while the stack is not empty
        while len(q) > 0:
            # pop the current node
            curr_node = q.pop()
            # print the nodes value
            print(curr_node.value)

            # check if left child exists
            if curr_node.left is not None:
                # push left child
                q.push(curr_node.left)

            # check if right child exists
            if curr_node.right is not None:
                # push right child
                q.push(curr_node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
