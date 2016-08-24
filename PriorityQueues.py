
import Queue as Q  # ver. < 3.0


class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New Level:', description
        return
    #def __cmp__(self, other):
        #return cmp(self.priority, other.priority)

q = Q.PriorityQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    print 'Processing level:', next_level.description

print

import heapq

heap = []
heapq.heappush(heap, (1, 'one'))
heapq.heappush(heap, (10, 'ten'))
heapq.heappush(heap, (5,'five'))

for x in heap:
    print x,
print

heapq.heappop(heap)

for x in heap:
    print x,
print

# the smallest
print heap[0]

print

heap = [(1, 'one'), (10, 'ten'), (5,'five')]
heapq.heapify(heap)
for x in heap:
	print x,
print

heap[1] = (9, 'nine')
for x in heap:
	print x,