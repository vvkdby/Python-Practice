# In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2.
# The former is floating point division, and the latter is floor division,
# sometimes also called integer division. In Python 2.2 or later in the 2.x line,
# there is no difference for integers unless you perform a from __future__ import
# division, which causes Python 2.x to adopt the behavior of 3.0

"""from __future__ import division
print((6/3) == (7/3))

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)"""

#Enter your code here. Read input from STDIN. Print output to STDOUT


"""n = int(raw_input())
Matrix = [[0 for x in range(n)] for x in range(n)]
Matrix[j][:] = [[str(i) for i in str(raw_input())] for j in range(n)]
Matrix = Matrix[n-1][:]
indices_matrix = [[0 for x in range(2)] for j in range(n**2)]
count = 0

def cavity_test(Matrix , index1,index2):
    if (int(Matrix[index1][index2]) > int(Matrix[index1-1][index2]) and int(Matrix[index1][index2]) > int(Matrix[index1+1][index2]) and int(Matrix[index1][index2]) > int(Matrix[index1][index2-1]) and int(Matrix[index1][index2]) > int(Matrix[index1][index2+1]) )== True:
        print (int(Matrix[index1][index2]) > int(Matrix[index1-1][index2]) and int(Matrix[index1][index2]) > int(Matrix[index1+1][index2]) and int(Matrix[index1][index2]) > int(Matrix[index1][index2-1]) and int(Matrix[index1][index2]) > int(Matrix[index1][index2+1]))
        return True
    else:
        return False
print(cavity_test(Matrix,2,2))
for i in range(1,n-1):
    for j in range(1,n-1):
        if cavity_test(Matrix,i,j) == True:
            indices_matrix[count][:] = [i,j]
            count = count + 1
#print indices_matrix
for i in range(len(indices_matrix)):
    if indices_matrix [i][0]!= 0:
        Matrix[indices_matrix[i][0]][indices_matrix[i][1]] = 'X'

for i in range(n):
    print (''.join(Matrix[i][:]))"""

"""import numpy as np
arr = np.empty((3,2), dtype = int )
arr[0] = raw_input().split()
arr[1] = raw_input().split()
arr[2] = raw_input().split()

b = np.empty((2,2),dtype= int )
b[0] = raw_input().split()
b[1] = raw_input().split()
print (arr[0:1][0:1] - b) == [0]"""

"""
# Response for grid search
import numpy as np
# we would need np arrays for fast matrix operations
T = int(raw_input())

def search_grid(x, y):
    rowx, colx = x.shape
    rowy, coly = y.shape
    flag = False
    print rowx,rowy,colx,coly
    for i in range((rowx - rowy + 1)):
        for j in range((colx - coly + 1)):
            # we need to slice a part of matrix x that is of
            # the same size as matrix y.
            #x_slice = x[np.ix_([i,i+rowy ],[j,j+coly])]
            x_slice = x[i:i+rowy ,j:j+coly ]
            print type(np.asarray(x_slice)), type(np.zeros(rowy,coly))
            if np.asarray(x_slice) - y == np.zeros(rowy , coly):
                flag = True
    return flag


for i in range(T):
    rowA, colA = map(int, raw_input().split())
    # initializing A as an empty np array
    A = np.empty((rowA,colA), dtype = int)
    # now reading the elements into the Matrix A, row-wise.
    for j in range(rowA):
        A[j] = map(int,str(raw_input()))
    rowB, colB = map(int, raw_input().split())
    # initialize B as an empty np array
    B = np.empty((rowB,colB),dtype = int)
    # again, reading B row wise
    for j in range(rowB):
        B[j] = map(int,str(raw_input()))
    if search_grid(A,B) == True:4
        print 'YES'
    else:
        print 'NO'
"""

