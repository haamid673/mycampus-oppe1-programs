program 1 - 
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

Program 2 - 

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

Program 3 - 

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

Program 4 -

# Accept a sequence of space-separated words as input. Each word is either a digit
# from "zero' to 'nine" (endpoints inclusive) or one of the two operands: "plus" or "minus". The operands and operators alternate in the sequence. In other words, no two
# consecutive words will be of the same type.
# You have to find the solution of this arithmetic problem and print the answer as an
# integer. Evaluate the expression without introducing brackets anywhere. That is,

# minus one plus two minus three
# is just -1 + 2 - 3.

def evaluate(s):
    temp_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    s= s.split()
    ans = 0
    for i in range(0, len(s) ,2):
        # if starts with plus or minus
        if s[i] == 'plus':
            ans += temp_dict[s[i+1]]
        elif s[i] == 'minus':
            ans -= temp_dict[s[i+1]]
        else:
            # it will be a number
            if i == 0:
                ans = temp_dict|s[i]
            else:
                if s[i-1] == 'plus':
                    ans += temp_dict[s[i]]
                elif s[i-1] == 'minus':
                    ans == temp_dict[s[i]]
    return ans
s = input("Enter a sequence of space-separated words: ")
print(evaluate(s))


Program 5 - 

# A data entry operator has a faulty keyboard. The keys 0 and 1 are very unreliable. Sometimes they work,
# sometimes they don't. While entering phone numbers into a database, the operator uses the letter '!' as a replacement
#  for 1 and 'o' as a replacement for 0 whenever these binary digits let him down. Both '!' and 'o' are in lower case. 
# 'l' is the first letter of the word 'land', and not capital 'i'.


# Accept a ten-digit number as input. Find the number of places where the numbers 0 and 1 have been replaced 
# by letters. If there are no such replacements, print the string No mistakes. If not, print the number of
# mistakes (replacements) and in the next line, print the correct phone number.


# Test Case 1 - 
# 987o35l7o4
# Output - 3 Mistakes
# 9870351704
# test 2 -  9874618291
# output - No Mistakes


Num= input()
count=0
real_num="" 
for i in Num:
    if i== "l":
        count+=1
        real_num+="1"
    elif i == "o":
        count+=1
        real_num+="0"
    else:
        real_num+=i
if count ==0:
    print("No mistakes")
else:
    print(str(count)+" mistakes")
    print(real_num)

Program 6 - 

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


Program 7 - 

# Accept a positive integer n as input and print the smallest integer that is
# divisible by all the integers in the range [1, n], endpoints inclusive.



def gcd(a,b): 
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def lcm(a,b):
    return (a*b) //gcd (a,b)

def lcm_n(n):
    ans = 1
    for i in range(1,n+1) :
        ans = lcm(ans, i)
    return ans
n = int(input("Enter a positive integer: "))
print (lcm_n(n))


Program 8 - 

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

Program 9 - 

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


Program 10 - 

# The scores_dataset is a list of dictionaries one of whose entries is given below for your reference:
# {'SeqNo': 1, 
# 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru',
# 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75,
# 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}
# A student X can mentor another student Y in subject if the following condition is satisfied:
# 10≤X.subject-Y.subject<20
# Write a function named mentors that accepts the following arguments:
# scores_dataset
# subject

# The function should return a dictionary having the following structure:
# key: SeqNo of a student
# value: list of SeqNo of students who can be mentored by the above student
# 1) You do not have to accept input from the user or print output to the console.
# (2) We randomly sample five elements from the dictionary that you return and print them to the console. You dont have to worry about order in which seqNo are entered into list
# (3) Note that a student cannot mentor himself! Also, if a student cannot mentor anyone, then the list should be empty.


def mentors(scores_dataset, subject):
    L={}
    for student in scores_dataset:
        L[student ["SeqNo" ]]=[]
        for j in scores_dataset:
            marks=student[subject]/-j[subject]
            if 10<=marks<=20:
                L[student['SeqNo ']].append(j['SeqNo'])
    return L


