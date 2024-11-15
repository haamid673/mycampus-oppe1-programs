# There are five boxes arranged from left to right. You keep adding a variable number of coins sequentially in each box. Start from box-1 and keep going right. Once you reach the last box, head back to box-1 and then 
# keep adding coins. In any given turn, the number of coins added to a box is always less than 10

# Find the box which has the maximum number of coins. If there are two boxes which have the same maximum
# number of coins, output the smaller of the two box numbers. The sequence of coins is represented by a string.
# For example, if the input is 3972894910, this is how coins are added:

# Box   Coins
#1      3 + 9 = 12
#2      9 + 4 = 13
#3      7 + 9 = 16
#4      2 + 1 = 3
#5      8 + 0 = 8

# In this case, 3 is the output as box-3 has the maximum number of coins in it.


A=input ()
B= []
for i in range (1,6):
    B.append (0)
for i in range(len(A) ):
    B[i%5]+=int(A[i])
print(B.index(max(B))+1)


#input, for, append, 