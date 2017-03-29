#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        pass

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        pass

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Push given item
        pass

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        pass

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        pass


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        pass

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        pass

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Insert given item
        pass

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        pass

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        pass


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
