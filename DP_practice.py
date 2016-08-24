#given coins of different denominations and a total sum
#to find: minimum number of coins that can be used to amount to S
#0/1 knapsack probelem
import sys
def min_coins_given_sum(Values, Sum):
    min_coins = [sys.maxint]*(Sum+1)
    min_coins[0] = 0
    for i in range(1,Sum+1):
        for j in range(len(Values)):
            if Values[j] <= i :
                sub_res = min_coins[i - Values[j]]
                if sub_res + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - Values[j]] + 1
    return min_coins

#Sum = 11
#Values = [1,3,5]
#print min_coins_given_sum(Values, Sum)

"""
fibonacci tried out with both memoization and tabulation
"""

#memoization

def fib_memo(n, lookup):
    #base case
    if n == 0 or n == 1:
        lookup[n] = 1

    #if value isn't previously calculated, calculate it
    if lookup[n] is None:
        lookup[n] = fib_memo(n-1, lookup) + fib_memo(n-2, lookup)

    #return the value corresponding to n
    return lookup[n]

n = 34
lookup = [None]*(101)
print "Fibonacci Number is ", fib_memo(n, lookup)



#tabulation

def fib_tab(n):
    #array declaration
    f = [0]*(n+1)

    #base case assignment
    f[1] = 1

    #calculating the fibonacci and storing the values
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

n = 9
print "Fibonacci number is " , fib_tab(n)
