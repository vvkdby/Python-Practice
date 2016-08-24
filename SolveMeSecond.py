def SolveMeSecond(a,b):
    return a+b

n = int(raw_input())

for i in range(0,n):
    a,b = (raw_input().split())
    print type(a)
    #Q.can this be done in one command itself? like this : int(raw_input().split())?
    #A.no. because the output raw_input().split is a 'list', with the individual elements being
    #of the type 'str'
    a,b = int(a),int(b)
    #print type(a)
    #a,b = map(int,raw_input().split()) >>> map(function, sequence) calls function(item)
    # for each of the sequence’s items and returns a list of the return values.
    res = SolveMeSecond(a,b)
    print res





