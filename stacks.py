def is_balanced(expression):
    stack = [] # list of stack
    # Dict used to map closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression: # Iterate through each character in the expression
        if char in '({[':  # If is an opening bracket
            stack.append(char) # it's added to the track
        elif char in ')}]': # Else if it is a closing bracket
            if not stack or mapping[char] != stack.pop(): # If stack is empty, or mapping doesn't match the last added opening bracket, => false. Else => last added opening bracket is popped from the stack
                return False

    return not stack  # If it matches returns true


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1)) 
print(is_balanced(expression2))  
