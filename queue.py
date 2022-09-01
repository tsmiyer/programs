#  Queue Data structure: FIFO(First in First Out)
# Abstract Data type:
# Operations :
#               Joining a Queue (at the end or the rear end)   (enqueue)
#               Serving an entry in a queue                    (deque)
# We use a list based implementation of the abstract data type: Queue


class Empty(Exception):
    pass  # no operation


class Queue:  # UNBOUNDED QUEUE only limited by memory; no wraparound
    # in enqueue
    # constructor
    def __init__(self):
        # Create an empty queue
        self._data = []  # nonpublic list instance

    def __len__(self):
        # Return the number of elements in the queue
        return len(self._data)

    def is_empty(self):
        # Return True if the queue is empty
        return len(self._data) == 0

    # get front element in the Queue       getter function
    # the front element in the Queue is not removed.
    def front(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            return (self._data[0])

    # deque operation
    def deque(self):
        # should we raise an empty Queue exception, here too? if Queue is empty??
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            return self._data.pop(0)

    # enqueue operation assuming that Queue is unbounded
    def enqueue(self, e):
        return self._data.append(e)

Q=Queue()
Q.enqueue(5)
Q.enqueue(4)
Q.enqueue(9)
Q.enqueue(7)
print(len(Q))
print(Q.front())
print(Q.deque())
print(Q.front())
print(len(Q))
print(Q.deque())
print(Q.front())
print(len(Q))
print(Q.deque())
print(Q.front())
print(len(Q))

