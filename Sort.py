def insertion_sort(array):
    n = len(array)
    for i in range(n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

def difference(array):
    printing_arr = []
    insertion_sort(array)
    n = len(array)
    diff_min = array[n-1] - array[n-2]
    i = 1
    while i <= n-1:
        #print i
        diff = abs(array[i]-array[i-1])
        #print diff
        if diff < diff_min:
            diff_min = diff
        i += 1
    return diff_min

def find_diff_min(array):
    diff_min = difference(array)
    n = len(array)
    printing_arr = []
    for i in range(n-1):
        diff = abs(array[i]-array[i+1])
        if diff == diff_min:
            printing_arr.append(array[i])
            printing_arr.append(array[i+1])
    return printing_arr

N = int(raw_input())
arr = map(long,raw_input().split(' '))
insertion_sort(arr)
print arr
print difference(arr)
printing_arr = find_diff_min(arr)
print ' '.join(map(str,printing_arr))
#print printing_arr