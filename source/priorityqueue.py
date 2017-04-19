#!python

from heap import MinHeap


class PriorityQueue(object):

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize a new binary min heap to store the items
        self.heap = MinHeap()

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.size(), self.front())

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        # TODO: Insert given item into heap
        ...

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        if self.size() < 1:
            return None
        else:
            # TODO: Return min item from heap, if any
            ...

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        if self.size() < 1:
            raise ValueError('Priority queue is empty and has no front item')
        else:
            # TODO: Remove and return min item from heap, if any
            ...

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority."""
        if self.size() < 1:
            raise ValueError('Priority queue is empty and has no front item')
        else:
            # TODO: Replace and return min item from heap, if any
            ...
