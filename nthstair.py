#http://www.geeksforgeeks.org/count-ways-reach-nth-stair/
#A program to count number of ways to reach n't stair when
# a person can climb either 1 or 2 stairs at a time
'''
plain vanilla recursive solution
'''
def countWays(n,m):
    if n < 1:
        return 0
    res = 1
    for i in range(1,n+1) and range(1,m+1):
        res += countWays(n-i, m)

    return res

n = 13
m = 5

print countWays(n, m)

