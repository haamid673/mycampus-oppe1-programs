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
