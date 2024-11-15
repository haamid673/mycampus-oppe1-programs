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