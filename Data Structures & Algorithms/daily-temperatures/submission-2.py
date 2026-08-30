class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            # While there is a stack and curr_temp
            # is higher than top of stack temp, you
            # go back into the stack and mark the difference
            # in index
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        return res



