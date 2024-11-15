# Given a matrix M, your task is to create a new matrix by inserting a column of ones before the first
# column of M. For example, this is the required transformation:

# [1 2 3]     [1 1 2 3]
# [4 5 6]     [1 4 5 6]

#Write a function named add_ones that accepts a matrix M as argument and returns a new matrix by inserting 
# a column of ones before the first column of M.
# (1) The matrix need not be square. 8 # 
# (2) You do not have to accept input from the user or print output to the console. You just have to write 
# the function definition.

# #test cases
# 1. [[1,2,3],[4,5,6]] -> [[1,1,2,3], [1,4,5,6]]
# 2. [[1,2,3],[4,5,6],[7,8,9] --> [[1,1,2,31, [1,4,5,6], [1,7,8,9]]


M=[[1,2,3],[4,5,6],[7,8,9]]
# M=[[1,2,3],[4,5,6]]

def add_ones (M) :
    #your code
    for i in range(len (M)):
        M[i].insert(0,1)
    return M
print(add_ones(M))