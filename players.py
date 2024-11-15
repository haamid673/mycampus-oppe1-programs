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