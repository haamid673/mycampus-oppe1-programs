#We shall define the distance between two points Pi = (x1, y1) and P2 = (x2, y2) in 2-D space as follows:
#        D(PI, P2) = |x1 - x2| + ly1 - y2|

# where, la - b| is the absolute value of the difference between two numbers a and b.
# Write a function named equidistant that accepts a list of points, a point P and a positive integer d 
# as arguments. It should return the number of points in the list points that are at a distanced from the point P.
# Each point is represented as a tuple - (x, y). The list points is a list of tuples.
# You do not have to accept input from the user or print output to the console. You just have to write the function
# definition.

#input-［（0,0), (2,0),(1,1), (1,-1), (3,0)
#        (1,0)
# output- 4
# input - [(0, 2), (1, 3), (-4, 3), (0, 10), (-5, 3)]
#        (1, 3)
#        4
# output- 0



def equidistant (List,P,d):
    count=0
    for i in List:
        if (abs(P[0]-i [0]) +abs(P[1]-i[1]))==d:
            count+=1
    return count

# List=[(0, 0), (2, 0), (1, 1), (1, -1), (3, 0)]
# P=(1,0)
# d=1

List=[(0, 2), (1, 3), (-4, 3), (0, 10), (-5, 3)]
P=(1, 3)
d=4
print(equidistant (List,P,d))