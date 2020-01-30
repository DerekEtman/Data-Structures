# from dll_stack import Stack
# from dll_queue import Queue
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
        if not self.value:
            self.value = value
            return self.value

        elif self.value < value:
            # 
            if self.right == None:
                # store the value to the right
                # print(f"first self.value {self.value}, value {value}")
                self.right = value
                # print(f"value: {value}, Self.value: {self.value}")
            else:
                # if theres a child already repeat the process on that child
                self.value = self.right
                # return self.insert(value)
        # elif the value is less than the root value
        elif  self.value > value: 
            if not self.left:
                self.left = value
            # if there's a child already repeat the process on that child
            # store the value to the left
            else:
                # if theres a child already repeat the process on that child
                self.value = self.left
                # return self.insert(value)
        return

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
                if self.right == None:
                # return False
                    return False
                else:
                # move to the right node and check again
                    self.value = self.right
                    return self.contains(target)
            # elif target is smaller than current value
            else:
                # if left node == None
                if self.left == None:
                # return False
                    return False
                else:
                    self.value = self.left
                # move to the left node and check again
                    return self.contains(target)

        # Return the maximum value found in the tree
    def get_max(self):
        current_largest = 0
        # print(f"Current_largest {current_largest}")

        if self.value > current_largest:
            current_largest = self.value
            self.value = self.right
            return self.get_max()
        else:
            return current_largest

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach


    def for_each(self, cb):
        pass

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
