# naive recursive algorithm with O(2^n) complexity

def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    if m == 0 or n == 0:
        return 0
    elif str1[m-1] == str2[n-1]:
        return 1 + lcs(str1[:m-1], str2[:n-1])
    else:
        return max(lcs(str1[:m], str2[:n-1]), lcs(str1[:m-1],str2[:n]))

#dynamic programming implementation with O(mn) complexity

def lcsdp(str1, str2):
    m = len(str1)
    n = len(str2)

    #array declaration for storing the DP values
    L = [[None]*(n+1) for i in range(m+1)]


    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of str1[0..i-1]
    and str2[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[m][n]

import time
start = time.time()
X = "AGGTAB"
Y = "GXTXAYB"
print lcs(X,Y)
end = time.time()
print (end-start)
print lcsdp(X,Y)
end2 = time.time()
print (end2-end)



#printing the longest common subsequence
def lcsprint(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]

    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # Following code is used to print LCS
    index = L[m][n]

    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = "\0"

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1

    print "LCS of " + X + " and " + Y + " is " + "".join(lcs)

# Driver program
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
#lcsprint(X, Y, m, n)