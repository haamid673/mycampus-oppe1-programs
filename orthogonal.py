#Two vectors are orthogonal to each other if their dot-product is zero. Write a
# function named orthogonal that accepts two arguments:
# L: a list of vectors; this is represented as a list of lists
# V: a vector; this is represented as a list
# Return the number of vectors in the list L that are orthogonal to the vector v.

def orthogonal(L,V) :
    count = 0
    for i in L:
        dot = 0 
        for j in range(len(i)):
            dot += i[j] * v[j]
        if dot == 0:
            count += 1
    return count

L = [[1, 2, 3], [2, -1, 1], [3, 0, -1], [2, 3, 1]]
v = [1, 1, 1]
print(orthogonal(L, v))
