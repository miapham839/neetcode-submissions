class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Declare stack
        stack = []
        # Iterate over input list
        for i in tokens:
            # If operators
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1 - num2)
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(int(num1 / num2))   
            # If number, add to stack
            else:
                stack.append(int(i))  
        # return top of stack
        return stack[0]
