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