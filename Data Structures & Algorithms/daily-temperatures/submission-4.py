class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        maximum = len(temperatures)-1
        for i, v in enumerate(temperatures):
            if len(stack) != 0 and temperatures[i] > stack[-1][1]:
                while stack and v > stack[-1][1]:
                    save = stack.pop()
                    result[save[0]] = i - save[0]
            stack.append([i, v])
        return result
