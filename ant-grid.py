# Consider a grid-world that is inhabited by an ant (BLUE). The ant can move only in two directions: UP or 
# RIGHT. The ant has sensed the presence of a source of food somewhere in the grid. Your task is twofold:
# Determine if the ant can reach the food source.
# If it can, find out the number of steps it has to take.
# For example, in the grid-world on the left, the ant can reach the food source in five steps. On the right,
# it can't.
# The grid-world is represented as a matrix of strings: 'B' stands for the initial position of the ant, 'W' stands for an empty cell and 'G' stands for the food source. For example, the grid-world on the left is
# represented as:



# Write a function named is_reachable that accepts a
# nxn matrix of strings named grid as argument. Return (True, steps) if the ant can reach the food source, where steps is the number of steps the ant needs to take. If it can't reach the food source, return (False, 
# None)

def is_reachable(grid): 
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='G':
                g=i,j
            elif grid[i][j]=='B':
                b=[i,j]

    if b[0]>=g[0] and b[1]<=g[1]:
        ans=abs (b[0]-g[0])+abs(b[1]-g[1])

        return True, ans
    else:
        return False, None
    


# functions, for, conditionals, 2d lists, return