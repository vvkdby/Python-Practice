#http://pythonhosted.org/llist/
#llist saves all the references, hence insertion at either end is O(1)
#popleft is O(1) while popright is O(n)



from LinkedList import Node
from LinkedList import UnderorderedList

#k-th from the end , recursive solution
def GetNode(head, position):
    if head == None:
        return 0

    index = GetNode(head.next, position) + 1

    if index == position:
        print head.data

    return index


n = Node(5)
n.next = Node(6)
n.next.next = Node(7)


GetNode(n, 2)

#adding two numbers represented as linked list in reverse(i.e head is the LSB)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = None
        temp = None
        head = None
        carry = 0
        while l1 is not None or l2 is not None:
            fdata = 0 if l1 is None else l1.val
            sdata = 0 if l2 is None else l2.val
            Sum = carry + fdata + sdata

            carry = 1 if Sum >= 10 else 0

            Sum = Sum if Sum < 10 else Sum%10

            temp = ListNode(Sum)

            if head is None:
                head = temp
            else:
                prev.next = temp

            prev = temp
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            #this takes care of the last case when the carry is in the alast digit
            if carry > 0:
                temp.next = ListNode(carry)

        return head




#add two numbers represented as linked list in proper order (head is the MSB)
#http://www.geeksforgeeks.org/sum-of-two-linked-lists/
#Following are the steps.
#1) Calculate sizes of given two linked lists.
#2) If sizes are same, then calculate sum using recursion. Hold all nodes in recursion call stack till the rightmost node, calculate sum of rightmost nodes and forward carry to left side.
#3) If size is not same, then follow below steps:
#….a) Calculate difference of sizes of two linked lists. Let the difference be diff
#….b) Move diff nodes ahead in the bigger linked list. Now use step 2 to calculate sum of smaller list and right sub-list (of same size) of larger list. Also, store the carry of this sum.
#….c) Calculate sum of the carry (calculated in previous step) with the remaining left sub-list of larger list. Nodes of this sum are added at the beginning of sum list obtained previous step.


# Adds two linked lists of same size represented by head1 and head2 and returns
# head of the resultant linked list. Carry is propagated while returning from
# the recursion
def addSameSize(head1, head2, carry):
    #check if the lists are empty
    if head1 is None:
        return None

    result = Node()

    result.next = addSameSize(head1.next, head2.next, carry)

    sum = head1.data + head2.data + carry
    carry = sum/10
    sum = sum%10

    result.data = sum

    return result

#This function is called after the smaller list is added to the bigger
#lists's sublist of same size.  Once the right sublist is added, the carry
#must be added to left side of larger list to get the final result.

def addCarrytoRemaining(head1, curr, carry, result):
    result = Node()

    if head1 != curr:
        addCarrytoRemaining(head1.next, curr, carry)

        sum = head1.data + carry
        carry = sum/10
        sum = sum%10

        UnderorderedList.add(result, sum)





# finding the merge point/intersection of two linked lists

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def FindMergeNode(headA, headB):
    traverse1 = Node()
    traverse2 = Node()
    traverse1 = headA
    traverse2 = headB
    lenA = 0
    lenB = 0
    while traverse1 != None:
        lenA += 1
        traverse1 = traverse1.next
    while traverse2 != None:
        lenB += 1
        traverse2 = traverse2.next
    traverse1 = headA
    traverse2 = headB
    if lenA > lenB:
        extra = lenA - lenB
        while extra:
            extra -= 1
            traverse1 = traverse.next
    else:
        if lenB > lenA:
            extra = lenB - lenA
            while extra:
                extra -= 1
                traverse2 = traverse2.next

    while traverse1 != traverse2:
        traverse1 = traverse1.next
        traverse2 = traverse2.next

    return traverse1.data

