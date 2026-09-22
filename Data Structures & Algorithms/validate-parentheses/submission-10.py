class Solution:
    def isValid(self, s: str) -> bool:
        # init stack
        stack = []

        # dictionary:
        pairs = { '(' : ')', '{' : '}', '[' : ']'}
        
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if (stack != []) and (i == pairs[stack[-1]]):
                    stack.pop()
                else:
                    return False
        return stack == []
