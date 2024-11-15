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