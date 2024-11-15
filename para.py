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
