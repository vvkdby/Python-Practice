"""
The list methods make it very easy to use a list as a stack,
where the last element added is the first element retrieved (“last-in, first-out”).
To add an item to the top of the stack, use append(). To retrieve an item from the
top of the stack, use pop() without an explicit index.
"""
"""
It is also possible to use a list as a queue, where the first element added is the first element retrieved
(“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the
 end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other
 elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.
"""


"""
https://docs.python.org/2/library/heapq.html
"""
