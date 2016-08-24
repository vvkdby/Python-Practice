
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)




q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