Program 11 -


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



Program 12 - 

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


Program 13 - 

# para is a sequence of space-separated words. All words will be in lower case.There will be a single space between 
# consecutive words. The string has no other special characters other than the space.

# Write a function named exact_count that accepts the string para and a positive integer n as arguments. You 
# have to return True if there is at least one word in para that occurs exactly n times, and False otherwise.
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def exact_count (para, n) :
    para=para.split(" ")
    D={}
    for i in para:
        if i not in D:
            D[i]=1 #D ["hello"]=1
        else:
            D[i]+=1
    for i in D:
        if D[i]==n:
            return True
        else:
            return False


Program 14 - 

# # In a portal login website, you are asked to write a function get_password_strength
# to decide the strength of a password.
# The strength is decided based on the total score of the password, Use following
# conditions:
# If password has length greater than 7 then score increases by one point.
# If password has at least one upper case and one lower case alphabets score increases
# by one point.
# If password has at least one number and no consecutive numbers like 12 or 234 then
# score increases by one point.
# If password has at least one special character (any character other than numbers and
# alphabets) then score increases by one point
# If password contains username then it is invalid password.
# If the password has score of four points, three points, two points, or one point then print very strong, Strong ,Moderate, or, Weak respectively. If the password is
# invalid, then print PASSWORD SHOULD NOT CONTAIN USERNAME and If the score is zero, then
# print Use a different password. The arguments to the function are username and
# password which are already defined.

# Sample Input:
# username = "John"
# password = "John1234"

# Sample Output:
# Invalid Password

# Sample Input:
# username = "John"
# password = "John1234#"'

# Sample Output:
#invalid password



def get_password_strength(username, password):
    score = 0
    if len (password) > 7:
        score += 1
    if any(i.isupper() for i in password) and any(i.islower() for i in password):
        score += 1
    if any(i.isdigit() for i in password):
        score += 1
    if any(not i.isalnum() for i in password):
        score += 1
    if username in password:
        return ("PASSWORD SHOULD NOT CONTAIN USERNAME" )
    if score == 0:
        return("Use a different password")
    elif score == 1:
        return ("Weak" )
    elif score == 2:
        return ("Moderate")
    elif score == 3:
            return("Strong")
    elif score == 4:
            return("Very strong")

Program 15 - 

#A phone number belonging to a specific operator is valid if it satisfies all the 
# following conditions: It should have 10 digits It should begin with 98123
# A digit can occur at most five times Keep accepting a phone number as input on each line. The last line of the input
# stream will have the word STOP. Create a dictionary named D. The keys should be the phone numbers. If a phone number is valid, then the value corresponding to it should be VALID, if not, the
# value should be INVALID. Print the dictionary as output. The keys and values of the dictionary should be of type str. The keys should be added to the dictionary in the order in which they
# appear in the test-case area.

def valid_phone_number(phone_number):
    if len(phone_number) != 10:
        return False
    if phone_number [:5] != '98123':
        return False
    for i in phone_number:
        if phone_number.count (i) > 5:
            return False
    return True

D = {}
while True:
    phone_number = input()
    if phone_number == 'STOP':
        break
    if valid_phone_number (phone_number):
        D [phone_number] = 'VALID'
    else:
        D [phone_number] = ' INVALID'
print (D)


Program 16 - 

# players is a dictionary that has the details of the sports played by some people. The keys are names of the people. The value corresponding to a key is another dictionary. The keys of the inner dictionary are the names of the sports, and the values are Boolean values which represent whether the person plays a sport or
# not. For example:

# players = {
# 
# 'Karthik': { 
# 'Tennis': True,
# 'Badminton': True,
# 'Cricket': False 
# }, 

# 'Rahul!': { 
# 'Tennis': False, 
# 'Badminton': False
# 'Cricket': True 
#   }
#｝


# Here, Karthik plays tennis and badminton, but not cricket.
# Write a function named exactly_two that accepts the dictionary players as argument and returns the set of
# all players who play exactly two sports.

