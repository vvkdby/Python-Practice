# -*- coding: utf-8 -*-
'''
#Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits
operations required to convert ‘str1′ into ‘str2′.
#Insert
#Remove
#Replace
#All of the above operations are of equal cost.
#
'''
#naive recursive

def editdistance(str1, str2, m, n):

    if m == 0:
        return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return editdistance(str1, str2, m-1, n-1)

    return 1 + min(editdistance(str1, str2, m, n-1), editdistance(str1, str2, m-1, n), editdistance(str1, str2, m-1, n-1))


str1 = "sunday"
str2 = "saturday"
print editdistance(str1, str2, len(str1), len(str2))



#using tabulation
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]



str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))