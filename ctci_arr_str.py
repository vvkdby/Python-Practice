#function to rotate a 2 dimensional array by 90 degrees
def rotatearray(arr, n):
    for layer in range(n/2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            #save the top element
            top = arr[first][i]
            #left to top
            arr[first][i] = arr[last-offset][first]
            #bottom to left
            arr[last-offset][first] = arr[last][last - offset]
            #right to bottom
            arr[last][last - offset] = arr[i][last]
            #top tp right
            arr[i][last] = top


    return arr

array = [[1,2,3], [4,5,6], [7,8,9]]

#print rotatearray(array, 3)

#function to check if a string is a substring to another, and then using this
# telling if a string is a rotated version of another

def isRotatation(base, test):

    str = ''.join([base,base])

    if test in base:
        return True
    else:
        False




#function to check if the edit distance between two strings is 1 (vs not one)
# Returns true if edit distance between s1 and s2 is
# one, else false
def isEditDistanceOne(s1, s2):

    # Find lengths of given strings
    m = len(s1)
    n = len(s2)

    # If difference between lengths is more than 1,
    # then strings can't be at one distance
    if abs(m - n) > 1:
        return False

    count = 0    # Count of isEditDistanceOne

    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return False

            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1

            # Increment count of edits
            count+=1

        else:    # if current characters match
            i+=1
            j+=1

    # if last character is extra in any string
    if i < m or j < n:
        count+=1

    return count == 1



