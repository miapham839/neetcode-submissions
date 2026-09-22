class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack != [] and temp > stack[-1][0]:
                popped = stack.pop()
                output[popped[1]] = i - popped[1]
            stack.append([temp, i])
        return output