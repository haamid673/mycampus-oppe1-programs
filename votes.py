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