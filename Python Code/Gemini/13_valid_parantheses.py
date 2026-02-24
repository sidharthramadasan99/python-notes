#13_valid_parantheses.py
#
#
#

def isValid(s):
    stack = []
    mapping = {
        ")": "(",
        "}":"{",
        "]":"["
        }
    
    for char in s:
        if char in mapping:
            # Pop top element if stack is not empty, else use dummy '#'
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False 
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
            
            return not stack # If stack is empty, it's valid