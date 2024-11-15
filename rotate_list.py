#A clockwise rotation of a list consists of taking the last element and moving it to the beginning of the list. For instance, if we rotate the list 11, 2, 3, 4, 51, we get 15, 1, 2, 3, 41. If we rotate it again, we get 14, 5, 1, 2, 31. Your task is to
# perform k rotations of a list.

# The first line of input contains a non-empty sequence of comma-separated integers. The second line of input is a positive integer k. Perform k rotations of the list and
# print it as a sequence of comma-separated integers.

def rotate (L):
    L.insert(0, L.pop())
    return L

L= [1, 2, 3, 4, 5]
k = int(input ("Enter a positive integer: "))
for i in range(k):
    L = rotate (L)
print(L)
