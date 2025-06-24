class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        a = 0

        for i, a in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < a:
                yesterday = stack.pop()
                res[yesterday] = i - yesterday
            stack.append(i)
        return res 
        