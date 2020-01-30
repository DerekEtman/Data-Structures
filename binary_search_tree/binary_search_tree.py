from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the root value
        # if the value is greater than the root value
        # print(f"initial value {self.value}")
        # if not self.value:
        #     self.value = BinarySearchTree(value)
        #     return self.value

        if self.value < value:
            # 
            if not self.right:
                # store the value to the right
                self.right = BinarySearchTree(value)
                # return

            else:
                # if theres a child already repeat the process on that child
                # self.value = self.right
                # return self.insert(value)
                return self.right.insert(value)

        # elif the value is less than the root value
        if  self.value > value: 
            if not self.left:
                self.left = BinarySearchTree(value)
                return
            # if there's a child already repeat the process on that child
            # store the value to the left
            else:
                # if theres a child already repeat the process on that child
                # self.value = self.left
                # return self.insert(value)
               return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check to see if target is equal to root
        if self.value == target:
            # if yes return true
            return True
        # else
        else:
            # if target is larger than current value
            if target > self.value:
                # if right node == None
                if not self.right:
                # return False
                    return False
                else:
                # move to the right node and check again
                    # self.value = self.right
                    return self.right.contains(target)
            # elif target is smaller than current value
            else:
                # if left node == None
                if not self.left:
                # return False
                    return False
                else:
                    # self.value = self.left
                # move to the left node and check again
                    return self.left.contains(target)

        # Return the maximum value found in the tree
    def get_max(self):
        # current_largest = 0
        # print(f"Current_largest {current_largest}")

        # if self.value > current_largest:
        #     # current_largest = self.value
        #     # self.value = self.right
        #     return self.right.get_max()
        # else:
        #     return current_largest


        if not self.right:
            return self.value
        else:
            return self.right.get_max()

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach


    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
