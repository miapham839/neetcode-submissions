class Solution:
    '''
    - Dictionary: K-V: close bracket - open
    - init stack
    - Iterate over s
        if s not closing brack -> add to stack
        else, check if top of stack is matching opening bracket
            if matches, pop the stack
            else: return False
        return stack empty?
    - 
    '''
    def isValid(self, s: str) -> bool:
        # Declare dictionary. K-V: close bracket - open bracket
        matches = { '}':'{', ')':'(', ']':'[' }
        # Init stack
        char_stack = []
        # Iterate over s
        for i in s:
            # if i is not a closing bracket -> add to stack
            if i not in matches.keys():
                char_stack.append(i)
            # else, check if it matches the top of the stack
            else:
                if char_stack == []:
                    return False
                elif matches[i] == char_stack[-1]:
                    char_stack.pop()
                else:
                    # Found a not-matching pair
                    return False
        # If there's still an opening bracket not popped off the stack --> not valid
        return char_stack == []


        