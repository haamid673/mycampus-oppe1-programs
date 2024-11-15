# A sequence of integers of even length is said to be left-heavy if the sum of the terms in the left-half of
# the sequence is greater than the sum of the terms in the right half. It is termed right-heavy if the sum of the 
# second half is greater than the first half. It is said to be balanced if both the sums are equal.


# Accept a sequence of gomma-separated integers as input. Determine if the sequence is left-heavy,
# right-heavy or balanced and print this as the output.


# Input -1,2,3,4,5,6
# output - right-heavy

# input- 1,1,1,1
# output- balanced


A=input().split(",")
B=len (A)//2
left=0
right=0
for i in range (B):
    left+=int(A[i])
    right+=int(A[len(A)-i-1])
if left==right:
    print( 'balanced' )
elif left<right:
    print ('right-heavy')
else:
    print ('left-heavy')