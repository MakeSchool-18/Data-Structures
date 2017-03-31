#!python

from linkedlist import LinkedList


# implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # TODO: Check if empty
        pass

    def length(self):
        """Return the number of items in this queue"""
        # TODO: Count number of items
        pass

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # TODO: Insert given item
        pass

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # TODO: Return front item, if any
        pass

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # TODO: Remove and return front item, if any
        pass


# implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # TODO: Check if empty
        pass

    def length(self):
        """Return the number of items in this queue"""
        # TODO: Count number of items
        pass

    def enqueue(self, item):
        """Insert the given item at the back of this queue"""
        # TODO: Insert given item
        pass

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty"""
        # TODO: Return front item, if any
        pass

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty"""
        # TODO: Remove and return front item, if any
        pass


# implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue
