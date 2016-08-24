
'''
recursive implementation of binary search
'''
def binarySearch(arr, l, r, x):

    #check base case
    if r >= l:

        mid = l + (r - l)/2

        #if the element is present at the middle itself
        if arr[mid] == x:
            return mid

        #if the element is smaller than the middle element,
        #it must be present in the left half of the array
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"


'''
iterative implementation of binary search
'''


def iterativeBinarySearch(arr, l, r, x):

    while l <= r:

        mid = l + (r-l)/2

        #check if x is present at mid
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
             r = mid - 1

    return - 1




arr = [ 2, 3, 4, 10, 40 ]
x = 10

index = iterativeBinarySearch(arr, 0, len(arr)-1, x)

if index != -1:
    print "Element is present at index %d" % index
else:
    print "Element is not present in array"