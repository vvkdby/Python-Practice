#calculates all permutations of a string
#takes O(n!) time to run

def permutations(word):
    if len(word) <= 1:
        return [word]

    #get all permutations of length n - 1
    perms = permutations(word[1:])
    char = word[0]

    result = []
    #iterate over all the permutations
    for perm in perms:
        #iterate over every possible position where we can insert the first char
        for i in range(len(perms) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result

word = 'vivek'
result = permutations(word)
print result
print len(result)