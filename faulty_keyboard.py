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