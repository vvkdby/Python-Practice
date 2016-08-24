'''
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example, length of LIS for
{ 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}
'''

#following is a solution using the tabulation method

def lis(arr):

    n = len(arr)

    lis = [1]*n

    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)



arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is", lis(arr)
