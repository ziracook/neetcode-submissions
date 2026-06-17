class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # Pairs of values, temp + index

        for i, t in enumerate(temperatures):
            # While the current temp is greater than whats on the top of the stack
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t, i])

        return res

        