# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# ([]){}() is valid
# ([)] is not valid
# Last in first out

def isValid(string):
    bracket_list = []
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for bracket in string:
        # iterates oevr key of dictionary
        if bracket in brackets:
            bracket_list.append(bracket)
        elif len(bracket_list)==0 or bracket!=brackets[bracket_list.pop()]:
            return False

    return len(bracket_list)==0

print(isValid('(([]){}()'))