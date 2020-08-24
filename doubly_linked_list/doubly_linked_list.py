"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        current = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            current.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        current = self.head
        if self.head.next is not None:
            self.length -= 1
            self.head.next.prev = None
            self.head = self.head.next
            return current.value
        else:
            self.length -= 1
            self.head = None
            self.tail = None
            return current.value
    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        current = self.tail
        if current is None:
            self.head = new_node
            self.tail = new_node
        new_node.prev = current
        self.tail.next = new_node
        self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        current = self.tail
        if self.tail.prev is not None:
            self.length -= 1
            current.prev.next = None
            self.tail = current.prev
            return current.value
        else:
            self.length -= 1
            self.head = None
            self.tail = None
            return current.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is not self.head:
            if node is self.tail:
                node.prev.next = None
                self.tail = node.prev
                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = self.head
                self.head.prev = node
                node.prev = None
                self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is not self.tail:
            if node is self.head:
                node.next.prev = None
                self.head = node.next
                node.prev = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev = self.tail
                self.tail.next = node
                node.next = None
                self.tail = node
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                self.head = node.next
                node.next.prev = None
            elif node is self.tail:
                self.tail = node.prev
                node.prev.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value


