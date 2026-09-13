class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']': '[', '}':'{'}
        for i in s:
            if i in pairs.values():
                stack.append(i)
            else:
                if not stack or pairs[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return stack == []


        