# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.reverse()
l2.reverse()
print(l2)
print(l1)
l3=lambda x,y:[x+y for x,y in map(x,y)]
print(l3(l1,l2))
