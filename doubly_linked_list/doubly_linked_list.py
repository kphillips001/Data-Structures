"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

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
        if current.next != None:
            current.delete()
            self.length -= 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

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
        if current.prev != None:
            current.delete()
            self.length -= 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

        return current.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        moved = node.value
        self.delete(node)
        self.add_to_head(moved)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        moved = node.value
        self.delete(node)
        self.add_to_tail(moved)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        current = self.head
        while current != None:
            if current != node:
                current = current.next
            else:
                if current.next == None and current.prev == None:
                    self.head = None
                    self.tail = None
                    self.length = 0
                elif current.next != None and current.prev == None:
                    self.head = current.next
                    current.delete()
                    self.length -= 1
                elif current.next == None and current.prev != None:
                    self.tail = current.prev
                    current.delete()
                    self.length -= 1
                else:
                    current.delete()
                    self.length -= 1
                return current.value

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


