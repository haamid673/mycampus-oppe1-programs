# A square matrix M is said to be:

# diagonal: if the entries outside the main-diagonal are all zeros
# scalar: if it is a diagonal matrix, all of whose diagonal elements are equal
# identity: if it is a scalar matrix, all of whose diagonal elements are equal to 1

# Write a function named matrix_type that accepts a matrix Mas argument and returns the type of matrix. It should be 
# one of these strings: diagonal, scalar, identity, non-diagonal. The type you output should be the most appropriate 
# one for the given matrix.
# You do not have to accept input from the user or print output to the console. You just have to write the
# function definition.


def matrix_type(M): 
    B=M[0][0]
    identity=0
    scalar=0
    for i in range(len(M)):
        for j in range(len(M)):
            if i!=j:
                if M[i][j]!=0:
                    return("non-diagonal")
            else:
                #for identity
                if M[i][j]==1:
                    identity+=1
                else:
                    if M[i][j]==B:
                        scalar+=1
    if identity ==len(M):
        return("identity")
    else:
        if scalar==len(M):
            return("scalar")
        else:
            return("diagonal")
