class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
    def enqueue(self,item):
        self.inbox.push(item)
    def dequeue(self):
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()



q=queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
a = q.dequeue()
print a



"""
s = Stack()
s.push('hello')
s.push('true')
print(s.pop())
"""


