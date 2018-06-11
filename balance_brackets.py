###check if a string of brackets in balanced

OPENING_BRACKETS = {"{", "[", "("}
BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}

def isValid(s):
    stack = []
    for bracket in s:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif not stack:
            return False        # Can't pop from an empty stack
        elif stack.pop() != BRACKETS_MAP[bracket]:
            return False        # Closing the wrong kind of bracket
    return not stack
    
    
print(isValid('{[][[]][]()[]'))
