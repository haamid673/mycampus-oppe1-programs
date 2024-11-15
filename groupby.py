# Consider the list L = [1, 2, 1, 5, 4, 5, 4, 3, 41. 
# Group-by is an operation on a list L that does the following: it combines identical elements in L into a list. That is, it creates a list for each
# unique element in L and all the copies of this element go into this list.
# The result of a group-by operation is a nested list.
# For example, group_by (L) should return the following list:
#  [[1, 11, [2], [3], [4, 4, 4], [5, 5]]
# Write a function named group_by that accepts a list of positive integers as 
# argument. Perform a group-by operation on the list and return the nested list. 
# The order in which you arrange the inner lists doesn't matter.
# The input will be a non-empty list. You do not have to accept input from the user or print output to the console. You 
# just have to write the function definition.


def group_by(L) :
    L.sort()
    ans = []
    i = 0
    while i < len(L): 
        temp = []
        temp.append (L[i])
        J= 1 + 1
        while j < len(L) and L[j] == L[i]:
            temp.append(L[j])
            j += 1
        ans.append(temp)
        i = j
    return ans
L = [1, 2, 1, 5, 4, 5, 4, 3, 4]
print(group_by(L))