from sys import maxint

#kadane's algorithm to calculate the maximum subarray in an array
def kadane(A):
    max_sum = -maxint - 1
    curr_sum = -maxint - 1
    L = 0
    R = 0
    for i in range(len(A)):
        if curr_sum < 0:
            #if sum is negative, reset
            curr_sum = A[i]
            L = i
            R = i
        else:
            #otherwise keep going
            curr_sum += A[i]
            R = i

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print kadane(A)

def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray(A)


'''
max profit stock problem
'''

def getBestTime(stocks):
    min = 0
    maxDiff = 0
    buy = sell = 0
    size = len(stocks)

    for i in range(size):
        if stocks[i] < stocks[min]:
            min = i
        diff = stocks[i] - stocks[min]

        if diff > maxDiff :
            buy = min
            sell = i
            maxDiff = diff

    return buy, sell


stocks = [100, 180, 260, 310, 40, 535, 695]
print getBestTime(stocks)
