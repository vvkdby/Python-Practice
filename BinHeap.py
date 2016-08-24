class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    #for insertion you percolate up
    def percUp(self,i):
        #this while statement justifies why that initial zero was important
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i/2]:
                #compare current node to its parent and swap if heaporder property unsatisfied
                 tmp = self.heapList[i // 2]
                 self.heapList[i // 2] = self.heapList[i]
                 self.heapList[i] = tmp
            i = i//2

    #insert method that uses the percUp method:
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    #we percolate downwards for deletion
    def percDown(self,i):

        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        #check for the last element (one leaf)
        if i*2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      print self.heapList



bh = BinHeap()
bh.buildHeap([9,6,5,2,3])