"""
arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

def sum_array(grid):
    s = sum(map(sum, grid))
    return int(s)

def getsubgrid(x1, y1, x2, y2, grid):
    return [item[x1:x2] for item in grid[y1:y2]]

def hourglass_sum(grid):
    hr_sum = sum_array(grid)
    return (hr_sum - grid[1][0] - grid[1][2])

sum_max = -20000
for i in range(4):
    for j in range(4):
        sub_matrix = getsubgrid(i,j,i+3,j+3,arr)
        total = hourglass_sum(sub_matrix)
        if total > sum_max:
            sum_max = total

print sum_max
"""
"""
def seq_num(x,lastans,N):
    return (x^lastans)%N

[N,Q] = map(int, raw_input().split(' '))
# initialize the list of lists as empty arrays
#lists = [[]]*N
#this won't work because all these lists are the reference to the same object and hence whenever you append an element,
#it gets appended to all the sub-lists
lists = [[] for i in range(N)]
lastans = 0
#begin the loop and analyze each case:
for i in range(Q):
    [a,x,y] = map(int, raw_input().split(' '))
    # a decides what type of input it is
    if a == 1:
        lists[seq_num(x,lastans,N)].append(y)
    else:
        size = len(lists[seq_num(x,lastans,N)])
        lastans = lists[seq_num(x,lastans,N)][y%size]
        print lastans
"""
"""
import string
string_in = raw_input()

set_alphabets = set(string.lowercase)

set_string = set(string_in.lower())

if len(set_alphabets.difference(set_string)) == 0:
    print 'pangram'
else:
    print 'not pangram'
    """
"""
N = int(raw_input())
string_list = [[] for _ in range(N)]
for i in range(N):
    str = raw_input()
    string_list[i].append(str)

common = set(string_list[0])
for i in range(0, N):
    common = common.intersection(string_list[i])
    print common
print len(common)
"""
"""
T = int(raw_input())
count = 0
for i in range(T):
    string_in = raw_input()
    if len(string_in) %2 == 1:
        print -1
    else:
        str1 = string_in[:(len(string_in)/2)]
        str2 = string_in[(len(string_in)/2):]
        set_all = list(set(string_in))
        print set_all
        for j in range(len(set_all)):
            count1 = str1.count(set_all[j])
            count2 = str2.count(set_all[j])
            if (count1 - count2) > 0:
                count += abs(count1 - count2)
        print count
"""
"""
N = int(raw_input())
#convert N to binary
binN = "{0:b}".format(N)
print binN
gap = []
count = 0
found = False
for i in range(1,len(binN)):
    if binN[i-1] == 1 and binN[i] == 0:
        found = True
    if binN[i-1] == 0 and binN[i] == 1:
        found = False
        count += 1
        gap.append(count-1)
        count = 0
    if found==True:
        count += 1
    print count
print gap
"""
"""
import sys
import numpy as np


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
arr = np.array(arr)
total = 0
for i in range(4):
    for j in range(4):
        new_mat = 1*arr[i:(i+3),j:(j+3)]
        new_mat[1,0] = 0
        new_mat[1,2] = 0
        total_new = (new_mat.sum()).sum()
        if total_new > total:
            total = total_new
print total
"""
"""
def sumlist(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + sumlist(numlist[1:])

print(sumlist([1,3,5,7,9]))
"""
"""
def rev_str(str):
    if len(str) == 1:
        return str
    else:
        return (rev_str(str[1:]) + str[0]).
print(rev_str("ppppriyaaaa"))
"""
"""
def pal_check(str):
    if str == '':
        return True
    else:
        if ord(str[0]) == ord(str[len(str)-1]):
            return pal_check(str[1:len(str)-1])
        else:
            return False
print(pal_check('aabaa'))
"""
"""
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
"""

"""
def plusOne(A):
    digit = A[len(A)-1]
    if digit < 9:
        A[len(A)-1] = digit + 1
        return A
    else:
        A[len(A)-1] = 0
        plusOne(A[0:len(A)-1])
        return A
print  plusOne([1,2,9])

"""
"""
A = [1,2,3,4]

rt_sum = [0]*len(A)
lf_sum = [0]*len(A)
rt_sum[0] = A[0]
for i in range(1,len(A)):
    rt_sum[i] = rt_sum[i-1] + A[i]

lf_sum[len(A)-1] = A[len(A)-1]
for i in range(1, len(A)):
    lf_sum[len(A) - 1 - i] = lf_sum[len(A)-i] + A[len(A) - 1 - i]

print rt_sum
print lf_sum

"""
"""
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
"""

"""
Adil's twitter question
T = int(raw_input())
arr = []
for i in range(T):
   k = int(raw_input())
   arr.append(k)

dict_list = {}

for i in range(T):
   dict_list[arr[i]] = arr.count(arr[i])
arr_before = []
for i in range(T):
   if dict_list[arr[i]] > 1:
      arr_before.append(1)
      dict_list[arr[i]] =- 1
   else:
      arr_before.append(0)

print "".join([str(i) for i in arr_before])

"""



