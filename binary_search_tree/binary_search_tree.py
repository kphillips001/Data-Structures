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
        # pass
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else: 
            # Else ????
                # Repeat the process on left subtree
                self.left.insert(value)

        # case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
               # Repeat the process on right subtree 
               self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: Self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: Target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        
        # forget about the left subtree
        # Iterate through the nodes using a loop consruct
        if self.right is None:
            return self.value
        while self.right is not None:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # run on the root node
        fn(self.value)
        # run on every node of the subtree to the left
        if self.left:
            self.left.for_each(fn)
        # run on every node of the subtree to the right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # If the current node is None, we know we've reached the end of a recursion (i.e., base case) and we want to return
        if self is None: 
            return 
        # check if we can "move left"
        if self.left is not None: 
            self.left.in_order_print(node) 
        # once we traverse as far left as we can, "visit" the node by printing its value (visit logic)
        print(self.value)
        # check if we can "move right" 
        if self.right is not None: 
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        # use a queue to form a "line" for the nodes to get in
        queue = Queue()
        # start by placing the root in the queue
        queue.enqueue(node)
        # need a while loop to iterate -- while length of queue is greater than 0
        while queue.__len__() > 0:
            # dequeue item from front of queue
            current = queue.dequeue()
            # print that item
            print(current.value)
            # place current item's left node in the queue if not None
            if current.left: 
                queue.enqueue(current.left)
            # place current item's right node in queue if not None
            if current.right: 
                queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        stack.push(node)
        # while loop to manage iteration -- check length of stack
        # if stack is not empty, enter the while loop
        while stack.size > 0:
            # pop top item off the stack
            current = stack.pop()
            # print that item's value
            print(current.value)
            # if there is a right subtree
            if current.right: 
                # push right item onto stack
                stack.push(current.right)

            # if there is a left subtree
            if current.left:
                # push left item onto stack
                stack.push(current.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if self is None: 
            return

        print(self.value)

        if self.left: 
            self.left.pre_order_dft(node)

        if self.right: 
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self is None: 
            return

        if self.left: 
            self.left.post_order_dft(node)

        if self.right:
            self.right.post_order_dft(node)
        
        print(self.value)