# You do not have to accept input from the user or print output to the console. You just have to write the 
# function definition.

def exactly_two(players):
    d=[]
    for i in players:
        sport_count=0
    if players [i] ['Tennis']:
        sport_count+=1
    if players [i] ['Badminton']:
        sport_count+=1
    if players[i]['Cricket']:
        sport_count+=1
    if sport_count==2:
        d.append(i)
    return set(d)


Program 17 - 

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


Program 18 - 


# The scores_dataset is a list of dictionaries one of whose entries is given below for your reference: 
# {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru',
#'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75,
# 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}
# An institution decides to allow students to create student groups for each subject where students with similar marks can help each other. But it draws up a set of constraints for creating student groups:
# A group should be associated with a particular subject.
# The difference between the scores of any two students in the group should be at most mark_limit.
# It follows that multiple groups can be formed for a given subject.

# Write a function called crowded_group that accepts three arguments as input:
# scores_dataset
# subject
# mark_limit
# Return the size of the largest possible group in this subject with the given mark_limit.


def crowded_group(scores, sub, limit):
    lis= []
    for st in scores:
        lis.append(st[sub])
    lis.sort()
    grp=0 
    for i in range(len(lis)):
        for j in range (len(lis)):
            if list[j]-lis[i]<=limit: 
                if j-i+1>grp:
                    grp=j-i+1
    return grp


Program 19 - 


# Gurunath is a popular store inside IIT Madras. Among other things, it sells stationary items. The owner of the 
# stores gives you the list of transactions that have happened in a day. Each transcation comes with aunique 
# transaction ID. He wants to estaimte the cost of each transaction. Can you help him out?
# The list trans is a list of transactions that happened at the shop in a given day. Each element of this list 
# is a dictionary. The details of one such transaction is given below:
# {
# 
# 'TID': 'Gurunath_8528', 
# 'Items': [
    # {'Name': 'Notebook', 'Price': 50, 'Qty': 4},
    # {'Name': 'Pencil', 'Price': 10, 'Qty': 1}, 
    # {'Name': 'Eraser', 'Price': 15, 'Qty': 1}, 
    # {'Name': 'File', 'Price': 80, 'Qty': 1}
#       ]
# }

# Does this remind you of the shopping bills dataset from CT?
# Write a function named get_summary that accepts the list trans as argument. It should return a list of dictionaries. Each dictionary should have two keys: "TID" and "Cost". For example, one of the elements of the
# list would be as follows:
# { 
# "Cost": 305, 
# "TID": "Gurunath_8528"
# }

# The computation of the cost is given below:
# 50x4+10x1+15x1+80x1=305

# (1) The order of elements in the returned list should be the same as the order in the input list. That is the ith 
# element in the returned list should correspond to the transaction cost of the ith element in trans.

# (2) You do not have to accept input from the user or print the output to the console. You just have to write the function definition.



def get_summary(trans):
    D=[]
    for i in trans:
        A={}
        cost=0
        for items in i["Items"]:
            cost+=int(items["Price"])*int(items["Qty"])
        A["Cost"]=cost
        A["TID"]=i["TID"]
        D.append(A)
    return D


Program 20 - 

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



Program 21 - 

#Results is a dictionary that holds information about the votes polled in a student election. The keys of the dictionary are the names of the candidates. The 
# values are the corresponding votes won by each of the candidates. Write a function named out come that accepts results as argument and returns the name of the candidate who has won the election. You can assume
# that there will be no ties.

# Sample Innut Expected Output
# {'john': 10, 'mike': 8, 'stan': 5, 'eric': 3, 'will': 2, 'joe': 1} -- "'john'
# {'john':*10, 'mike': 8, 'stan': 5, 'eric': 3, 'will': 2, 'joe': 1, 'jane': 10}'---jane'


def outcome(results):
    max = 0
    for i in results:
        if results [i] > max:
            max = results[i]
            name = i
    return name
results = {'john': 10, 'mike': 8, 'stan': 5, 'eric': 3, 'will': 2, 'joe': 1}
print(outcome(results))