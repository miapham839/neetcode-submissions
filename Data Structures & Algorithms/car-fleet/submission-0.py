class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort and create list of (position, speed) tuples
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for car in pair:
            if stack != [] and ((target - car[0])/car[1] <= (target - stack[-1][0])/stack[-1][1]):
                continue
            stack.append(car)
        return len(stack)

        