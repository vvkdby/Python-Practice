
def SimpleArraySum(n,s):
    return sum(s)

#read in the number of numbers
count = int(raw_input())
#by default, the following command reads this as list elements
nums = raw_input().split()
nums = map(int,nums)
summation = SimpleArraySum(count,nums)
print summation


