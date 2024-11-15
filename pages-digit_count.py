# You are given a book that has n pages. The pages of the book are numbered from 1 to n. Each page of the book has a page-number written at the bottom of the page. Find the number of times each digit appears in the page-numbers of the book. For example, if the book has 15 pages, this is the number of times each digit 
# appears:
# {
# 0: 1,
# 1: 8,
# 2: 2,
# 3: 2,
# 4: 2,
# 5：2，
# 6: 1,
# 7: 1,
# 8: 1,
# 9: 1 
# Write a function named digit_count that accepts the number of pages as argument. It should return a dictionary D that has the following structure. The keys of this dictionary are digits, the values are the
# frequencies of occurrence of the corresponding digits.
# You do not have to accept input from the user or print output to the console. You just have to write the
# function definition.
# Input - 15
# output- {0: 1, 1: 8, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
# input - 30
# output - {0: 3, 1: 13, 2: 13, 3: 4, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3}



def digit_count(n):
    #your code
    D={}
    for i in range(10):
        D[i]=0 
    for j in range(1,n+1):
        for k in str(j):
            D[int(k)]+=1
    return D

n=int(input())
print(digit_count(n))